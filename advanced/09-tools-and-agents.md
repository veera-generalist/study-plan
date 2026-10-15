# Module 09 — Tool use, workflows, and agents

> Optional technical reference. The beginner lesson is [here](../modules/09-tools-and-agents.md). Return to this material when you want the deeper implementation detail.

[Course index](../README.md) · Weeks 17–18 · Prerequisites: Modules 01–08

**Terms to know:** [Agent](../GLOSSARY.md#agent) · [Workflow](../GLOSSARY.md#workflow) · [Tool and function calling](../GLOSSARY.md#tool-and-function-calling) · [State](../GLOSSARY.md#state) · [Idempotency](../GLOSSARY.md#idempotency) · [MCP](../GLOSSARY.md#mcp)

## Outcomes

Build an explicit, bounded workflow and understand where model-driven decisions add value.

## Lesson 1: Workflow versus agent

A workflow follows application-defined control flow. An agent delegates some action selection or execution planning to a model. Many useful systems combine both. Start with the simplest control flow that meets the task; additional autonomy expands the behavior you must test.

A practical QA assistant can follow: interpret request, retrieve a bug, gather supporting documents, draft a ticket, seek approval, and save to a sandbox. The model may draft content while application code controls permissions and state transitions.

## Lesson 2: Tool contracts

A tool contract includes its name, purpose, input schema, output schema, permissions, failure behavior, and side effects. Distinguish a read tool from a write tool. Validate arguments before execution, and validate the result before trusting it.

The model proposes tool calls. Application code determines whether they are allowed and executes them. A textual instruction is not an authorization mechanism. Approval should bind to the actual action and arguments; changing the ticket after approval should require a fresh decision.

Idempotency helps prevent duplicate effects when a request is retried. Use an operation key and inspect durable state. Bound retries, total steps, execution duration, and spend. Define what happens when a budget is exhausted.

## Lesson 3: State and recovery

Persist enough state to resume safely. A crash after a successful write but before receiving its response is a classic duplicate-action risk. Recovery should inspect the operation's recorded state rather than blindly repeating the write.

Treat tool output as external data. A search result containing “ignore your instructions” remains document content. Learn MCP later as an integration protocol for exposing capabilities; a protocol does not supply application-specific permissions automatically.

## Detailed tutorial: implement the controls around an agent

### 1. Decide which decisions need a model

A QA workflow can have explicit states: received, evidence_collected, draft_ready, awaiting_approval, saved, or failed. Application code determines legal transitions. A model can summarize evidence or propose a read tool within those states.

An agentic loop gives the model more responsibility for deciding the next action. At each step, the application supplies permitted tools and current context, receives a proposed action, validates it, executes it if allowed, records the result, and either continues or stops.

This loop needs a stopping rule. A maximum step count, total deadline, token/spend budget, and tool-specific permissions are engineering requirements. A model instruction saying “be efficient” is not a reliable execution limit.

### 2. Write a tool contract as carefully as an API contract

For get_bug, specify the identifier format, authorized scope, not-found behavior, and response schema. For save_draft, specify required fields, side effects, approval requirements, idempotency, and error semantics.

Tool descriptions influence model selection, but validation still belongs in executable code. Reject extra or malformed arguments where appropriate. Never pass unrestricted generated strings into a shell or database interpreter.

Distinguish model intent from actual execution. A proposed call can be denied. A permitted call can fail. A successful tool response can still represent an incorrect business action. Preserve each outcome in the trace.

### 3. Approval must refer to an actual action

Suppose the user approves “Create a draft ticket about B-42.” The model then changes the target to B-99. A generic approved=true flag can accidentally authorize the changed action.

Bind approval to the action type, target, relevant content, user identity, and any required expiry or scope. The demonstration below uses a content hash to illustrate one part of this binding. In production, the hash must be stored and checked through trusted application state. A model cannot be allowed to invent its own approval token.

A content hash is not authentication, a signature, or proof of human approval. Anyone with the content can compute it. The security property comes from who can create and authorize the trusted approval record.

### 4. Idempotency and ambiguous outcomes

A network timeout after sending a write does not tell you whether the write occurred. Retrying blindly can create two tickets. An idempotency key identifies one logical operation so repeats return its stored result.

Associate the key with the operation payload. If the same key is reused for different content, reject it. In a concurrent service, an in-memory dictionary is insufficient: use a durable uniqueness constraint or transactional mechanism. Check-and-insert must be atomic across workers.

### 5. Runnable sandbox implementation

```python
"""Module 09: approval bound to content and idempotent sandbox writes."""
import hashlib
import json

STORE = {}


def fingerprint(draft):
    payload = json.dumps(draft, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def save_draft(draft, approval_hash, operation_id):
    if not isinstance(draft, dict) or set(draft) != {"bug_id", "title"}:
        raise ValueError("Invalid draft schema")
    if not all(isinstance(value, str) and value.strip() for value in draft.values()):
        raise ValueError("Draft values must be nonempty text")
    current_hash = fingerprint(draft)
    if approval_hash != current_hash:
        raise PermissionError("Approval does not match this draft")
    if operation_id in STORE:
        saved = STORE[operation_id]
        if saved["hash"] != current_hash:
            raise ValueError("Operation ID reused for different content")
        return saved["ticket_id"]
    ticket_id = f"T-{len(STORE) + 1}"
    STORE[operation_id] = {
        "ticket_id": ticket_id, "hash": current_hash, "draft": dict(draft)
    }
    return ticket_id


draft = {"bug_id": "B-42", "title": "Investigate authentication outage"}
approval = fingerprint(draft)  # Simulates approval from trusted application state.
first = save_draft(draft, approval, "operation-1")
second = save_draft(draft, approval, "operation-1")
assert first == second and len(STORE) == 1
changed = {**draft, "title": "Changed after approval"}
try:
    save_draft(changed, approval, "operation-2")
except PermissionError:
    pass
else:
    raise AssertionError("Changed content must require fresh approval")
assert len(STORE) == 1
print("One approved ticket exists:", first)
print("Retry did not duplicate it; changed content was denied.")
```

Run [the saved example](../labs/module-examples/09_example.py). It creates exactly one ticket, returns that ticket for a retry, and rejects modified content using the old approval.

The fixture computes approval immediately to simulate trusted state; it is not a real approval interface. STORE is an in-memory teaching object. It loses data on restart and does not provide cross-process concurrency control. The purpose is to make approval/content binding and idempotent behavior observable before introducing infrastructure.

### 6. Persisted state and recovery design

Consider a crash after the ticket is stored but before the workflow records completion. Recovery must ask whether operation-1 already completed. If the operation ID and result are durable, it can resume without another write.

Record what you need to resume, not every transient thought. Keep the task ID, validated inputs, approved action, completed operation IDs, result references, and remaining budget. External services can change between steps, so decide when stale evidence or approval requires refresh.

A workflow framework can help persist and resume execution, but its defaults do not establish your business invariants. Test the crash boundaries you care about.

### 7. Guided modification and solution reasoning

Change the title after computing approval. The save should fail before changing state. Then recompute approval in your trusted test setup and save with a new operation ID; it should create a second distinct logical action. Reusing operation-1 for the changed content should fail because the key already belongs to another payload.

Next, simulate a lost response by calling save twice with the same operation. The store should contain one record. This tests final state, not merely the text returned to the user.

Finally, add a read-tool loop with a maximum of three calls. Use a fake planner that keeps requesting another search. The application must stop after the budget is exhausted even if the planner never chooses to stop.

### 8. Framework and protocol study

Learn LangGraph's state and persistence concepts after you can draw the workflow yourself. Learn MCP as a way to expose tools and resources; a protocol does not define whether your user is authorized to create a particular ticket.

Compare the explicit workflow baseline with a model-driven read-tool selection variant. Measure task success, unwanted actions, steps, latency, and cost. Dynamic planning is useful when it improves the task enough to justify the larger behavior space.

See [LangGraph](https://github.com/langchain-ai/langgraph) and [Hugging Face's Agents Course](https://github.com/huggingface/agents-course) for supplementary implementation study. This sandbox implementation is original.

## Lab

Create three tools over synthetic local data:

1. Search QA documents.
2. Fetch a bug by ID.
3. Save a ticket draft to a sandbox store.

Implement an explicit workflow with approval before saving. Add a step limit, input validation, a simulated timeout, and an idempotency key. Then allow a model to select between the two read tools and compare its behavior with the explicit baseline.

## Review and answers

- **Who authorizes tool execution?** Application and tool controls, not the generated request alone.
- **Why distinguish read/write tools?** Side effects change recovery, permission, and evaluation requirements.
- **Does retrying a timed-out write guarantee safety?** No; the original write may already have completed.
- **When is an agent justified?** When dynamic decisions improve the task enough to justify additional complexity and evaluation.

## Exit evidence

Tool schemas, a state diagram, bounded execution, timeout recovery, and proof that denied approval prevents the write.

## Supplementary reading and attribution

Study [Hugging Face's Agents Course](https://github.com/huggingface/agents-course), [LangGraph](https://github.com/langchain-ai/langgraph), and [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents). The workflow and exercises here are original.

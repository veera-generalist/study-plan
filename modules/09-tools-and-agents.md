# Module 09 — Tool use, workflows, and agents

[Course index](../README.md) · Weeks 17–18 · Prerequisites: Modules 01–08

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

# Module 09 — Give an assistant a small action

[Previous: comparing versions](08-rag-evaluation-and-statistics.md) · [Course home](../README.md) · [Next: testing difficult situations](10-agent-evaluation-and-security.md)

**Before you begin:** understand the difference between an answer and the information supporting it. This lesson uses a paper simulation; it does not place orders or change a real system.

## Introduction

An assistant can explain how returns work. A more capable application might also look up an order or prepare a return request.

Those are different responsibilities.

Generating the sentence “Your request has been saved” does not establish that anything was actually saved. To perform an action, the application needs a real capability and rules about using it.

This lesson introduces tools and agents through a small, visible process.

## Learning objectives

By the end, you should be able to:

1. Explain what a tool lets an assistant do.
2. Distinguish a proposed action from a completed action.
3. Describe a simple workflow with an approval step.
4. Explain why repeated requests need careful handling.

## Scenario: prepare a request for shop staff

For this lesson, add a fictional internal task:

> A customer may ask the assistant to prepare a return-request draft for shop staff. Preparing a draft does not approve a return or promise a refund.

This is a new application feature, not a change to Maple Books' return policy.

The existing conditions remain: an undamaged book, within 14 days, with a receipt.

We will simulate looking up an order and saving a draft in a practice notebook.

## Lesson

### 1. A tool is a capability exposed by the application

A **tool** is a function the surrounding software makes available for a defined purpose.

Examples include:

- Look up an order.
- Search an approved document.
- Save a return-request draft.

The model can propose using a tool. Application code decides whether the request is valid and permitted, then performs it.

A model-generated request is not automatically authority to act.

### 2. Describe the tool clearly

A useful tool description explains:

- What it does.
- What information it needs.
- What it returns.
- What it can change.
- What happens when the request cannot be completed.

For our paper exercise:

| Tool | Needs | Returns or changes |
|---|---|---|
| Look up order | An order ID and an authorized user | The permitted order details, or not found |
| Prepare draft | The needed order and return details | Text for review |
| Save draft | The approved draft | A saved draft ID |

You do not need a tool framework to understand these boundaries.

### 3. Reading and writing have different consequences

Looking up an order reads information. Saving a draft changes stored information.

A change outside the response text is called a **side effect**.

Before a write action, check the details and required permission. For a customer, the draft might need a preview and explicit approval before saving.

Private order information also needs access checks even though reading does not modify a record.

### 4. A workflow prescribes the order of steps

A **workflow** is a process the application defines.

Our example is:

~~~text
Receive the request
        ↓
Check access and find the order
        ↓
Collect the needed details
        ↓
Prepare and show a draft
        ↓
Obtain approval for that draft
        ↓
Save it and report the actual result
~~~

The model may help write the draft while the application controls the order of operations.

This is already a useful AI application. It does not need unrestricted autonomy.

### 5. An agent chooses some actions dynamically

An **agent** delegates some decisions about what to do next to a model.

For example, it may choose whether to search a policy document or look up an order first, based on the request.

The application still needs boundaries: which tools are available, what is permitted, how long the process can run, and when to ask for help.

A workflow and an agent can be combined. The useful question is what degree of decision-making the task needs.

### 6. Keep track of progress

The application needs to know what has happened so far. This is its **state**.

For the draft request, useful state includes:

- Which order is involved.
- Which details were confirmed.
- What draft was shown.
- Whether that specific draft was approved.
- Whether it was saved.
- The resulting draft ID.

Without this record, the assistant might confuse a proposed action with a completed one.

### 7. Approval should refer to the actual draft

Suppose the customer approves a draft for order O-101. The assistant then changes it to order O-202.

The old approval should not automatically authorize the changed draft.

The application must connect approval with the action and details the person actually reviewed. The model should not create its own proof of approval.

For now, write down the exact approved draft in your simulation.

### 8. Repeating an action can create duplicates

Imagine the save action completed, but the reply was lost. The customer asks again.

Saving again without checking could create two drafts.

**Idempotency** means handling repeated attempts at the same logical operation without creating additional unintended effects.

You can understand the idea by assigning the intended save an operation ID and checking whether it already has a result. Real implementations need durable, reliable storage; a paper note is only a learning model.

### 9. Set a stopping rule

An assistant can get stuck asking for more searches or repeatedly trying a failed tool.

Define a limit, such as a maximum number of steps or a requirement to ask a person after a failed attempt.

“Keep trying until it works” is not a complete operating policy.

## Walkthrough: simulate a draft request

Use these invented order details:

> Order O-101 belongs to the requesting customer. It was purchased ten days ago. The customer reports that the book is undamaged and has the receipt.

The customer asks:

> Please prepare a return request.

A careful sequence is:

1. Confirm that the application is permitted to access O-101.
2. Retrieve the stated order details.
3. Prepare a draft saying the customer requests a return and reports those conditions.
4. Show the draft for review.
5. Ask whether the customer wants that draft saved.
6. Save only after approval.
7. Report the actual saved draft ID.

The assistant should not say the refund has been approved. Preparing a draft and approving a return are different actions.

If the save action fails, the final reply must reflect that failure rather than invent a draft ID.

## Try it yourself

Act as the application and write down what you would do:

1. The order cannot be found.
2. The customer declines to save the draft.
3. The draft changes after approval.
4. The customer repeats the same save request after a delayed reply.

For each case, identify which information or state you need before continuing.

## Assignment

Draw a small workflow for an assistant action of your choice.

Use only a pretend environment. Define the read tools, write tools, required approval, stopping rule, and evidence of completion.

Walk through one normal task and one failure. Record what should be different in the final state.

You do not need to install an agent framework or connect to a real order system.

## Knowledge check

1. Does saying “saved” establish that a tool completed?
2. Who decides whether a proposed tool call may execute?
3. What makes an agent different from a fixed workflow?
4. Why should changed draft content require a new approval decision?
5. What problem does idempotency address?

<details>
<summary>Read the answers and explanations</summary>

1. No. Inspect the actual tool result or stored state.
2. Application and tool controls enforce the relevant rules.
3. An agent delegates some next-action choices to a model; a workflow prescribes the process.
4. The earlier approval applied to the details that were reviewed.
5. It helps prevent repeated attempts from creating duplicate unintended effects.

For the activity: a missing order needs clarification or a recorded failure; declined approval means no save; changed content needs review again; a repeated save requires checking whether the same operation already completed.

</details>

## What you learned

You can distinguish conversation from action and describe the controls around a small tool-using assistant.

Continue when you can explain what proves that an action happened.

## Keep learning

Continue to [Module 10: testing difficult situations](10-agent-evaluation-and-security.md).

The [optional technical note](../advanced/09-tools-and-agents.md) contains a Python sandbox implementation. [Hugging Face's Agents Course](https://github.com/huggingface/agents-course) and [LangGraph](https://github.com/langchain-ai/langgraph) are later implementation resources.

The draft workflow and order examples here are original; see [attributions](../ATTRIBUTIONS.md).

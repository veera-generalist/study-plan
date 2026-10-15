# Module 11 — Find where a failure began

[Previous: difficult situations](10-agent-evaluation-and-security.md) · [Course home](../README.md) · [Next: your first small project](12-optimization-and-career.md)

**Before you begin:** understand the simple document-answering and draft-saving processes. A written step record is enough for this lesson.

## Introduction

A customer receives the wrong closing time.

You could change the prompt immediately. But what if the application selected an old document? What if the model produced a correct answer and another part of the application changed it?

To improve the system, follow the information through the steps.

This lesson introduces a simple record of what happened and shows how that record supports a decision about a change.

## Learning objectives

By the end, you should be able to:

1. Keep a useful record of one assistant task.
2. Distinguish a source problem from an answer problem.
3. Record the relevant version of instructions and information.
4. Write a clear recommendation about trying or holding a change.

## Scenario: Saturday closing time is wrong

The customer asks:

> What time do you close on Saturday?

The approved current opening-hours document says 6 p.m. The customer sees:

> We close at 7 p.m.

You need to know more than “the answer failed.” You need the intermediate evidence.

## Lesson

### 1. Record the steps of one task

For a document-answering task, record:

- The exact question.
- Which source was selected.
- What text was sent to the model.
- What the model returned.
- What the user finally saw.
- Any failure or retry.

For a tool action, add the proposed tool call, permission/approval decision, result, and final state.

This can begin as a small table. You do not need a monitoring platform to understand the idea.

### 2. Learn a few names after seeing their purpose

A **log** is a recorded event or message.

A **trace** connects events and operations belonging to one execution. It helps you follow the task across its steps.

A **span** represents one operation within that trace, such as searching a document or calling a model.

These are implementation terms. Their purpose is to make the process visible enough to investigate.

The wider ability to understand a system from such evidence is often called **observability**.

### 3. Compare what each step received and produced

If the source supplied to the model says 7 p.m. because it is an old draft, investigate source selection.

If the actual model request contains the approved 6 p.m. fact but its response says 7 p.m., the needed evidence was present. Investigate the instructions and response-generation step.

If the model returns 6 p.m. but the user sees 7 p.m., inspect the surrounding application.

The observation narrows the investigation. It does not always prove a complete root cause by itself.

### 4. Keep versions with the evidence

You may change the prompt or replace a document later.

If the record only says “used the policy,” you may not know which text produced the result.

Give important versions simple names, such as prompt-A and opening-hours-current-v1. Preserve the actual contents or a dependable reference to them.

For a live model run, record the available model identity and execution date too. External services can change over time.

### 5. Measure the complete task when that matters

A fast model call can sit inside a slow application.

If a customer waits ten seconds, find out whether time was spent searching, generating, retrying, or waiting for a tool.

When timing something, say what you measured: one operation or the complete user task.

You can start with a rough observation in a manual exercise. Detailed timing and dashboards are optional technical work.

### 6. Collect enough evidence without exposing private details

Keep the information needed to investigate, with appropriate access.

Do not copy real customer details into a public study notebook. Use the fictional Maple Books facts and invented orders for this course.

In an implementation, decide which records should contain full text, which can use identifiers, and who may read them.

Recording everything without thought is not the goal.

### 7. A release decision connects evidence to a purpose

A **release** makes a changed version available for use.

Before choosing a candidate, summarize:

- What changed.
- What improved.
- What got worse.
- What has not been checked.
- What you recommend next.

A small successful exercise can support further testing. It does not automatically support a broad customer rollout.

For an actual application, a limited trial and a plan to return to the previous version can reduce exposure while gathering evidence. You will encounter the terms **canary release** and **rollback** for these ideas.

### 8. Keep checks at useful stages

You do not need every expensive review after every small edit.

An implementation may have fast checks during development and broader checks before a release.

The important principle is to match the evidence to the decision. A short smoke check may show the application starts. It does not establish that policy answers and write permissions are correct.

This lesson asks for a reasoned report, not a deployment pipeline.

## Walkthrough: two records, different investigations

These are invented records for the same Saturday question.

| Step | Run A | Run B |
|---|---|---|
| Source selected | Archived draft: closes at 7 p.m. | Approved document H: closes at 6 p.m. |
| Information sent to model | The archived 7 p.m. passage | The approved 6 p.m. passage |
| Model response | “We close at 7 p.m.” | “We close at 7 p.m.” |
| Final user response | Same as model response | Same as model response |

Both final answers are wrong for the current policy.

For A, correcting source selection is a sensible first investigation.

For B, the right evidence was supplied. Inspect the full instructions and generation behavior rather than assuming the same retrieval defect.

Now imagine a third record where the model says 6 p.m. but the displayed answer says 7 p.m. That points to another application step. This is why preserving intermediate results matters.

## Try it yourself

Make a record for one question from your collection.

Use these columns:

| Step | Input or evidence | Result | What you noticed |
|---|---|---|---|
| Receive question | | | |
| Select information | | | |
| Produce answer | | | |
| Review answer | | | |

If you are simulating the process, label it as a simulation.

Then deliberately change one step and explain which evidence would reveal the change.

## Assignment

Write a one-page change recommendation for your assistant.

Use a small comparison you actually performed or a clearly labeled teaching example. Include a useful successful case and a failure.

Your recommendation can be:

- Continue investigating.
- Revise and compare again.
- Try a limited next step.

State what evidence you still need. Do not invent a successful live run or a production rollout.

## Knowledge check

1. What does a trace help you follow?
2. Why preserve the source text and prompt version?
3. Does the same wrong final answer always have the same cause?
4. Does a fast model call establish a fast complete task?
5. What should a change recommendation say about missing evidence?

<details>
<summary>Read the answers and explanations</summary>

1. The connected operations in one task.
2. So you can establish what information and instructions were actually used.
3. No. Source selection, generation, or another application step can differ.
4. No. Other steps may dominate the user's wait.
5. State the gap and how it limits the decision.

For the activity, a useful record should let you trace the changed result to the step where the relevant evidence first differed.

</details>

## What you learned

You can investigate an answer by following the process and communicate a change decision using visible evidence.

Continue when you can distinguish what you observed from what you still need to investigate.

## Keep learning

Continue to [Module 12: your first small project](12-optimization-and-career.md).

The [optional technical note](../advanced/11-observability-and-delivery.md) covers instrumentation and delivery checks. [Phoenix](https://github.com/Arize-ai/phoenix) and [OpenTelemetry's trace concepts](https://opentelemetry.io/docs/concepts/signals/traces/) are later references.

The step records and recommendation exercise here are original; see [source credits](../ATTRIBUTIONS.md).

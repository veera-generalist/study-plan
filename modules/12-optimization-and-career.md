# Module 12 — Bring it together in a small project

[Previous: investigating failures](11-observability-and-delivery.md) · [Course home](../README.md)

**Before you begin:** bring the notes and examples you made in earlier lessons. You can complete a written project first and add Python when ready.

## Introduction

You have worked through the main parts of a small AI application:

- Give it a clear purpose.
- Supply relevant information.
- Write useful instructions.
- Collect questions.
- Check answers.
- Compare a change.
- Understand tools and difficult situations.
- Investigate a failure.

Now combine those ideas into one project you can explain from beginning to end.

A small, honest project with clear evidence is a good starting point. It does not need every framework or technique you have heard about.

## Learning objectives

By the end, you should be able to:

1. Define a project small enough to complete.
2. Keep a starting version and one evaluated improvement.
3. Present successful and unsuccessful examples.
4. Distinguish a written prototype from a working implementation.
5. Choose a realistic next programming step.

## Scenario: your Maple Books assistant

Your project is:

> Help customers understand the supplied shop policies, answer supported questions, and explain missing information.

Start with answering questions. The draft-saving workflow is an optional extension, not a requirement for the first version.

You can use another domain if you have clear, reusable source information. Keep its facts small enough to check carefully.

## Lesson

### 1. Define who it helps and what it does

Write a short problem statement.

For example:

> Customers ask recurring questions about opening hours, returns, and delivery. The assistant uses approved shop information to give short, understandable answers.

Then state the boundary:

> It does not approve refunds, invent delivery services, or claim access to live stock information.

This describes the actual intended product. It also helps choose relevant questions.

### 2. Preserve the starting version

Keep the source facts, prompt, question collection, and replies from the first version.

Call this version A.

If you later improve the prompt, you will have a dependable reference. Without it, the comparison may rely on memory or a particularly memorable answer.

When you use a live tool, preserve actual replies and the available tool/model information. When you use authored examples, label them accordingly.

### 3. Choose one observed problem

Suppose A repeatedly invents services when information is absent.

A focused improvement might strengthen the missing-information instruction and add a valid demonstration.

Write:

> I expect B to avoid unsupported service claims more consistently.

Do not change every part of the application at once. A focused change is easier to interpret.

If the wrong document is being supplied, fix that step instead of only adjusting answer style.

### 4. Compare and explain

Use your development questions and the same review rules.

Keep the paired outcomes, including regressions. Select a candidate before using reserved questions for a fresh assessment.

Describe the result within its limits:

> B handled two missing-information cases better in my small exercise, but one closing-time answer regressed.

That is more useful than claiming “The assistant is accurate” without explaining the evidence.

### 5. Improve what matters for the task

A longer answer is not automatically better. A more expensive model is not automatically necessary. A faster response is not useful if it promises the wrong policy.

Choose improvements based on observed needs.

Possible next steps include clearer instructions, better source selection, a more suitable model, or an application control around a write action.

You can eventually compare quality, time, and cost together. For this first project, explain the tradeoff you actually observed rather than manufacturing measurements.

### 6. Describe the project at the right level

A **written prototype** describes prompts, examples, expected behavior, and review results.

A **working implementation** runs the relevant application steps in software.

A **live-model experiment** includes actual model requests and recorded responses.

These can all be useful learning artifacts. They demonstrate different things.

If you manually chose each document and pasted it into a chat tool, you have practiced the document-answering process. Do not claim to have built automated retrieval.

If you did not connect a real order system, say the tool workflow was simulated.

### 7. Choose a gentle Python next step

Python remains the language for implementation in this course.

Start by automating something you already understand:

1. Store a few questions and reviewed outcomes.
2. Print a simple summary, like the optional example in Module 05.
3. Read the records from a file.
4. Add a small model adapter when the data flow is clear.
5. Keep request failures separate from valid but wrong answers.

You do not need to jump immediately into complex frameworks.

The optional local-model lab is one later adapter example. It needs separate setup, and its tests use simulated service responses. A real inference run still needs your chosen model environment.

### 8. Present a failure as part of the work

Choose one informative failure and show:

- The question.
- The source information.
- The reply or action.
- The rule it failed.
- Your likely explanation.
- The change you tried or would try.

A failure is valuable when it reveals engineering judgment. Hiding every weak example makes the project harder to assess.

### 9. Connect evidence to your career direction

For AI engineering, show the components you built and how they work together.

For evaluation engineering, show how you chose examples, defined expected behavior, reviewed outcomes, and interpreted a change.

A project can demonstrate both. State which parts you implemented and which remain planned.

Your project description should report actual work. Add numerical results only when you have stored records that support them.

## Walkthrough: a simple project report

Here is a report outline using invented teaching outcomes:

> **Purpose:** Answer questions about the supplied Maple Books policies.
>
> **Starting point:** Prompt A plus the three approved shop documents.
>
> **Observed issue:** Some missing-information questions produced invented service details.
>
> **Change:** Prompt B explicitly states how to handle missing information.
>
> **Development result:** B fixes two examples and breaks one previously correct example.
>
> **Decision:** Investigate the regression before selecting B.
>
> **Next evidence needed:** A revised candidate, a repeated comparison, and fresh questions after selection.

This outline makes the work understandable without requiring a dashboard.

In your own report, replace the teaching outcomes with what you actually observed. If the project is written-only, state that prominently.

## Try it yourself

Prepare a two-minute explanation of your project:

1. What does it help someone do?
2. What information does it use?
3. What did you check?
4. What went wrong?
5. What is your next step?

Try explaining it without unexplained acronyms. If a sentence depends on a term you cannot explain, return to the relevant lesson.

## Assignment

Create a small project folder or document containing:

- The problem and scope.
- The source facts and their origin.
- Prompt A and one revised prompt.
- A small question collection and review rules.
- Actual replies or clearly labeled supplied examples.
- A paired comparison.
- One failure analysis.
- A short recommendation and limitations.

A collection of about ten carefully reviewed questions is a useful learning target, not a guarantee of reliability. Start smaller if necessary.

Choose either a written prototype or a working implementation. Label it accurately. Add the simulated draft workflow only if the question-answering part is understandable and complete enough for your learning goal.

## Knowledge check

1. Why preserve a starting version?
2. Should you fix every component at once?
3. Does manually pasting documents establish automated retrieval?
4. What should a portfolio claim say about a simulated tool?
5. What is a sensible first Python step?

<details>
<summary>Read the answers and explanations</summary>

1. It gives you evidence for a comparison rather than relying on memory.
2. Usually start with a focused change tied to an observed problem.
3. No. It demonstrates the manual process, not an automated implementation.
4. State that it was simulated and describe what was actually checked.
5. Automate a familiar, small operation such as storing examples and counting reviewed outcomes.

For the presentation activity, a clear description should separate completed work, observed results, and planned next steps.

</details>

## What you learned

You now have a path from an assistant idea to a small project with reviewable evidence.

The next step is to deepen implementation at a comfortable pace while keeping the same habits: clear purpose, suitable information, explicit checks, visible failures, and honest conclusions.

Completing the introductory lessons builds understanding. Professional readiness also requires continued programming practice and experience with working systems.

## Keep learning

Choose a [project brief](../projects/README.md) when you want a larger implementation task.

For coding, return to [the optional Python note](../advanced/01-python-engineering.md) and the [local-model adapter lab](../labs/live-model/README.md) when their prerequisites make sense.

The [optional technical note for this lesson](../advanced/12-optimization-and-career.md) explores optimization and more formal portfolio evidence. [DSPy](https://github.com/stanfordnlp/dspy) is later reading after you have trustworthy evaluation examples.

The project narrative, report outline, and activities here are original; see [attributions](../ATTRIBUTIONS.md).

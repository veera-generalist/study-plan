# Module 03 — Writing useful prompts

[Previous: understanding language models](02-model-foundations.md) · [Course home](../README.md) · [Next: collecting questions](04-datasets-and-oracles.md)

**Before you begin:** complete Modules 01–02. You can do this lesson with the written examples. An AI chat tool is useful for optional practice; no coding setup is required.

## Introduction

You have a purpose for the Maple Books assistant and you know that a language model uses the information available to it.

The next step is to ask it for the behavior you want.

A vague request leaves many decisions open. A clear request describes the task, supplies relevant information, and explains what a useful answer should look like.

Writing and improving those requests is often called **prompt engineering**. You can begin with ordinary language.

## Learning objectives

By the end, you should be able to:

1. Write a prompt with a clear task and relevant information.
2. Ask for an appropriate answer format.
3. Explain what to do when information is missing.
4. Improve a prompt by examining the responses it produces.

## Scenario: a question the shop cannot answer yet

A customer asks:

> Do you offer same-day delivery?

We know:

> Delivery within Riverton takes three working days.

That fact does not say whether a separate same-day service exists.

A useful assistant should make that limit clear. A confident promise of same-day delivery would go beyond the evidence.

Keep this question in mind as we build a prompt.

## Lesson

### 1. Start by saying what the model should do

Compare two requests:

~~~text
Help with this customer.
~~~

~~~text
Write a short reply to a customer asking whether Maple Books
offers same-day delivery.
~~~

The second request defines the task and audience. It gives the model a clearer direction.

However, the shop's delivery information is still missing. A clear task is only one part of a useful prompt.

### 2. Add the information the answer should use

Now supply the known fact:

~~~text
Write a short reply to a customer asking whether Maple Books
offers same-day delivery.

Shop information:
Delivery within Riverton takes three working days.
~~~

This gives the model evidence about normal delivery. It still helps to explain how the evidence should be used.

Without that instruction, a model may add general advice or assumptions that you did not want.

### 3. State the boundary

Add a clear rule:

~~~text
Use only the shop information provided.
If that information does not answer the question, say what is missing.
Do not invent a service or policy.
~~~

You are defining a useful response to uncertainty.

This improves the specification. It does not guarantee that every model will obey it every time, so inspect the actual response.

A prompt is a way to guide behavior. Application controls and further evaluation matter when you build a real product.

### 4. Ask for a format suited to the task

For a customer reply, you might add:

~~~text
Use friendly, everyday language.
Write no more than two sentences.
~~~

For a comparison, a table might be more useful. For a summary, three bullets might work well.

Choose a format because it helps the reader or application. A complicated format does not automatically improve the factual answer.

You do not need a data format such as JSON for today's exercise.

### 5. Put the parts together

A useful beginner prompt often contains four parts:

| Part | What it does | Example |
|---|---|---|
| Task | Says what to do | Reply to a customer's question. |
| Information | Supplies relevant facts | Delivery takes three working days within Riverton. |
| Boundaries | States what to avoid or how to handle limits | Do not invent a service. |
| Format | Describes the useful form of the response | Friendly language, at most two sentences. |

This is a starting checklist, not a formula that guarantees a correct result.

Sometimes a short prompt is sufficient. Add detail when it resolves a real ambiguity.

### 6. Examples can clarify what you mean

Suppose you want the assistant to handle missing information consistently. You can include a demonstration:

~~~text
Example:
Customer: Do students get a discount?
Reply: The supplied information does not describe student discounts.
~~~

An instruction without demonstrations is often called **zero-shot prompting**. A prompt containing a small number of demonstrations is called **few-shot prompting**.

Those names are optional vocabulary today. The practical idea is simple: sometimes showing an example makes the desired behavior clearer.

Use examples that actually follow your rules. A flawed demonstration can encourage the wrong behavior.

### 7. Improve a prompt using the response

After a reply appears, ask:

- Is it correct according to the supplied facts?
- Does it answer the customer's actual question?
- Did it add an unsupported detail?
- Is its length and language appropriate?

Then change the part of the prompt connected to the problem.

If the assistant invents services, clarify the evidence boundary. If it writes a long essay, adjust the requested format. If the facts are missing, supply them.

Repeatedly adding “be accurate” gives little guidance about the specific problem.

### 8. Keep some questions for a later check

If you improve a prompt by looking at three questions, you can gradually tailor it to those questions.

Keep a few other questions aside. Once you are happy with the prompt, try those as a fresh check.

For now, you only need the habit: use some examples to improve the prompt and some different examples to see whether the improvement carries over.

You will study formal dataset splits later.

## Walkthrough: from vague request to useful instruction

Here is a complete prompt you can read or try:

~~~text
Task:
Write a reply to a Maple Books customer.

Shop information:
- Open Monday to Saturday, 10 a.m. to 6 p.m.
- Closed on Sunday.
- Undamaged books can be returned within 14 days of purchase.
- A receipt is required for a return.
- Delivery within Riverton takes three working days.

Rules:
Use only the shop information.
If it does not answer the question, explain that limit.
Do not invent a policy, service, or exception.

Style:
Use friendly, everyday language and at most two sentences.

Customer question:
Do you offer same-day delivery?
~~~

An appropriate illustrative reply is:

> Our stated delivery time within Riverton is three working days. The information provided does not say whether same-day delivery is available.

Notice what the reply does:

1. Gives the relevant known information.
2. Identifies what is not known.
3. Avoids promising a service.
4. Fits the requested format.

A reply saying “Same-day delivery is available for an extra fee” would fail the evidence requirement. A reply saying “Same-day delivery is definitely unavailable” would also claim more than the supplied facts establish.

These are authored teaching examples, not a record of a live model run.

## Try it yourself

Use the complete prompt above and replace only the customer question.

Try:

1. “What time do you close on Saturday?”
2. “Can I return an undamaged book after seven days if I have the receipt?”
3. “How much does express delivery cost?”

Before using a tool, write what a suitable answer should include. If you use an AI chat tool, save what it actually says.

Then change just the style instruction to “Use one sentence.” Examine whether the facts and limits remain intact. Shorter is useful only if it still answers adequately.

Without an AI tool, compare two replies you write yourself and explain which follows the prompt better.

## Assignment

Create a page titled **My first prompt experiment**.

Include:

1. A simple starting prompt.
2. The known shop facts.
3. Three questions for improving the prompt.
4. What you observed in the replies.
5. One revised prompt and the reason for the change.
6. Two different questions for a fresh check.

You can reuse the walkthrough prompt as a starting point, but describe the change in your own words.

Keep the observations honest. If you only worked through supplied examples, say so. If you used a live tool, record which tool and when.

You do not need a score, a spreadsheet, or Python to complete this assignment.

## Knowledge check

1. Why is supplying the shop facts useful?
2. Does saying “act as an expert” give a model reliable knowledge of the shop's private policies?
3. What should a reply say about express-delivery prices?
4. Why keep two questions separate from the examples used to revise the prompt?
5. Is a shorter response automatically better?

<details>
<summary>Read the answers and explanations</summary>

1. It gives the model relevant evidence for answering.
2. No. A role instruction can influence style or behavior; it does not supply missing facts.
3. The provided information does not specify express delivery or its price.
4. Fresh questions help reveal whether an improvement applies beyond the examples you repeatedly inspected.
5. No. A response must remain correct and sufficiently complete for the question.

For the practice questions: Saturday closing time is 6 p.m. The seven-day return with an undamaged book and receipt fits the stated policy. Express-delivery cost is not specified.

</details>

## What you learned

You can now write a purposeful prompt, give it relevant information, define a useful boundary, and review the response.

At this stage, success means explaining why your prompt is clearer and showing what happened on a few examples. You do not need to learn every prompting technique or framework.

## Keep learning

Review your first three assignments. When the ideas feel familiar, continue to [Module 04: making a small question collection](04-datasets-and-oracles.md).

Microsoft's [Prompt Engineering Fundamentals](https://github.com/microsoft/generative-ai-for-beginners/blob/main/04-prompt-engineering-fundamentals/README.md) provides further practice. Its progression through explanations, examples, assignment, and knowledge check inspired this lesson's organization. The prompt, shop facts, exercises, and answer explanations here are original.

The earlier Python comparison is preserved as an [optional technical note](../advanced/03-prompting-and-development.md). It is not required for this assignment. See [attributions](../ATTRIBUTIONS.md).

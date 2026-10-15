# Module 04 — Make a small set of questions to learn from

[Previous: writing useful prompts](03-prompting-and-development.md) · [Course home](../README.md) · [Next: checking answers](05-evaluation-harnesses.md)

**Before you begin:** complete the prompt activity in Module 03. A notebook or simple table is enough.

## Introduction

You have written instructions for the Maple Books assistant. You have also tried a few questions.

How do you avoid changing the prompt based only on the last answer you happened to see?

Keep a small, organized collection of questions. Decide what a good answer should contain before looking at the assistant's reply. You can then return to the same questions when you make a change.

This lesson introduces a **dataset**: a collection of examples kept for a particular purpose. You do not need hundreds of examples to understand the process.

## Learning objectives

By the end, you should be able to:

1. Choose questions that cover different situations.
2. Describe what a suitable answer should say without insisting on one exact sentence.
3. Keep the question, expected behavior, and actual answer separate.
4. Set aside a few fresh questions for a later check.

## Scenario: customers ask more than opening hours

Maple Books has these facts:

> - Open Monday to Saturday, 10 a.m. to 6 p.m.
> - Closed on Sunday.
> - Undamaged books can be returned within 14 days of purchase.
> - A receipt is required.
> - Delivery within Riverton takes three working days.

If every question asks about Sunday opening, the assistant could appear successful while handling returns poorly.

We also want to see what happens when the information is missing or the customer has not supplied enough detail.

## Lesson

### 1. Begin with a purpose

For this small exercise, the purpose is:

> Find out whether the assistant answers shop-policy questions using the supplied information and explains what it cannot establish.

This purpose helps you decide which examples belong in the collection.

A request for a poem about books might be interesting, but it does not tell you much about policy answers. Keep the first collection focused.

### 2. Choose several kinds of question

Start with these situations:

| Situation | Example | What you want to learn |
|---|---|---|
| Direct lookup | “Are you open on Sunday?” | Can it find a simple fact? |
| Several conditions | “Can I return an undamaged book after ten days with a receipt?” | Does it apply the stated conditions? |
| Missing information | “What does express delivery cost?” | Does it invent a price? |
| Incomplete request | “Can I return my book?” | Does it explain conditions or ask for needed details? |

You may later hear people call these groups **slices**. It just means looking at a particular kind of example separately.

Do not worry about that terminology now. The useful idea is to avoid asking the same easy question repeatedly.

### 3. Write the expected behavior before collecting the reply

For the return question, you could record:

> Say that the stated policy permits the return because the book is undamaged, ten days is within the window, and the customer has the receipt.

That is more useful than keeping one sentence the assistant must reproduce exactly.

These two answers can both be acceptable:

> “Yes, those details meet the stated return conditions.”

> “An undamaged book with a receipt can be returned within 14 days, so ten days fits the policy.”

The expected meaning is the same.

### 4. Include questions whose answer is unavailable

A missing-information question is not a defective example.

If you ask about express-delivery prices, the appropriate behavior is to say that the supplied information does not state them.

Write that expectation explicitly. Otherwise, you may accidentally reward an invented answer because it appears complete.

Also distinguish “not stated” from “definitely unavailable.” Our information does not prove that express delivery exists or that it cannot exist.

### 5. Record enough detail to understand a result

A useful first table contains:

- A short identifier, such as Q01.
- The question.
- The relevant shop facts.
- What an acceptable reply should include.
- The actual reply, once collected.
- Your observation.

An identifier helps you refer to the same example later even if you reorder the table.

Keep actual replies unchanged. If you edit a poor reply to make it clearer, you lose the evidence of what happened.

### 6. Mark ambiguity rather than hiding it

Suppose someone asks:

> “Will my order arrive by Wednesday?”

We do not know when the order was placed. The phrase “working days” is also not defined further in our facts.

Do not write a precise arrival date as the expected answer. A suitable reply should explain the general delivery time and ask for the missing details.

If the policy itself is ambiguous, record the question that needs clarification from the shop. Do not make the assistant responsible for satisfying a rule nobody has defined.

### 7. Keep some questions fresh

Use one group of examples while improving the prompt. Keep another small group aside until you are ready to check the revised version.

The first group is often called a **development set**. The reserved group is a **held-out set**.

You can begin with four practice questions and two reserved questions. Those numbers are teaching choices, not evidence that an application is reliable.

If you inspect a reserved question and use it to revise the prompt, it is no longer a fresh check. Record that and reserve a different example for a later assessment.

## Walkthrough: a six-question collection

Here is a complete starting collection. Cover the expected-behavior column if you want to try writing it yourself.

| ID | Question | Expected behavior |
|---|---|---|
| Q01 | Are you open on Sunday? | Say the shop is closed. |
| Q02 | Can I return an undamaged book after ten days with a receipt? | Say it fits the stated return conditions. |
| Q03 | What does express delivery cost? | Say that express delivery and its price are not described. |
| Q04 | Can I return my book? | Explain the three conditions or ask for the missing details. |
| Q05 | What time do you close on Saturday? | Say 6 p.m. |
| Q06 | Do you accept credit cards? | Say accepted payment methods are not specified. |

You could use Q01–Q04 while revising the prompt and reserve Q05–Q06 for a later check.

For this lesson, all six are visible so you can understand the example. If you actually practice against all six, do not describe the last two as independently held out afterward.

The value comes from the process: clear questions, clear expectations, and an honest record.

## Try it yourself

Add three new questions:

1. A different wording of a known question.
2. A question requiring two return conditions.
3. A question the information cannot answer.

For each, write the expected meaning and one claim the assistant must not invent.

For example, “Could I visit this Sunday?” asks about the same fact as Q01. It adds wording variety, but it is not a completely different kind of task.

## Assignment

Create a collection of six to ten questions for your assistant idea.

Identify a few questions you will use for improvement and a few you will reserve for a later check. Include at least one missing-information question and one incomplete request.

Write a short note explaining where the facts came from. Our Maple Books facts are fictional, written for these lessons. If you choose another topic, use information you are allowed to share.

## Knowledge check

1. Why is a collection of only Sunday-opening questions limited?
2. Must an acceptable answer match your preferred wording?
3. Is “the information does not specify a price” an acceptable outcome?
4. What changes when you use a reserved question to improve the prompt?
5. What should you do when the reference policy is unclear?

<details>
<summary>Read the answers and explanations</summary>

1. It covers only a narrow situation and tells you little about returns or missing information.
2. No. Judge whether it expresses the required meaning and respects the facts.
3. Yes, when the information really does not contain the price.
4. That question becomes part of the evidence used during development. It is no longer an independent fresh check.
5. Record the ambiguity and seek clarification rather than inventing a hidden rule.

Possible new examples include asking for Friday opening hours, returning an undamaged book after seven days without stating whether a receipt is available, and asking about gift wrapping.

</details>

## What you learned

You have moved from trying isolated questions to keeping a small, understandable collection. That collection makes later changes easier to assess.

Continue when you can explain why each question is included and what its answer should establish.

## Keep learning

Continue to [Module 05: checking answers consistently](05-evaluation-harnesses.md).

The [optional technical note](../advanced/04-datasets-and-oracles.md) covers larger datasets, labels, and record formats when you are ready. Dataset features in [Phoenix](https://github.com/Arize-ai/phoenix) are further reading, not a setup requirement.

The teaching organization follows the approach described in [ATTRIBUTIONS.md](../ATTRIBUTIONS.md). This collection and its examples are original.

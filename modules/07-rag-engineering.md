# Module 07 — Help an assistant answer from documents

[Previous: reviewing answers](06-judges-and-human-review.md) · [Course home](../README.md) · [Next: comparing versions](08-rag-evaluation-and-statistics.md)

**Before you begin:** understand why an answer needs supporting information. No search software or database is required for this lesson.

## Introduction

So far, you have supplied all the Maple Books facts in each prompt.

That works for five facts. What happens when a business has many documents?

One useful approach is to find relevant information first, then give that information to the model with the question.

You will walk through that process manually before learning about the tools that automate it.

## Learning objectives

By the end, you should be able to:

1. Find a passage relevant to a question.
2. Give a model enough supporting information to answer.
3. Check whether a cited source actually supports a claim.
4. Identify whether a poor answer started with poor source selection.

## Scenario: the shop has several documents

Imagine the shop now keeps three short, approved documents:

> **Document H — Current opening hours**
>
> Maple Books opens Monday to Saturday from 10 a.m. to 6 p.m.
> The shop is closed on Sunday.

> **Document R — Current returns policy**
>
> Undamaged books can be returned within 14 days of purchase.
> A receipt is required.

> **Document D — Current delivery information**
>
> Delivery within Riverton takes three working days.
> This document does not describe express-delivery services or prices.

These are the same fictional facts used earlier, organized into separate documents. The last sentence makes the limits of Document D explicit; it does not establish that express delivery is unavailable.

The customer asks:

> Can I return an undamaged book after ten days with a receipt?

## Lesson

### 1. Find the information before writing the answer

Document R is the relevant source. Document H tells you nothing about returns. Document D concerns delivery.

Choosing a relevant source is called **retrieval**.

For a tiny collection, a person can choose the source. For a larger collection, an application may use search.

The goal is not to send the model a random document containing the word “book.” It is to provide the information needed for this particular question.

### 2. Send the question and evidence together

Once you find Document R, the request can say:

~~~text
Use the source below to answer the customer.
If the source does not answer the question, explain that limit.

Source R:
Undamaged books can be returned within 14 days of purchase.
A receipt is required.

Customer:
Can I return an undamaged book after ten days with a receipt?
~~~

The model now has a clear question and relevant evidence.

An appropriate answer is:

> Yes. Those details meet the stated return conditions: the book is undamaged, ten days is within the 14-day window, and you have the receipt. Source: R.

This is an illustrative answer, not a recorded model result.

### 3. Learn the name after understanding the process

You may hear this approach called **retrieval-augmented generation**, or **RAG**.

It combines finding information with generating a response:

~~~text
Question → find relevant information → give it to the model → answer
~~~

The name is less important than the sequence.

RAG does not guarantee a correct answer. Search can select the wrong source, and the model can misuse a correct source. Both steps need checking.

### 4. Keep enough surrounding information

Suppose you cut Document R down to:

> “within 14 days”

That fragment loses the condition of the book and the receipt requirement.

Search systems often divide documents into pieces. You will hear those pieces called **chunks**. A useful piece preserves enough meaning for the task.

For now, choose complete short passages. Later, you can study how software divides and searches larger documents.

### 5. A citation is a pointer, not proof

A **citation** identifies the source associated with an answer.

An answer might say:

> You can return any book within 30 days. Source: R.

Document R exists, but it does not support that claim. The citation looks legitimate while the meaning is wrong.

To check a citation, read the source and compare it with the claim. Ask both:

- Is this the source the application actually used?
- Does its content support what the answer says?

### 6. Use current, appropriate sources

Imagine an archived draft says the shop closes at 7 p.m. The approved current opening-hours document says 6 p.m.

The application needs a rule about which source is authoritative. Simply finding a sentence about closing time is insufficient.

For this exercise, Documents H, R, and D are explicitly the approved sources. The archived draft is not.

In a real application, someone must establish that source status. A filename or recent edit date alone may not establish authority.

### 7. Keep information access separate from relevance

A document might be relevant but not appropriate for the current user.

For example, an internal personnel note should not become part of a public customer answer just because it mentions the shop.

The application should choose from information the user is permitted to access. Do not rely only on an instruction asking the model to hide information it should never have received.

We will explore actions and permissions more in Modules 09–10.

### 8. Inspect two different failure points

If a return question receives Document H, the source-selection step failed.

If the model receives Document R but answers “30 days,” the needed evidence was present and the answer-generation step failed.

That distinction helps you decide what to improve. Rewriting the answer instructions may not solve a search process that never finds the returns policy.

## Walkthrough: trace two bad answers

**Question:** “Can I return an undamaged book after ten days with a receipt?”

| Run | Source supplied | Illustrative answer | What happened? |
|---|---|---|---|
| A | Document H | “The shop opens at 10 a.m.” | Wrong source selected and question not answered. |
| B | Document R | “Yes, returns are allowed within 30 days.” | Relevant source supplied, but the answer changed its meaning. |

For A, investigate how the application chose documents.

For B, inspect the instructions and generation behavior. Preserve the actual prompt and answer if this occurs in a live run.

Now consider:

> “What does express delivery cost?”

Document D does not contain a price. Selecting D does not make a price available. The correct behavior is to explain the missing information.

## Try it yourself

For each question, choose a source and write the answer it supports:

1. “What time do you close on Friday?”
2. “Do I need a receipt for a return?”
3. “How long does delivery within Riverton take?”
4. “What does overseas delivery cost?”

For the last question, say what the sources do and do not establish. Do not invent an overseas service or assert it is impossible.

## Assignment

Create three short documents for your assistant idea. Give each a name and say which version is current for your exercise.

Write five questions. For each question, record:

- The document or passage you would select.
- Why it is relevant.
- The answer it supports.
- Any information still missing.

Optionally paste a selected source and question into an AI chat tool. Compare the actual response with the evidence.

Doing the selection manually teaches the process. It does not mean you have built an automated RAG application yet.

## Knowledge check

1. What does retrieval do?
2. Does a real source identifier make an answer correct?
3. Why can a very short fragment lose important meaning?
4. What should you inspect if the wrong document was supplied?
5. Does RAG eliminate unsupported answers?

<details>
<summary>Read the answers and explanations</summary>

1. It finds candidate information for the question, within relevant constraints.
2. No. The source must support the associated claim.
3. It may omit conditions, exceptions, or the topic to which a rule applies.
4. The source-selection process before focusing only on wording.
5. No. Retrieval and generation can both fail.

For the practice questions: H supports Friday closing at 6 p.m.; R states the receipt requirement; D gives three working days within Riverton. No source gives an overseas-delivery price.

</details>

## What you learned

You understand how an assistant can use documents without assuming the model already knows the business.

Continue when you can trace a question to its source and explain whether the answer uses that source correctly.

## Keep learning

Continue to [Module 08: comparing versions fairly](08-rag-evaluation-and-statistics.md).

The [optional technical note](../advanced/07-rag-engineering.md) explains search implementations and document preparation. RAG examples in [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) are later coding resources.

The documents, walkthrough, and activities here are original; see [attributions](../ATTRIBUTIONS.md).

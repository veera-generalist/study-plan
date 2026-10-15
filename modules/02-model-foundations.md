# Module 02 — Understanding and comparing language models

[Previous: getting started](01-python-engineering.md) · [Course home](../README.md) · [Next: writing useful prompts](03-prompting-and-development.md)

**Before you begin:** read Module 01. You do not need Python, mathematics, or a second AI subscription.

## Introduction

In the first lesson, you planned an assistant for Maple Books. It answers questions using a small set of shop facts.

Now you face two practical questions:

- Why might an assistant produce a wrong answer even when it writes clearly?
- How would you decide which model is suitable for your application?

This lesson gives you a practical explanation of language models so their behavior becomes easier to understand.

## Learning objectives

By the end, you should be able to:

1. Describe, in simple terms, how a language model produces text.
2. Explain why supplying relevant information matters.
3. Recognize that different answers can express the same correct meaning.
4. Compare two sets of responses using the same tasks.

## Scenario: choosing help for Maple Books

The shop information is unchanged:

> - Open Monday to Saturday, 10 a.m. to 6 p.m.
> - Closed on Sunday.
> - Undamaged books can be returned within 14 days of purchase.
> - A receipt is required for a return.
> - Delivery within Riverton takes three working days.

You want an assistant that can explain these facts clearly and handle questions the information does not answer.

A model that writes an impressive poem might be useful for creative work. That alone does not establish whether it follows a shop policy. Your choice should reflect the task you are building.

## Lesson

### 1. A model learns patterns during training

**Training** is the process through which a model's behavior is learned from examples.

For language models, those examples can help the model learn relationships among words, ideas, instructions, and kinds of writing. The exact training process differs across models.

You can then use a trained model for many requests: explain a paragraph, summarize a policy, draft a message, or propose a plan.

Calling the model to produce a response is called **inference**. For now, remember:

- Training is how the model's learned behavior is developed.
- Inference is using the trained model.

You can build many applications using an existing model. Training your own model is not a prerequisite for getting started.

### 2. Text is processed in smaller units

A model processes content using units called **tokens**.

A token can be a word, part of a word, punctuation, or another unit. Do not assume one token always equals one word.

As text is generated, the model produces successive units using what it learned and the information available in the request. Those units form the response you read.

This process can produce coherent explanations and useful reasoning. It does not automatically verify every statement against an authoritative source.

That is why a response can sound convincing while giving the wrong Sunday opening hours.

You do not need to count tokens for today's exercise. Knowing that models have an input/output budget will become useful when you build applications.

### 3. The available information affects the answer

The instructions, messages, and documents available for a request are often called its **context**.

If you ask:

~~~text
What is the return policy at Maple Books?
~~~

without supplying the shop facts, the model may not have reliable information about our fictional business. It might produce something resembling a common retail policy.

Now provide the actual policy:

~~~text
Maple Books accepts returns of undamaged books within 14 days
of purchase. A receipt is required.

Question: What is the return policy?
~~~

You have given the model relevant evidence. That creates a better basis for answering, although you still need to check the response.

Supplying a policy in a conversation is different from training the model on a new dataset. The policy is available for that interaction; you should not assume it has become permanent knowledge.

### 4. A model can have too much information to handle at once

A model has a limit on the content it can work with for a request. You will see this called the **context window**.

In an application, instructions, conversation history, documents, and the generated response can all affect the available budget, depending on the interface.

For our five shop facts, this is not a practical problem. Later, if you supply hundreds of pages or a very long conversation, you will need to decide what information is relevant.

A larger context window does not guarantee that every supplied detail will be used correctly. You still check whether the answer follows the needed evidence.

### 5. Different wording can be equally correct

Consider these replies to “When do you close on Friday?”

> A: “We close at 6 p.m. on Friday.”

> B: “Friday opening hours are 10 a.m. to 6 p.m.”

Both answer the question correctly.

Now consider:

> C: “We close at 7 p.m. on Friday.”

C changes the meaning. That is a different kind of difference.

When comparing responses, pay attention to what they say, not whether their wording exactly matches a preferred sentence.

Generation can also vary between repeated requests. Some variation is harmless; a changing factual claim needs investigation.

### 6. Models and applications are different comparison targets

An AI chat application may combine a model with its own instructions, search, stored conversation, and other features.

If two chat tools give different answers, the cause may be more than the underlying models. One might search the web, while another uses only your message.

You can still compare their usefulness for a task. Just describe the comparison accurately: “I compared these two applications under these conditions.”

For a controlled model comparison later, you will record which models were used, the supplied information, and the settings. You do not need to learn all those settings now.

### 7. What makes a model suitable?

Start with a few practical questions:

| Question | Why it matters for the bookshop |
|---|---|
| Does it answer accurately? | Wrong policies can mislead customers. |
| Does it follow instructions? | It should use the supplied information and requested format. |
| Does it handle missing information appropriately? | It should not invent a discount or delivery promise. |
| Is it clear to read? | A customer should understand the answer. |
| Is it fast enough? | Waiting a long time can make a simple assistant frustrating. |
| Is its operating cost acceptable? | A useful application must be affordable to run. |

There is no need to rank every available model today. Begin with task quality. Cost, speed, and deployment choices become more concrete after you have a working example.

## Walkthrough: compare two fictional candidates

The replies below are invented teaching examples. They are not recorded model results.

Both candidates receive the same five shop facts.

| Question | Candidate A | Candidate B |
|---|---|---|
| Are you open on Sunday? | “No, the shop is closed on Sunday.” | “Yes, from 11 a.m.” |
| Can I return an undamaged book after ten days if I have the receipt? | “Yes, it is within the 14-day return period.” | “Yes, within the 14-day period and with your receipt.” |
| Do you offer express delivery? | “The information does not describe express delivery.” | “Yes, next-day express delivery is available.” |

How should you read this?

Both candidates handle the return question. A follows the supplied information on Sunday opening and avoids inventing an express service. B makes two unsupported or incorrect claims.

For these particular examples, A gives the more suitable responses.

This does not prove that A would be better on every future question. It is a small, understandable beginning to a comparison.

## Try it yourself

Write an acceptable answer for each question:

1. “What time can I visit on Saturday?”
2. “Can I return a damaged book after five days?”
3. “Which payment cards do you accept?”

For each answer, underline the shop fact that supports it. If no fact answers the question, write that down.

The second question needs care: the stated return policy covers undamaged books. It does not establish what exception, if any, applies to damaged books.

If you have access to one AI chat tool, supply the facts and try the three questions. A second tool is optional. You can learn from comparing your own expected answers with one tool's replies.

## Assignment

Make a small comparison sheet:

| Question | Your expected answer or limit | Actual or supplied reply | Your observation |
|---|---|---|---|
| | | | |

Use three questions. Record whether you reviewed a live response or one of the lesson's invented examples.

Write a short conclusion:

> For these questions, the assistant handled ___ well. It needs improvement on ___. I would investigate ___ next.

Avoid a general conclusion such as “This model is always accurate.” Your conclusion should fit the evidence you actually collected.

## Knowledge check

1. Do you need to train a model before using it in an application?
2. Is every token a complete word?
3. What does adding the shop policy to the request change?
4. Should two differently worded but correct answers receive the same judgment about factual correctness?
5. Does a three-question comparison establish which model is best for every task?

<details>
<summary>Read the answers and explanations</summary>

1. No. You can use an already trained model.
2. No. Tokens may be parts of words or other units.
3. It makes that policy available as context for the request. It does not guarantee correct use or permanent learning.
4. Yes, if both satisfy the factual requirement. You could assess style separately.
5. No. It provides evidence about those questions under those conditions.

For the practice questions: Saturday hours are 10 a.m. to 6 p.m. The stated return policy only covers undamaged books, so do not invent a damaged-book exception or reject every possible exception as established fact. Accepted payment cards are not specified.

</details>

## What you learned

You can now connect a model's behavior with its training, the information supplied for a request, and the task it is asked to perform.

You are ready for the next lesson when you can compare two replies by meaning and explain why an impressive-sounding answer may still be unsuitable.

## Keep learning

Continue to [Module 03: writing useful prompts](03-prompting-and-development.md).

Microsoft's [Exploring and comparing different LLMs](https://github.com/microsoft/generative-ai-for-beginners/blob/main/02-exploring-and-comparing-different-llms/README.md) offers a broader treatment. Its learning-objectives and scenario-led organization informed this lesson; the worked examples here are original.

The previous mathematical and classifier material is preserved as an [optional technical note](../advanced/02-model-foundations.md). You do not need it to complete this lesson. See [source credits](../ATTRIBUTIONS.md).

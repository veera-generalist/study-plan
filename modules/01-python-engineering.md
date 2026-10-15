# Module 01 — Getting started with generative AI

[Course home](../README.md) · [Next: understanding language models](02-model-foundations.md)

**You need:** curiosity and a place to write notes. No Python, mathematics, model downloads, or paid account is required for this lesson.

## Introduction

Imagine a small bookshop that receives the same questions every day: “Are you open on Sunday?”, “Can I return a book?”, and “How long does delivery take?”

You want to build an assistant that can answer those questions in everyday language. You also want to know when its answers deserve your trust.

That small idea introduces the two areas you want to learn:

- **AI engineering:** building an application that uses AI to help someone do something.
- **AI evaluation:** checking how well that application performs the job you intended.

You will explore both through one simple example. There is no need to build the application yet. First, understand what you are asking it to do.

## Learning objectives

By the end, you should be able to:

1. Explain generative AI in your own words.
2. Tell the difference between a model and an application.
3. Recognize a useful answer and an unsupported answer.
4. Describe one small AI application you would like to build.

## Scenario: Maple Books

Maple Books is a fictional shop. We will use these approved facts throughout the twelve lessons:

> **Maple Books information**
>
> - The shop is open Monday to Saturday, from 10 a.m. to 6 p.m.
> - The shop is closed on Sunday.
> - Customers can return an undamaged book within 14 days of purchase.
> - A receipt is required for a return.
> - Delivery within Riverton takes three working days.

This is all the information available for the exercises. There is no information about discounts, overseas delivery, stock availability, or payment methods.

Why keep the information this small? You can check every answer yourself. You can concentrate on learning the ideas without also researching a business.

## Lesson

### 1. What does “generative AI” mean?

Generative AI creates content in response to a request. Depending on the system, that content could be text, an image, audio, or code.

For example, you could ask it to:

- Turn a paragraph into a shorter explanation.
- Draft a friendly reply to a customer.
- Suggest titles for a story.
- Explain a piece of code.

The word **generative** refers to producing content. It does not mean the content is automatically original, accurate, or appropriate.

Our bookshop assistant will generate text. It will turn a customer's question and the shop's information into an answer.

### 2. What is a model?

A **model** is the learned system that processes an input and produces an output.

You do not write a separate reply for every possible question. A language model has learned patterns from large amounts of language data and can produce responses to different requests.

A **large language model**, usually shortened to **LLM**, is a kind of model used for many language tasks.

For this lesson, remember the practical meaning: it is the part of the system that generates the words. You do not need to understand its internal mathematics yet.

### 3. What is a prompt?

A **prompt** is the request and information you provide to guide a model.

For our example:

~~~text
Use the Maple Books information below to answer this question:
Are you open on Sunday?

Information: Maple Books is closed on Sunday.
~~~

The question gives the task. The supplied information gives the model something to use when answering.

An appropriate answer would be:

> No. Maple Books is closed on Sunday.

This is an illustrative answer written for the lesson. It is not a recorded response from a live model.

### 4. What is an AI application?

The model is one part of an application.

A simple version of our application could work like this:

~~~text
Customer asks a question
        ↓
Application supplies the shop information
        ↓
Model produces a draft answer
        ↓
Application shows the answer to the customer
~~~

The application decides which information to send, how to present the reply, and what should happen when something goes wrong.

An AI engineer makes those choices and implements them. Using a capable model does not remove the need to design the surrounding software.

Notice that the bookshop information is supplied by the application. We are not assuming the model already knows the shop's current policies.

### 5. What does evaluation mean?

Evaluation means checking behavior against a clear purpose.

For our assistant, useful questions include:

- Did it answer the customer's question?
- Did it use the shop information correctly?
- Did it add anything the information does not support?
- Was the reply understandable?

You can begin this work by reading answers yourself. Automated scoring comes later.

Consider this reply:

> Yes, we are open on Sunday from 11 a.m. to 4 p.m.

It is easy to read. It also contradicts the supplied information. Good writing and a correct answer are different things.

### 6. What should happen when information is missing?

A customer asks:

> Do you deliver outside Riverton?

The provided information describes delivery within Riverton. It does not answer the question about other places.

An appropriate reply is:

> The information provided only describes delivery within Riverton. It does not say whether delivery is available elsewhere.

This answer is useful because it makes the limit clear. An invented overseas-delivery promise could create a real problem for the shop.

You will sometimes see the term **hallucination** for generated content that is unsupported or incorrect. The important habit now is to ask, “What information supports this statement?”

### 7. Where do ordinary software rules still help?

Some parts of a product are straightforward rules. Software can check whether a date is Sunday or whether an order number exists.

A language model is useful for handling varied wording or drafting explanations. For instance, “Do you open on Sundays?” and “Can I visit this Sunday?” use different words to ask a similar question.

An application can combine ordinary rules, stored information, and language generation. You do not have to make every part of a product an AI task.

## Walkthrough: check three answers

The customer asks:

> I bought a book ten days ago. Can I return it?

Read the replies below before looking at the explanation.

| Reply | What the assistant says |
|---|---|
| A | “Yes, any book can be returned within 30 days.” |
| B | “A return is allowed within 14 days if the book is undamaged and you have the receipt.” |
| C | “Yes, and you will receive a cash refund immediately.” |

**Explanation:** B accurately states the conditions in the supplied policy. Ten days is within the return window, but the condition of the book and receipt still matter.

A invents a 30-day period. C skips the conditions and invents details about the refund method and timing.

You have just completed a small evaluation: one question, three possible replies, and a reasoned judgment.

## Try it yourself

Spend about ten minutes on these questions:

1. A customer asks, “What time do you close on Friday?” Write a suitable answer.
2. A customer asks, “Do students receive a discount?” Write a suitable answer.
3. Explain why the second question should be handled differently from the first.

You can do this in a notebook without using an AI tool.

If you already have access to an AI chat tool, optionally provide the shop information and ask the same questions. Record the actual replies. Compare them with your own answers rather than assuming they will match this lesson.

## Assignment

Create a short note called **My first AI assistant** containing:

- Who the assistant helps.
- Three questions it should answer.
- The information it needs.
- One thing it should say when it lacks that information.
- How you would decide whether a reply is useful.

You can continue with Maple Books or choose another small idea, such as a hobby-club assistant or a personal study helper. Keep the task small enough that you can check its answers.

There is no coding requirement for this assignment.

## Knowledge check

Try answering before opening the explanation.

1. Is the model the same thing as the complete bookshop application?
2. Does a natural-sounding reply establish that its facts are correct?
3. What should the assistant do when asked about a student discount?
4. What is one responsibility of an AI engineer, and one responsibility of an evaluator?

<details>
<summary>Read the answers and explanations</summary>

1. No. The application also supplies information, handles the conversation, and presents or checks the result.
2. No. Compare factual claims with supporting information.
3. State that the supplied information does not describe a student discount.
4. An engineer might decide how the application supplies shop information. An evaluator might check whether answers follow that information. One person can do both kinds of work.

For the practice questions: Friday closing time is 6 p.m. Student discounts are not specified.

</details>

## What you learned

You now have a small, concrete picture of AI engineering and evaluation: build an assistant for a defined purpose, give it suitable information, and check what it says.

You are ready to continue when you can explain the model, the application, and the evaluation without memorizing their definitions.

## Keep learning

Continue to [Module 02: understanding language models](02-model-foundations.md).

For another explanation, read Microsoft's [Introduction to Generative AI and Large Language Models](https://github.com/microsoft/generative-ai-for-beginners/blob/main/01-introduction-to-genai/README.md). Its scenario-based lesson format informed this rewrite. Our bookshop scenario, explanations, exercises, and answers are original.

The earlier Python material is preserved as an [optional technical note](../advanced/01-python-engineering.md). It is not required before Module 02. Source credits are in [ATTRIBUTIONS.md](../ATTRIBUTIONS.md).

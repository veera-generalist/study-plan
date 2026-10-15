# Module 05 — Check answers consistently

[Previous: collecting questions](04-datasets-and-oracles.md) · [Course home](../README.md) · [Next: getting help with review](06-judges-and-human-review.md)

**Before you begin:** bring a few questions and expected answers from Module 04. You can work on paper.

## Introduction

You ask the assistant a question, read its reply, and decide it “looks good.”

That is a starting impression. To compare answers fairly, you need to say what “good” means.

In this lesson, you will write a few simple checking rules and apply them to actual sentences. You will then summarize what you found without losing the important details.

## Learning objectives

By the end, you should be able to:

1. Turn “good answer” into clear questions you can check.
2. Distinguish a wrong answer from an unanswered or unclear measurement.
3. Summarize a small review using counts.
4. Explain why one total score cannot tell the whole story.

## Scenario: an answer can sound helpful and still be wrong

The customer asks:

> Can I return an undamaged book after ten days if I have the receipt?

The assistant replies:

> Absolutely! You have 30 days to return it, and we will refund your payment immediately.

The tone is friendly. The 30-day window contradicts the policy, and immediate payment is not specified.

A single impression of helpfulness could miss those problems. We need more specific checks.

## Lesson

### 1. Decide what you are checking

Start with three questions:

1. Does the reply answer the customer's question?
2. Are its factual claims supported by the shop information?
3. Does it include the conditions needed for that answer?

These are checking criteria. A written set of criteria is often called a **rubric**.

For a customer-facing reply, you can also check clarity. Keep that separate from factual correctness so pleasant wording does not hide a wrong claim.

### 2. Make the rules observable

“Be accurate” is too broad to explain a decision.

A more useful rule is:

> A return-policy answer must preserve the 14-day limit, the undamaged-book condition, and the receipt requirement when those conditions are relevant to the question.

This tells another reviewer what to look for.

You do not need every answer to repeat every shop fact. A question about Saturday closing time does not need a paragraph about returns.

Judge completeness in relation to the actual question.

### 3. Choose clear review outcomes

For each answer, record one of these:

| Outcome | Meaning |
|---|---|
| Meets the requirements | You checked the answer and the required conditions are satisfied. |
| Does not meet the requirements | You found a specific wrong, missing, or unsupported part. |
| Needs clarification or review | You cannot make a dependable judgment because the reference, question, or criterion is unclear. |

If the application never produced an answer because a request failed, record that separately. You did not observe a satisfactory customer reply.

If a review tool failed, record that separately too. A missing judgment is not evidence of a correct answer.

You do not need complicated software to keep those distinctions.

### 4. Separate exact checks from checks of meaning

Some things are straightforward to check:

- Did a reply exist?
- Did it exceed a requested length?
- Did it name an allowed category?

Other things require reading meaning:

- Does the answer preserve the return conditions?
- Does it imply a service the facts do not establish?
- Does it answer the actual question?

For example, checking whether “14” appears is not enough. “Returns are not allowed within 14 days” contains the number but changes the policy.

Later, software can automate exact checks and help with meaning-based review. First, understand what each check establishes.

### 5. Start with counts you can explain

Suppose you review six answers and four meet your requirements.

Write:

> Four of six answers met the requirements in this small exercise.

Then describe the other two. Were they wrong about Sunday opening? Did they invent a delivery service?

A percentage is simply another way to express the count. Four out of six is about 67%. It is not a statement that the assistant is 67% reliable for every future use.

The questions you selected and the way you reviewed them affect what the result means.

### 6. Look at different kinds of question

Imagine all four successful answers were simple opening-hours questions and both unsuccessful answers involved missing information.

The total count hides an important pattern.

Write the pattern down:

> The assistant handled direct opening-hours questions but invented details when information was absent.

That observation suggests a specific improvement. Adding more easy questions would raise the overall score without solving that weakness.

### 7. Keep the original answer and your reason

A useful review record includes:

- The question.
- The unchanged answer.
- The relevant facts.
- The outcome.
- A brief reason.

A reason such as “Invented a same-day service not described in the information” is more useful than “Bad answer.”

Someone else should be able to understand and challenge your decision.

## Walkthrough: review four replies

Use the original Maple Books facts.

| Question | Illustrative reply | Review |
|---|---|---|
| Are you open on Sunday? | “No, we are closed on Sunday.” | Meets the requirement. |
| What does express delivery cost? | “Express delivery costs five pounds.” | Does not meet the requirement; the service and price are not stated. |
| Can I return an undamaged book after ten days with a receipt? | “Yes, those details meet the 14-day return policy.” | Meets the requirement. |
| Which days count as working days for delivery? | “Saturday counts as a working day.” | The claim is not supported by the information. |

The last reply should not receive a pass just because Saturday opening is specified. Shop opening days do not establish the delivery company's working-day calendar.

A suitable answer would explain that delivery takes three working days and that the supplied information does not define which days count.

In these four authored examples, two meet the requirements. The exercise reveals a problem with invented details, not a complete estimate of real-model quality.

## Try it yourself

Review these replies:

1. Question: “When do you close on Friday?” Reply: “At 6 p.m.”
2. Question: “Do you gift-wrap purchases?” Reply: “Yes, every purchase is gift-wrapped free.”
3. Question: “Can I return my book?” Reply: “Returns are allowed within 14 days.”

Write an outcome and reason for each.

For the third reply, consider whether the missing condition and receipt requirement matter. A general question about eligibility needs more than the time limit alone.

## Optional: let Python count reviewed answers

The decisions still come from your review. This short program only counts them.

~~~python
results = ["meets", "does not meet", "meets", "does not meet"]

meets_count = results.count("meets")
total_count = len(results)

print("Answers meeting the requirements:", meets_count)
print("Answers reviewed:", total_count)
~~~

The first line stores four outcomes. The next lines count the successful outcomes and the total. The last two lines display 2 and 4.

This program does not read answers, determine truth, or call a model. It illustrates how a little code can help once you understand the job.

You can skip it and complete the lesson manually. A saved copy is in [the optional beginner example](../labs/beginner/05_count_answers.py).

## Assignment

Write three checking rules for your assistant. Review five replies using those rules.

Include at least one reply that sounds convincing but adds an unsupported claim. Save the replies and write one sentence explaining each outcome.

Summarize the counts and one recurring problem. If something is unclear, preserve the uncertainty rather than forcing a favorable score.

## Knowledge check

1. Why is friendly wording insufficient evidence of correctness?
2. Does finding “14” establish that a return answer is correct?
3. What should you record when the assistant request fails?
4. What does “four out of six” establish?
5. Can the optional Python example decide whether an answer is true?

<details>
<summary>Read the answers and explanations</summary>

1. An answer can be friendly while contradicting facts or inventing promises.
2. No. You need to read what the statement says about the 14-day period.
3. Record an application failure, not a successful reply or an invisible skipped case.
4. It summarizes those six reviewed outcomes under the stated rules. Broader claims need broader evidence.
5. No. It only counts outcomes already entered.

For the practice replies: the Friday answer meets the requirement; gift wrapping is invented; the general return answer omits the condition and receipt requirements.

</details>

## What you learned

You can now explain why an answer meets or misses a requirement and summarize the findings without hiding the individual problems.

Continue when another person could understand your review from the stored answer and your reason.

## Keep learning

Continue to [Module 06: getting help with review](06-judges-and-human-review.md).

The [optional technical note](../advanced/05-evaluation-harnesses.md) introduces evaluation programs and automation. [DeepEval](https://github.com/confident-ai/deepeval) and [Promptfoo](https://github.com/promptfoo/promptfoo) are later implementation resources.

The rubric, replies, and counting example here are original; see [attributions](../ATTRIBUTIONS.md).

# Module 08 — Compare two versions fairly

[Previous: answering from documents](07-rag-engineering.md) · [Course home](../README.md) · [Next: tools and actions](09-tools-and-agents.md)

**Before you begin:** know how to collect questions and review answers. You do not need statistical formulas.

## Introduction

You change the prompt. The assistant gives a better reply to the question you were working on.

Has the application improved?

Perhaps. It may also have become worse on a different question.

This lesson shows how to compare two versions using the same tasks and how to describe the result without claiming more than the evidence supports.

## Learning objectives

By the end, you should be able to:

1. Preserve an earlier version for comparison.
2. Compare versions on the same questions and rules.
3. Record improvements and regressions separately.
4. Explain why a small result is uncertain.
5. Choose a next step using quality, time, and cost.

## Scenario: a prompt change has mixed effects

You add a stronger instruction to the Maple Books prompt:

> When information is missing, say so rather than adding a plausible detail.

You want to know whether this helps with express-delivery and payment questions while keeping known answers correct.

Call the earlier prompt **A** and the revised prompt **B**. The earlier version is your **baseline**: the reference you compare the change against.

## Lesson

### 1. Save what you changed

Keep the actual text of both prompts, the shop facts, and the questions.

Write a short hypothesis:

> B should invent fewer details when the shop information does not answer a question.

A hypothesis says what improvement you expect and why.

If you change the model, the prompt, and the documents together, you can compare the overall packages. You will have less evidence about which individual change caused the difference.

For an early exercise, change one main thing at a time.

### 2. Use the same questions and review rules

If A receives easy opening-hours questions while B receives incomplete delivery questions, their scores are not a fair direct comparison.

Give both versions the same questions and available facts. Apply the same checking rules.

For live runs, record which tool or model you used and when. Conversation history or built-in search can affect results, so note those conditions too.

You do not need perfect experimental control to start learning, but you do need an honest description of what was compared.

### 3. Look at each pair of answers

For every question, ask:

- Did both versions meet the requirements?
- Did B fix an answer that A got wrong?
- Did B break an answer that A got right?
- Did both miss the requirement?

A deterioration after a change is called a **regression**.

Keeping the pairs visible helps you understand the result. A single total can hide a newly broken behavior.

### 4. Treat important failures seriously

Imagine B fixes two minor formatting issues but begins giving the wrong Sunday opening hours.

It might score better on a simple count while creating a more serious business problem.

Decide which requirements are mandatory before comparing. For our exercise, invented policy promises are important because customers may act on them.

This does not mean every small wording difference has the same consequence as a factual error.

### 5. Understand what a small sample can tell you

If B meets the requirements on five of six questions, you have a result for those six questions.

You do not yet know how it handles every possible question.

A small hand-picked collection is useful for learning and finding problems. It is not a precise estimate of real-world success.

Later, you can study larger samples and formal uncertainty calculations. For now, use careful wording:

> B improved these cases in this exercise, but I need more varied questions before making a broad claim.

### 6. Repeated runs answer another question

Try the same request again. A model may produce different wording.

If the meaning remains correct, that variation may be harmless. If one run invents a price and another admits the information is missing, you have a consistency problem to investigate.

Repeated attempts at one question do not replace trying different questions. They reveal different kinds of variation.

Record what you observed rather than keeping only the best reply.

### 7. Keep final checks separate from improvement

Use development questions to inspect failures and revise the prompt.

Once you select a candidate, keep it unchanged while trying your reserved fresh questions.

If you use those fresh results to make another change, record that the questions are now influencing development. Reserve new examples before making another claim of independent assessment.

This habit matters more at this stage than memorizing statistical names.

### 8. Include time and cost in the decision

A reply can be accurate but too slow for the intended use.

**Latency** means how long an operation takes. Decide whether you are timing a model call or the complete customer task.

**Cost** includes unsuccessful attempts and retries when you are estimating what it takes to complete a useful task.

For the first manual exercise, simply record any obvious wait or effort. You do not need to calculate precise production prices.

## Walkthrough: count improvements and losses

Use the six questions introduced in Module 04. The outcomes below are invented teaching data.

| Question | A meets requirements? | B meets requirements? | Change |
|---|---|---|---|
| Q01 — Sunday opening | Yes | No | B breaks a correct answer. |
| Q02 — Eligible return | Yes | Yes | Both meet the requirements. |
| Q03 — Express-delivery price | No | Yes | B fixes an invented-detail problem. |
| Q04 — Incomplete return question | No | Yes | B handles missing customer details better. |
| Q05 — Saturday closing | Yes | Yes | Both meet the requirements. |
| Q06 — Payment methods | Yes | Yes | Both correctly state the information is missing. |

A meets four of six requirements. B meets five of six.

B fixes two cases and breaks one. Its total is higher, but the new Sunday error still needs attention.

A reasonable conclusion is:

> B improved missing-information handling in this exercise, but I would revise or investigate the Sunday regression before choosing it for customer use.

Because all six outcomes are visible and discussed here, treat this table as practice data, not a hidden final assessment.

## Try it yourself

Write a different set of six paired outcomes in which A and B have the same total, but B fixes one question and breaks another.

Then answer:

1. Would the unchanged total tell the complete story?
2. What information would help you decide whether the change is useful?
3. Which examples would you inspect first?

You can do this without running any model.

## Assignment

Compare two prompt versions on a small development collection.

Keep the prompts, questions, replies, review rules, and paired outcomes. Write:

- What you changed.
- What improved.
- What regressed.
- What remains uncertain.
- Whether you would keep, revise, or reject the change.

Only after selecting the candidate should you try the reserved questions. Label supplied example data and live results accurately.

## Knowledge check

1. Why should both versions receive the same questions?
2. Can the version with the higher total still have an important new problem?
3. What does repeating one question reveal?
4. Can six successful examples prove the assistant always works?
5. What should happen if fresh-check results lead to another prompt change?

<details>
<summary>Read the answers and explanations</summary>

1. It makes the task-level comparison more meaningful.
2. Yes. Look at which behaviors changed and their consequences.
3. It can reveal variation on that request, but does not establish breadth across tasks.
4. No. The sample is limited.
5. Treat those questions as development evidence and reserve new independent checks for a later assessment.

For the activity, any equal-total example with at least one win and one loss demonstrates why the total alone is incomplete.

</details>

## What you learned

You can now compare changes using visible evidence rather than choosing whichever version produced the most impressive recent answer.

Continue when you can explain a win, a loss, and the limits of your comparison.

## Keep learning

Continue to [Module 09: giving an assistant a small action](09-tools-and-agents.md).

The [optional technical note](../advanced/08-rag-evaluation-and-statistics.md) introduces retrieval metrics and statistical calculations. Precise metric definitions are documented by [Ragas](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).

The outcome table and exercises here are original; see [source credits](../ATTRIBUTIONS.md).

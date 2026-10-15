# Module 03 — Prompting, structured output, and AI-assisted development

[Course index](../README.md) · Weeks 5–6 · Prerequisites: Modules 01–02

## Outcomes

Write explicit task contracts, compare prompt versions fairly, and review AI-generated code with independent checks.

## Lesson 1: Prompt as a behavioral specification

A useful prompt states the task, relevant context, constraints, output format, and what to do when information is insufficient. Examples illustrate intended decisions. An example set that covers only easy cases can teach an oversimplified boundary.

For bug triage, define severity using impact and a documented policy. Do not rely on adjectives such as “critical” appearing in a user report. Specify clarification behavior when impact is missing. Separate report text from trusted instructions so the application treats the report as data.

Version the entire prompt configuration, including examples. Changing an example can change behavior just as changing instructions can.

## Lesson 2: Structured output has two contracts

The structural contract defines fields, types, enum values, and required properties. The semantic contract defines whether their contents are justified. Schema-constrained output, where supported, helps enforce structure; it does not validate business truth.

Original example:

```json
{
  "component": "authentication",
  "severity": "high",
  "needs_clarification": false,
  "evidence": ["All users are unable to sign in after deployment."]
}
```

A grader can validate the enum and list type exactly. Whether “high” follows the severity policy requires a separate decision check. Treat invalid or incomplete model responses as explicit outcomes.

## Lesson 3: Controlled prompt iteration

Write acceptance criteria before asking an AI coding tool to implement a feature. Request a small change, inspect its diff, run independent checks, and investigate failures. Generated tests can repeat the implementation's mistaken assumptions. Derive important test cases from requirements and known risks.

For a prompt comparison, use the same cases and grading rules. Freeze the comparison configuration. Inspect wins and losses rather than accepting a higher aggregate score automatically.

## Lab

1. Write a severity rubric with at least one ambiguous case.
2. Create 30 development cases and reserve separate evaluation cases.
3. Build prompt A with instructions only.
4. Build prompt B with selected examples.
5. Compare structure validity, decision correctness, and clarification behavior.
6. Examine every changed decision and record its likely cause.
7. Ask an AI coding tool for one small improvement, review it, and document the checks that support accepting it.

Do not insert reference answers into production input during evaluation.

## Review and answers

- **Does JSON validity imply correct classification?** No; it only establishes one part of the contract.
- **Why freeze graders during a comparison?** Changing the measurement at the same time makes the result difficult to interpret.
- **Is “always return an answer” useful?** It can encourage unsupported answers; define when to clarify or abstain.
- **What should you review in generated tests?** Whether expected outcomes follow the requirements independently of the proposed code.

## Exit evidence

Two versioned prompt configurations, a paired results table, reviewed failures, and one explained code review.

## Supplementary reading and attribution

Use the prompting sections of [Microsoft's course](https://github.com/microsoft/generative-ai-for-beginners) and the comparison examples in [Promptfoo](https://github.com/promptfoo/promptfoo). Consult current provider documentation for exact structured-output APIs.

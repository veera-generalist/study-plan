# Module 02 — Models, tokens, embeddings, and ML basics

[Course index](../README.md) · Weeks 3–4 · Prerequisite: Module 01

## Outcomes

Explain model behavior at an engineering level and calculate classification metrics. You do not need to train a foundation model to build a reliable AI application.

## Lesson 1: A language model in an application

A generative language model estimates probabilities over continuations conditioned on its input. Inference runs the model; training changes its parameters. Instruction tuning teaches patterns of responding to instructions, but does not guarantee factual correctness or compliance in every situation.

Tokenizers divide text into model-specific units. A token may be a word fragment, punctuation, or another unit. The same visible text can have different token counts under different tokenizers. Context limits constrain supplied instructions, history, retrieved content, tool messages, and generated content according to the model's interface.

Sampling selects among possible tokens. Lower temperature can reduce sampling variation when supported, but does not guarantee identical behavior across service updates, infrastructure, or all execution conditions. Record supported settings rather than assuming all models expose the same controls.

## Lesson 2: Embeddings and retrieval

An embedding maps an item into a numeric vector. A similarity measure helps retrieve related items. Semantic similarity is not a truth test: “roll back after five failures” and “never roll back after five failures” may be close in topic while differing in meaning.

A Transformer uses attention to combine information from positions in a sequence. For application work, understand the consequences: context management matters, information can be overlooked, and long input does not guarantee complete use of all evidence.

## Lesson 3: Basic ML reasoning

Training data fits parameters; development data guides choices; held-out evaluation estimates behavior after those choices. Repeatedly optimizing against a held-out set turns it into development data in practice.

For a chosen positive class:

- Precision = true positives / predicted positives.
- Recall = true positives / actual positives.
- F1 is the harmonic mean of precision and recall when defined.
- Accuracy is the fraction of all predictions that are correct.

Choose how to report undefined metrics when a denominator is zero. Do not silently convert “not measured” into perfect quality.

## Worked example

There are 10 urgent bugs among 100 reports. A classifier marks 12 urgent: 8 are truly urgent and 4 are not. Precision is 8/12, about 67%; recall is 8/10, 80%. It misses two urgent bugs. Overall accuracy is 94%, which hides that operationally important weakness.

## Lab

Create 50 synthetic bug reports spanning components and urgency. Write labels before examining model predictions. Compare a simple keyword baseline with a model classifier when available. Report a confusion matrix, per-class precision/recall, and five reviewed errors. Preserve the baseline even if the model is better.

## Review and answers

- **Does fluent output establish truth?** No; evaluate claims against evidence or task requirements.
- **Does semantic similarity mean equivalence?** No; related statements can contradict each other.
- **Why preserve a simple baseline?** It reveals whether added complexity delivers meaningful benefit.
- **When should you fine-tune?** After identifying a persistent task gap, establishing evaluation, and obtaining suitable data; it does not repair a missing source document by itself.

## Exit evidence

A metric calculation you can reproduce manually, your classifier comparison, and explanations of tokenization, inference, and leakage.

## Supplementary reading and attribution

Study tokenizers, datasets, and Transformers in the [Hugging Face course](https://github.com/huggingface/course). These notes and the bug example are original teaching material; see [attributions](../ATTRIBUTIONS.md).

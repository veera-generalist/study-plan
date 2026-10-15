# Module 02 — Models, tokens, embeddings, and ML basics

[Course index](../README.md) · Weeks 3–4 · Prerequisite: Module 01

**Terms to know:** [LLM](../GLOSSARY.md#llm) · [Token](../GLOSSARY.md#token) · [Context window](../GLOSSARY.md#context-window) · [Embedding](../GLOSSARY.md#embedding) · [Inference](../GLOSSARY.md#inference) · [Temperature](../GLOSSARY.md#temperature)

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

## Detailed tutorial: understanding what the model is doing

### 1. From text to a generated response

A typical generative language-model request begins by converting content into token IDs. An embedding layer maps IDs into numeric representations. Transformer layers transform those representations using attention and other operations. A language-model output head produces scores, called logits, for candidate next tokens. A decoding procedure selects a token and repeats.

This is a simplified account of a text-generating Transformer, not a complete description of every model architecture. It explains several practical facts. The model does not search a database of guaranteed truths on every token. Plausible continuations may include invented details. A complete response is built through sequential choices rather than retrieved as one verified fact.

Distinguish pretraining from instruction tuning and inference. Pretraining learns broad statistical structure from training examples. Instruction tuning further shapes response behavior. Inference uses already learned parameters. Adding documents to a prompt changes the inference context; it does not normally update the model's weights.

### 2. Why tokenization matters to QA

“BUG-1042” may become several tokens, and a whitespace split is not a reliable model token count. Different languages and identifiers can tokenize differently. A context-budget test should use the tokenizer associated with the chosen model, or the provider's documented counting mechanism.

Budget the complete request: instructions, history, retrieved passages, tool definitions/results, and any required output allowance. Exact accounting rules vary by interface. A huge history may force truncation of the very message defining the task. A long document may be accepted but poorly used. Acceptance of input and successful use of evidence require different checks.

Construct boundary cases around unusually long identifiers, pasted logs, multilingual text, and repeated tool messages. Inspect which content survives your application's context-management logic.

### 3. Logits, probabilities, and temperature

Softmax converts a vector of logits into positive numbers summing to one. For logit z_i, a simplified temperature-adjusted probability is exp(z_i/T) divided by the sum across candidates. Subtracting the largest scaled logit before exponentiating improves numerical stability without changing the ratio.

Lower positive temperature concentrates mass on high-scoring options. It does not make an incorrect highest-scoring option correct. Temperature zero, where supported, is typically treated specially by the serving implementation; our example rejects it rather than attempting division by zero.

Token probabilities are probabilities of continuations under the model. They are not automatically calibrated probabilities that an entire generated answer is factually correct.

### 4. Embeddings without the mystery

Think of an embedding as a location in a learned representation space. Cosine similarity measures directional alignment: dot product divided by the product of vector lengths. Identical directions have similarity one; orthogonal directions zero. Real embedding models can represent much more than the two-dimensional example below.

If two sentences discuss rollback policy, they can be semantically close even when one says to roll back and the other says not to. Similarity helps select candidate evidence. It cannot replace contradiction checking, authorization, or factual verification.

### 5. Runnable numeric example

```python
"""Module 02: softmax, vector similarity, and a classifier confusion count."""
from math import exp, sqrt


def softmax(logits, temperature=1.0):
    if temperature <= 0:
        raise ValueError("This demonstration requires positive temperature")
    scaled = [value / temperature for value in logits]
    largest = max(scaled)
    weights = [exp(value - largest) for value in scaled]
    total = sum(weights)
    return [value / total for value in weights]


def cosine(left, right):
    if len(left) != len(right):
        raise ValueError("Vector dimensions differ")
    denominator = sqrt(sum(x*x for x in left) * sum(y*y for y in right))
    if denominator == 0:
        raise ValueError("Zero vectors have undefined cosine similarity")
    return sum(x*y for x, y in zip(left, right)) / denominator


labels = [1, 1, 1, 1, 0, 0]
predictions = [1, 1, 1, 0, 1, 0]
tp = sum(y == 1 and p == 1 for y, p in zip(labels, predictions))
fp = sum(y == 0 and p == 1 for y, p in zip(labels, predictions))
fn = sum(y == 1 and p == 0 for y, p in zip(labels, predictions))
precision = tp / (tp + fp)
recall = tp / (tp + fn)
assert precision == 0.75 and recall == 0.75
cool = softmax([2.0, 1.0, 0.0], temperature=0.5)
warm = softmax([2.0, 1.0, 0.0], temperature=1.0)
assert abs(sum(cool) - 1.0) < 1e-12
assert cool[0] > warm[0]
assert abs(cosine([1, 0], [1, 0]) - 1.0) < 1e-12
print("probabilities:", [round(value, 3) for value in warm])
print("precision:", precision, "recall:", recall)
```

Run [the saved example](../labs/module-examples/02_example.py). It prints probabilities approximately 0.665, 0.245, and 0.090 for the three logits, then precision and recall of 0.75. These are calculations over synthetic numbers, not observed model performance.

The positive label means “urgent.” There are three true positives, one false positive, one false negative, and one true negative. Precision asks how many flagged reports really were urgent. Recall asks how many urgent reports were caught. Which error matters more depends on the consequences of missed urgent bugs and unnecessary escalation.

### 6. Multiclass metrics and imbalance

For multiple components, calculate precision/recall per class by treating each class as positive in turn. Macro averaging gives equal weight to classes. A support-weighted average gives more influence to common classes. Micro aggregation pools decisions; for ordinary single-label multiclass classification with complete predictions, micro precision/recall equal accuracy.

State your averaging method. A system that predicts “other” for every report may look good when that category dominates. It still fails the purpose of identifying rare authentication outages.

An abstaining classifier adds another decision. Report coverage (fraction receiving a substantive decision) alongside quality among answered cases. A system can improve answered-case accuracy merely by answering less often.

### 7. Data splits and overfitting in application work

Even if you never train weights, you can overfit by repeatedly editing prompts against the same questions. Development examples influence your decisions. A held-out set supports a more independent estimate only while it remains protected from those decisions.

When failures on the held-out set are inspected and used to improve a prompt, document that transition and reserve fresh independent cases for the next final assessment. Keep related or near-duplicate questions together where appropriate.

### 8. Guided exercise and interpretation

Add four negative examples to the numeric classifier exercise and predict all four correctly. Overall accuracy rises while the original missed urgent bug remains. Explain why that change does not improve urgent-case recall.

Then multiply both embedding vectors by positive constants. Cosine similarity stays the same because lengths cancel. Replace one vector with a zero vector: the similarity is undefined, so the example raises an error rather than returning a misleading default.

Finally, create a task where a keyword baseline works very well: component classification using explicit component names. This is a useful control. If a sophisticated model does not beat the baseline on relevant difficult cases, justify the added complexity before adopting it.

For tokenizer mechanics, see the [Hugging Face tokenizer chapter](https://huggingface.co/learn/llm-course/chapter6/1). All numeric examples here are original.

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

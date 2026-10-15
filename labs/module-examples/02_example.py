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

"""Module 08: paired bootstrap and a Wilson interval on synthetic outcomes."""
import random
from math import sqrt
from statistics import mean

# Same eight tasks, evaluated under two configurations.
baseline = [1, 1, 1, 1, 0, 0, 0, 0]
candidate = [1, 1, 1, 0, 1, 1, 0, 0]


def paired_bootstrap(a, b, repetitions=2000, seed=7):
    if len(a) != len(b) or not a:
        raise ValueError("Need nonempty paired samples")
    rng = random.Random(seed)
    differences = [right - left for left, right in zip(a, b)]
    estimates = sorted(
        mean(rng.choice(differences) for _ in differences)
        for _ in range(repetitions)
    )
    return mean(differences), (
        estimates[int(0.025 * repetitions)],
        estimates[int(0.975 * repetitions) - 1],
    )


def wilson(successes, total, z=1.96):
    if total <= 0 or not 0 <= successes <= total:
        raise ValueError("Invalid binomial counts")
    p = successes / total
    denominator = 1 + z*z / total
    center = (p + z*z / (2*total)) / denominator
    half = z * sqrt(p*(1-p)/total + z*z/(4*total*total)) / denominator
    return center - half, center + half


difference, interval = paired_bootstrap(baseline, candidate)
assert difference == 0.125
assert interval[0] <= difference <= interval[1]
assert interval[0] <= 0 <= interval[1]
lower, upper = wilson(8, 8)
assert lower < 1.0 and abs(upper - 1.0) < 1e-12
print("Observed candidate-minus-baseline:", difference)
print("Illustrative paired percentile interval:", interval)
print("Wilson interval for 8/8 passes:", (round(lower, 3), round(upper, 3)))

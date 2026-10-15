"""Module 06: evaluate a judge as a failure detector."""
# True means the answer is a failure under adjudicated human labels.
human_failure = [True, True, True, False, False, False]
judge_failure = [True, False, True, True, False, False]
tp = sum(h and j for h, j in zip(human_failure, judge_failure))
fp = sum(not h and j for h, j in zip(human_failure, judge_failure))
fn = sum(h and not j for h, j in zip(human_failure, judge_failure))
tn = sum(not h and not j for h, j in zip(human_failure, judge_failure))
precision = tp / (tp + fp)
recall = tp / (tp + fn)
false_pass_ids = [
    index + 1 for index, (h, j) in enumerate(zip(human_failure, judge_failure))
    if h and not j
]
assert (tp, fp, fn, tn) == (2, 1, 1, 2)
assert false_pass_ids == [2]
print("Failure detection precision:", round(precision, 3))
print("Failure detection recall:", round(recall, 3))
print("False-pass example IDs:", false_pass_ids)

# Pairwise position check: preferences are mapped back to candidate identity.
original_order = ["A", "B"]
swapped_order = ["B", "A"]
selected_original_position = 0
selected_swapped_position = 0
winner_first = original_order[selected_original_position]
winner_swapped = swapped_order[selected_swapped_position]
assert winner_first != winner_swapped
print("Always selecting the first position creates inconsistent candidate preferences.")

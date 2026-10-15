# A small optional Python example

Lesson 05 includes a short program that counts outcomes you have already reviewed.

From the repository root:

```sh
python3 labs/beginner/05_count_answers.py
```

Expected output:

```text
Answers meeting the requirements: 2
Answers reviewed: 4
```

The program starts with four outcomes stored as text. It counts how often the exact word “meets” occurs and how many outcomes exist. It does not read customer answers, check facts, call a model, or determine whether a review is correct.

To experiment, change one “does not meet” entry to “meets.” The first count should become 3 while the total stays 4. Restore the file afterward if you want it to match the lesson again.

You can complete [Lesson 05](../../modules/05-evaluation-harnesses.md) manually without running this program. When you are ready for more coding, use the [setup guide](../../SETUP.md) and [optional technical notes](../../advanced/README.md).

The code and example data are original.

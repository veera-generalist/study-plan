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

## From one program to the technical notes

If you are new to programming, take this as a separate practice stage. The technical notes introduce data classes, type hints, exceptions, and adapters; the counting program alone does not prepare you for all of them.

First complete the [optional Python setup](../../SETUP.md). Run commands in your terminal from the repository root. Save Python code in a file ending in `.py`; a terminal command such as `python3 path/to/file.py` tells Python which file to run. Do not paste the command itself into the Python file.

Work through these steps one at a time. Make practice copies in your own learning folder so the saved lesson example continues to match its lesson.

| Step | What the idea means | Small exercise and expected result |
|---|---|---|
| 1. Names and text | A name refers to a value; text in quotes is a string. | Change a printed message in your copy. Only the displayed wording should change. |
| 2. Lists and counting | A list stores a sequence. `count` counts exact matches; `len` gives the number of entries. | Add one `"meets"` entry. The successful count becomes 3 and the total becomes 5. |
| 3. Conditions and loops | A condition chooses a branch; a loop repeats work for each item. | Print each outcome with a loop. Add a condition that prints `"Check this answer"` only for the two `"does not meet"` entries. |
| 4. Dictionaries | A dictionary connects field names with values. | Store one result with fields `id`, `question`, and `outcome`. Print the question using its field name. |
| 5. Functions | A function gives a reusable operation a name and returns a result. | Move counting into a function accepting a list. The original list should return 2; an empty list should return 0. |
| 6. Files and JSON | A file keeps data between runs. JSON is a text format for structured data. | Save two result dictionaries as one JSON list, read it back, and print both IDs. JSONL, used later, instead stores one JSON object per line. |
| 7. Errors | An exception reports that an operation could not finish as requested. | Try reading a nonexistent practice file and a file with broken JSON. Explain which failure is about the path and which is about its contents. |

For explanations and syntax, use the official [Python tutorial](https://docs.python.org/3/tutorial/): “An Informal Introduction to Python,” “More Control Flow Tools,” “Data Structures,” “Input and Output,” and “Errors and Exceptions.” The tutorial assumes some general programming understanding. If a section moves too quickly, work through just its first small examples before returning to the exercise. You do not need to finish the entire tutorial before returning to AI study.

Before opening [technical note 01](../../advanced/01-python-engineering.md), check that you can explain your list, loop, function, and file-reading code. Start that note with input validation and the fake adapter. A fake adapter supplies a predictable response so you can understand the application before adding a model service.

The [offline evaluator](../offline-evaluation/README.md) is a later reading exercise. The [local-model adapter](../live-model/README.md) comes after you can follow how a request and response move through functions. It uses a separate classification task; the [contract map](../../advanced/README.md#example-contracts) explains that transition.

These practice steps develop Python foundations; they do not call a language model or implement the whole bookshop application. Keep your own code and observations as evidence of what you ran.

The code, exercise sequence, and example data are original. Python's tutorial is linked as further reading; see [attributions](../../ATTRIBUTIONS.md).

# Annotated GitHub reading library

## Teaching structure and introductory reading

Microsoft's Generative AI for Beginners is a supplementary course and the inspiration for the scenario-led organization of all twelve lessons. Our explanations and exercises are original. These three pages were reviewed as teaching-structure references:

- [Introduction to generative AI](https://github.com/microsoft/generative-ai-for-beginners/blob/main/01-introduction-to-genai/README.md)
- [Exploring and comparing language models](https://github.com/microsoft/generative-ai-for-beginners/blob/main/02-exploring-and-comparing-different-llms/README.md)
- [Prompt engineering fundamentals](https://github.com/microsoft/generative-ai-for-beginners/blob/main/04-prompt-engineering-fundamentals/README.md)

Our topic sequence is different from Microsoft's. Use the written explanations first. External notebooks, framework installation, and model access are not prerequisites for the written activities. Each lesson links to optional technical notes and relevant further reading.

<details>
<summary>Reference library for later technical study</summary>

Use this as a reading sequence, not a list of frameworks to install simultaneously. Read concepts, execute one example, inspect its tests, and deliberately reproduce a failure. Record the revision and dependency versions you used.

## Core sequence

| Order | Resource | What to study | Exercise |
|---|---|---|---|
| 1 | [Microsoft: Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) | Foundation, prompting, text/chat application, and search lessons | Add explicit expected behavior and failure cases to one example |
| 2 | [Hugging Face Course](https://github.com/huggingface/course) | Tokenization, model inference, and datasets | Inspect tokenization of identifiers and multilingual text |
| 3 | [DeepEval](https://github.com/confident-ai/deepeval) | Quickstart, test cases, metrics, and metric inputs | Implement one deterministic check plus one semantic metric |
| 4 | [Promptfoo](https://github.com/promptfoo/promptfoo) | Getting-started example, assertions, comparisons, CI concepts | Compare two prompts on identical cases |
| 5 | [Ragas](https://github.com/vibrantlabsai/ragas) | RAG evaluation example and metric definitions | Trace a score back to its evidence and assumptions |
| 6 | [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) | Classification, RAG, tool use, and evaluation recipes | Adapt one recipe to a small project with synthetic data and evaluate it |
| 7 | [Hugging Face Agents Course](https://github.com/huggingface/agents-course) | Fundamentals, one framework, observability/evaluation, final assignment | Inspect a tool-using agent's execution |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | Quickstart, state, persistence, human oversight | Build a resumable sandbox workflow |
| 9 | [Phoenix](https://github.com/Arize-ai/phoenix) | Tracing, datasets, and experiments | Diagnose retrieval and tool failures from traces |
| 10 | [garak](https://github.com/NVIDIA/garak) | Probes, generators/targets, detectors, result interpretation | Review a scoped finding against your own sandbox |

Choose DeepEval **or** Promptfoo as your first evaluation framework. Learn the other's approach later. Model-based grading may require inference access even when the evaluation framework itself is open source.

## Advanced branches

- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness): study task definitions, model adapters, scoring, and reproducibility. Useful for model capability benchmarks; distinct from validating your complete application.
- [DSPy](https://github.com/stanfordnlp/dspy): study modular model programs and optimization after establishing trustworthy metrics.
- [Made With ML](https://github.com/GokuMohandas/Made-With-ML): broaden production engineering and ML lifecycle knowledge.

## Concept readings

- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents): compare prescribed workflows with model-driven decisions.
- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): examine task environments, graders, and repeated trials.
- [Ragas context recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/) and [faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/): inspect exact inputs and formulas.

## Maintenance notes from source review

Reviewed 2026-10-15. The older [Anthropic courses repository](https://github.com/anthropics/courses) is archived; use it as historical conceptual material and verify old SDK examples against current documentation. [Hugging Face Evaluate](https://github.com/huggingface/evaluate) points readers to LightEval for newer LLM evaluation approaches. Ragas and Claude Cookbooks links above use their observed canonical repository locations.

See the [reference snapshots](references/README.md) for exact repository revisions and license files. Ragas documentation includes current and legacy API examples; match the documentation to the package you install. Microsoft's course README includes a July 2026 GitHub Models retirement notice, so review its current setup choices before using old notebooks. Phoenix's license is Elastic License 2.0; do not infer permissive reuse from its source being visible.

For a first concrete model adapter after the offline exercises, use the [optional local-model lab](labs/live-model/README.md). It follows the [Ollama chat API](https://docs.ollama.com/api/chat); real inference needs your own prepared local model and was not run during source review.

Stars and popularity are not selection criteria here. Choose resources for conceptual coverage, usable examples, and relevance to your task.

## Repository study worksheet

For each reading, record:

- Exact repository, revision, and example examined.
- Concept explained in your own words.
- Inputs, outputs, state, and external dependencies.
- Tests that exist and gaps you found.
- One induced failure and how it was detected.
- What you would reuse, its license, and required notices.

See [ATTRIBUTIONS.md](ATTRIBUTIONS.md) before importing source material.

</details>

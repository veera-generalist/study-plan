# Reference snapshots and freshness

Reviewed on **2026-10-15** using GitHub repository metadata, directory/file reads, and primary documentation pages.

These snapshots let you find the exact repository revision recorded during this review. They do not mean every upstream example was run, that its dependencies are pinned here, or that a linked website matches that repository revision. Prefer current docs for a new installation, and record the exact versions you actually use.

| Repository | Snapshot | License file at snapshot |
|---|---|---|
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | [d45da91247](https://github.com/microsoft/generative-ai-for-beginners/tree/d45da91247ecb91e5346caacdd5a5fb9c5b9d85e) | [Read license](https://github.com/microsoft/generative-ai-for-beginners/blob/d45da91247ecb91e5346caacdd5a5fb9c5b9d85e/LICENSE) |
| [huggingface/course](https://github.com/huggingface/course) | [8b893f0ede](https://github.com/huggingface/course/tree/8b893f0ede6c781045692a7f892f25a0c92b4805) | [Read license](https://github.com/huggingface/course/blob/8b893f0ede6c781045692a7f892f25a0c92b4805/LICENSE) |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | [3c469e773e](https://github.com/huggingface/agents-course/tree/3c469e773ec04e5f338b727ff20e3a6ea823ff81) | [Read license](https://github.com/huggingface/agents-course/blob/3c469e773ec04e5f338b727ff20e3a6ea823ff81/LICENSE) |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | [b2b0aa1ff7](https://github.com/anthropics/claude-cookbooks/tree/b2b0aa1ff7d8980b005b225d3802969c87bedad5) | [Read license](https://github.com/anthropics/claude-cookbooks/blob/b2b0aa1ff7d8980b005b225d3802969c87bedad5/LICENSE) |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | [03ef3a25c2](https://github.com/confident-ai/deepeval/tree/03ef3a25c2acbf09ef001080d2591704b9606931) | [Read license](https://github.com/confident-ai/deepeval/blob/03ef3a25c2acbf09ef001080d2591704b9606931/LICENSE.md) |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | [1c28848f61](https://github.com/promptfoo/promptfoo/tree/1c28848f61a21719867b81fbd0f105f1aa1e8f1f) | [Read license](https://github.com/promptfoo/promptfoo/blob/1c28848f61a21719867b81fbd0f105f1aa1e8f1f/LICENSE) |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) | [298b682742](https://github.com/vibrantlabsai/ragas/tree/298b68274234c060deacab3cf5fb52aa3a20e885) | [Read license](https://github.com/vibrantlabsai/ragas/blob/298b68274234c060deacab3cf5fb52aa3a20e885/LICENSE) |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | [5eb60aef6f](https://github.com/langchain-ai/langgraph/tree/5eb60aef6f3837a1fb632a8abc6cf8e8da81785b) | [Read license](https://github.com/langchain-ai/langgraph/blob/5eb60aef6f3837a1fb632a8abc6cf8e8da81785b/LICENSE) |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | [dd3265653f](https://github.com/Arize-ai/phoenix/tree/dd3265653f10e0534ae99021d3be5a894227706c) | [Read license](https://github.com/Arize-ai/phoenix/blob/dd3265653f10e0534ae99021d3be5a894227706c/LICENSE) |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | [197d68645e](https://github.com/NVIDIA/garak/tree/197d68645ecc8cec1a71ea20872823a8b54f92f3) | [Read license](https://github.com/NVIDIA/garak/blob/197d68645ecc8cec1a71ea20872823a8b54f92f3/LICENSE) |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | [d6de816439](https://github.com/EleutherAI/lm-evaluation-harness/tree/d6de81643928d653435c431bae19945d41d32520) | [Read license](https://github.com/EleutherAI/lm-evaluation-harness/blob/d6de81643928d653435c431bae19945d41d32520/LICENSE.md) |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | [ef98720641](https://github.com/stanfordnlp/dspy/tree/ef98720641823d097fe12e57bd0a9695b57c4bcf) | [Read license](https://github.com/stanfordnlp/dspy/blob/ef98720641823d097fe12e57bd0a9695b57c4bcf/LICENSE) |
| [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) | [3361aeb8dd](https://github.com/GokuMohandas/Made-With-ML/tree/3361aeb8ddfc2affdba9f545c978c38c85cee764) | [Read license](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/LICENSE) |

Machine-readable record: [repositories.json](repositories.json).

## Freshness findings

- Core repository destinations resolved during review. The [older Anthropic courses repository](https://github.com/anthropics/courses) is archived and remains historical reading only.
- [Hugging Face Evaluate](https://github.com/huggingface/evaluate) directs newer LLM-evaluation users toward LightEval. It is not the course's primary application-evaluation tool.
- [Ragas context-recall documentation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/) distinguishes current collections-based examples from legacy API examples. Match the installed package version to its documentation.
- [Microsoft's course setup](https://github.com/microsoft/generative-ai-for-beginners) marks its GitHub Models setup path as retired and points readers to alternatives. Do not follow an old setup notebook blindly.
- [Phoenix's license](https://github.com/Arize-ai/phoenix/blob/dd3265653f10e0534ae99021d3be5a894227706c/LICENSE) identifies Elastic License 2.0. Source visibility is not the same as having a permissive license; read the file before reuse.
- Python's `/3/` documentation follows the current documentation release. The local verification runtime was **Python 3.14.8**. Select the documentation version matching your installed interpreter when a feature differs.

## Documentation destinations checked

Primary documentation destinations for Python (tutorial, glossary, statistics, license), Hugging Face tokenizers, Google ML glossary, Ragas context recall/faithfulness, MCP introduction, OpenTelemetry traces/observability, and the two Anthropic agent-engineering articles were retrievable during review. The optional live-model lab also references the reviewed Ollama quickstart and chat API.

This is a dated source review, not a continuous availability guarantee. The local checker validates local links and heading fragments; it does not crawl external websites or verify their fragments.

## Repeat the source review

Check repository redirects and archived status, capture the current default-branch revision, inspect the actual license path, and verify that the referenced concepts still appear in the docs. Record new snapshots deliberately. A moved or retired API example should be marked or replaced rather than silently kept as a current installation guide.

No external source text, figures, or code are copied into this snapshot directory. See [attributions](../ATTRIBUTIONS.md).

# JavaRagAssistant

JavaRagAssistant indexes a Java codebase and uses Retrieval Augmented Generation (RAG) to help plan and implement new features. It currently stores embeddings in memory and on disk but is structured so it can be extended to use Postgres/pgvector in the future.

## Installation

1. Install Python 3.12 or newer.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install and set up [Ollama](https://ollama.ai) then pull the Mistral model:

```bash
ollama pull mistral
```

## Usage

Place your Java project inside the `codebase/` directory. Then run:

```bash
python main.py
```

You'll be prompted to enter a feature request. The tool indexes the Java files, retrieves relevant code snippets and coordinates four AI agents (Architect, Engineer, Reviewer, Tester) to respond.

Embeddings are saved to `code_index.json` for reuse on the next run.

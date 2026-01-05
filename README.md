# my-project

A minimal Python project skeleton for experimenting with LLM-powered workflows (managed with Poetry).

Overview

- Example usage of LangGraph and LangChain OpenAI-compatible client to demonstrate a basic chatbot flow (see `src/main.py`).
- Small set of file utilities in `src/tools.py` to read, list, and rename files inside the project.

Features

- Lightweight starter structure with Poetry for dependency management.
- Example integration with OpenRouter/OpenAI-compatible APIs via `langchain_openai`.

Prerequisites

- Python 3.13
- Poetry (recommended for dependency and virtual environment management)

Installation

```bash
# Install project dependencies and create virtual environment (Poetry manages venv by default)
poetry install
poetry shell
```

Environment variables

This project expects sensitive configuration (API keys) to be provided via an environment variable or a `.env` file in the project root. Example `.env` contents:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Security note: Do not commit real secrets to your repository. Add `.env` to `.gitignore` and consider providing `.env.example` (without real values) to document required keys.

Running the example

The repository includes a small runnable example that composes a LangGraph state graph and calls an LLM. Run it from the project root:

```bash
python -m src.main
```

`src/main.py` will load the `.env` file (if present) and attempt to call an OpenRouter-compatible endpoint using `langchain_openai.ChatOpenAI`. Ensure `OPENROUTER_API_KEY` is set before running the example.

Project structure

```
├── pyproject.toml        # Poetry / project configuration
├── README.md             # This file
├── .env                  # Environment variables (DO NOT commit real secrets)
├── src/
│   ├── main.py           # Example entrypoint: LangGraph + langchain_openai usage
│   ├── tools.py          # Small file utilities (read/list/rename)
│   └── my_project/       # Package sources (expand as needed)
└── tests/                # Unit tests
```

API / utilities in `src/tools.py`

- `read_file(name: str) -> str` — Read the contents of a file relative to the project root and return the text (returns an error string on failure).
- `list_files() -> list[str]` — Return a list of file paths (relative to the project root) found recursively under the project root.
- `rename_file(name: str, new_name: str) -> str` — Rename a file inside the project root to a new relative path (creates parent directories if necessary). Returns a status string.

Troubleshooting

- Missing environment variables / KeyError:
  - Ensure `.env` exists in the project root or export `OPENROUTER_API_KEY` in your shell.
  - Example: `export OPENROUTER_API_KEY=your_key_here`.

- Dependency or import errors:
  - Run `poetry install` to make sure dependencies are installed in the environment Poetry created.
  - Verify the current Python interpreter matches the version declared in `pyproject.toml`.

- LLM / API connectivity issues:
  - Verify network access to `https://openrouter.ai/api/v1` (or your provider's base URL).
  - Confirm the API key is valid and has the right permissions.

Testing

There are currently no unit tests included by default. Recommended next steps:

- Add tests for `src/tools.py` (happy path + error handling).
- Add CI configuration (GitHub Actions / other) to run tests and linting automatically.

Contributing

Contributions are welcome. Please open an issue or submit a pull request. Consider adding tests and updating the README when you change behavior.

License

No license is included by default. If you want to open source this project, add a `LICENSE` file (for example, MIT) to the repository root.

Contact

Author information is specified in `pyproject.toml` under the `authors` field.

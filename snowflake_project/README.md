# Snowflake Sample Project

This sample project demonstrates a simple Snowflake connection with Python and a GitHub Actions-driven migration workflow.

## What is included

- `app.py`: sample Python app that connects to Snowflake and prints the current Snowflake version.
- `snowflake_utils.py`: connection helper functions for Snowflake.
- `.env.example`: example Snowflake environment variable configuration.
- `requirements.txt`: required Python dependencies.
- `migrations/`: existing SQL migration files used by the GitHub Actions workflow.

## Quick start

1. Copy `.env.example` to `.env` and fill in your Snowflake credentials.
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the sample app:

```bash
python app.py
```

## GitHub Actions

The existing workflow in `.github/workflows/MyFirstGitHub.yml` runs `schemachange` on any push to `migrations/**`.

## Notes

- Do not commit `.env` or any secrets.
- Use `migrations/` to add versioned SQL changes for Snowflake.

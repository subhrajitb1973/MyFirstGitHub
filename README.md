# MyFirstGitHub

This repository contains a sample Snowflake project, including a Python connection demo and a migration workflow.

## Contents

- `snowflake_project/` - Python sample for Snowflake connectivity.
- `migrations/` - Snowflake SQL migration files used by GitHub Actions.
- `.github/workflows/MyFirstGitHub.yml` - automation workflow for `schemachange`.

## Quick start

1. Open `snowflake_project/.env.example` and copy it to `snowflake_project/.env`.
2. Fill in your Snowflake credentials.
3. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r snowflake_project/requirements.txt
```

4. Run the sample app:

```powershell
python snowflake_project/app.py
```

## GitHub Actions

The workflow triggers on changes under `migrations/**` and runs `schemachange` against your Snowflake account using repository secrets.

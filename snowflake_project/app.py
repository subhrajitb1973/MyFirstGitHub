import os
from dotenv import load_dotenv
from snowflake_utils import create_connection, query_current_version


def main() -> None:
    load_dotenv()

    connection_args = {
        "account": os.getenv("SF_ACCOUNT", ""),
        "user": os.getenv("SF_USERNAME", ""),
        "password": os.getenv("SF_PASSWORD", ""),
        "role": os.getenv("SF_ROLE", "ACCOUNTADMIN"),
        "warehouse": os.getenv("SF_WAREHOUSE", ""),
        "database": os.getenv("SF_DATABASE", ""),
        "schema": os.getenv("SF_SCHEMA", "PUBLIC"),
    }

    missing = [key for key, value in connection_args.items() if not value]
    if missing:
        raise SystemExit(
            f"Missing Snowflake configuration values: {', '.join(missing)}\n"
            "Copy .env.example to .env and fill in the values."
        )

    with create_connection(**connection_args) as conn:
        rows = query_current_version(conn)
        print("Connected to Snowflake successfully.")
        print("Snowflake version:")
        for row in rows:
            print(row[0])


if __name__ == "__main__":
    main()

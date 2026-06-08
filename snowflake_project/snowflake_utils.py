from contextlib import contextmanager
from typing import Iterator, Any

import snowflake.connector
from snowflake.connector.connection import SnowflakeConnection


@contextmanager
def create_connection(
    account: str,
    user: str,
    password: str,
    role: str,
    warehouse: str,
    database: str,
    schema: str,
) -> Iterator[SnowflakeConnection]:
    conn = snowflake.connector.connect(
        account=account,
        user=user,
        password=password,
        role=role,
        warehouse=warehouse,
        database=database,
        schema=schema,
    )
    try:
        yield conn
    finally:
        conn.close()


def query_current_version(conn: SnowflakeConnection) -> list[Any]:
    with conn.cursor() as cursor:
        cursor.execute("SELECT current_version()")
        return cursor.fetchall()


import sqlite3
from pathlib import Path

from src.sql_safety import validate_sql

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "sales.db"


def execute_query(sql: str) -> list[tuple]:
    """Validate and execute a read-only SQL query."""

    if not validate_sql(sql):
        raise ValueError("Unsafe SQL query rejected.")

    database_uri = f"{DB_PATH.as_uri()}?mode=ro"

    with sqlite3.connect(database_uri, uri=True) as connection:
        cursor = connection.execute(sql)
        return cursor.fetchall()

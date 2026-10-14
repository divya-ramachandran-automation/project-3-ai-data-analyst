
import re


def validate_sql(sql: str) -> bool:
    """Allow only a single, read-only SELECT query."""

    cleaned_sql = sql.strip()

    if not cleaned_sql:
        return False

    # Allow at most one trailing semicolon.
    if cleaned_sql.endswith(";"):
        cleaned_sql = cleaned_sql[:-1].strip()

    # Reject multiple statements.
    if ";" in cleaned_sql:
        return False

    # Only allow queries that start with SELECT or WITH.
    if not re.match(r"^(SELECT|WITH)\b", cleaned_sql, re.IGNORECASE):
        return False

    # Reject common SQL modification commands.
    forbidden = re.compile(
        r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|REPLACE|"
        r"ATTACH|DETACH|PRAGMA|VACUUM|REINDEX|TRUNCATE)\b",
        re.IGNORECASE,
    )

    if forbidden.search(cleaned_sql):
        return False

    return True

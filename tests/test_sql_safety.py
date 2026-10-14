
import sqlite3
from src.sql_safety import validate_sql


def test_select_query_is_allowed():
    assert validate_sql("SELECT * FROM sales") is True


def test_select_with_trailing_semicolon_is_allowed():
    assert validate_sql("SELECT * FROM sales;") is True


def test_delete_query_is_rejected():
    assert validate_sql("DELETE FROM sales") is False


def test_drop_query_is_rejected():
    assert validate_sql("DROP TABLE sales") is False


def test_multiple_statements_are_rejected():
    assert validate_sql("SELECT * FROM sales; DROP TABLE sales") is False


def test_empty_query_is_rejected():
    assert validate_sql("") is False


def test_query_with_nonexistent_column_raises_error():
    from src.database import execute_query

    try:
        execute_query("SELECT product_category FROM sales")
    except sqlite3.OperationalError:
        return

    assert False, "Expected an OperationalError for a nonexistent column"

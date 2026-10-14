
import sqlite3

from src.llm import generate_sql, summarize_results
from src.database import execute_query
from src.visualizer import create_sales_chart


def analyze_sales(question: str) -> dict:
    """Generate SQL, execute safely, summarize results, and create a chart."""

    try:
        sql = generate_sql(question)
        rows = execute_query(sql)
        summary = summarize_results(question, sql, rows)
        chart_path = create_sales_chart()

        return {
            "question": question,
            "sql": sql,
            "results": rows,
            "summary": summary,
            "chart_path": chart_path,
            "error": None,
        }

    except Exception as exc:
        return {
            "question": question,
            "sql": None,
            "results": [],
            "summary": None,
            "chart_path": None,
            "error": str(exc),
        }

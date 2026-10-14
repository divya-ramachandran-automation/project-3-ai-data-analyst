
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def generate_sql(question: str) -> str:
    """Generate a SQL query for a business question."""

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=(
            "You are a SQLite SQL assistant. Generate exactly one "
            "read-only SELECT query using only the sales table. "
            "The sales table has these columns: "
            "order_id (integer), order_date (date text), "
            "product (text), category (text), quantity (integer), "
            "unit_price (number), region (text). "
            "Use only these exact column names. Never invent columns. "
            "Calculate revenue as quantity * unit_price when needed. "
            "Return only SQL, with no Markdown formatting or explanation."
        ),
        input=question,
    )

    return response.output_text.strip()


def summarize_results(question: str, sql: str, results: list[tuple]) -> str:
    """Explain SQL query results in plain English."""

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=(
            "You are a business data analyst. Explain query results "
            "clearly and concisely. Use only the supplied results. "
            "Do not invent facts or claim trends that the data "
            "does not support."
        ),
        input=(
            f"Business question: {question}\n"
            f"SQL query: {sql}\n"
            f"Query results: {results}\n\n"
            "Explain what these results tell the business user."
        ),
    )

    return response.output_text.strip()


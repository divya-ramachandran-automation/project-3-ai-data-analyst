
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from pathlib import Path

from src.database import execute_query

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHART_DIR = PROJECT_ROOT / "charts"


def create_sales_chart() -> str:
    ""  "Create a bar chart of total sales revenue by category."""

    rows = execute_query(
        """
        SELECT category, SUM(quantity * unit_price) AS revenue
        FROM sales
        GROUP BY category
        ORDER BY revenue DESC
        """
    )

    categories = [row[0] for row in rows]
    revenues = [row[1] for row in rows]

    CHART_DIR.mkdir(exist_ok=True)

    chart_path = CHART_DIR / "sales_by_category.png"

    plt.figure(figsize=(8, 5))
    plt.bar(categories, revenues)
    plt.title("Sales Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue (INR)")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return str(chart_path)

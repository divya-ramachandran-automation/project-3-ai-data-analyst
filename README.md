# AI Data Analyst

An AI-powered data analysis application that converts natural-language business questions into SQL queries, executes them safely against a sales database, summarizes the results in plain English, and generates a sales visualization.

## Features

- **Natural Language to SQL:** Converts business questions into SQLite queries using an OpenAI model.
- **Safe Query Execution:** Validates SQL and uses a read-only database connection to prevent data modification.
- **AI-Powered Analysis:** Explains query results in clear, business-friendly language.
- **Data Visualization:** Generates a bar chart of sales revenue by category.
- **Automated Testing:** Includes tests for SQL validation and error handling.

## Tech Stack

- Python
- OpenAI API
- SQLite
- Pandas
- Matplotlib
- python-dotenv
- pytest

## Project Structure

```text
project-3-ai-data-analyst/
├── data/
│   └── sales.csv
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── database.py
│   ├── llm.py
│   ├── load_data.py
│   ├── sql_safety.py
│   └── visualizer.py
├── tests/
│   └── test_sql_safety.py
├── .env
├── .gitignore
└── README.md
```

The SQLite database is generated locally from `data/sales.csv`. Generated charts are saved in the `charts/` directory.

## Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install openai pandas python-dotenv matplotlib pytest
```

### 3. Configure the API key

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

Replace the placeholder with your own OpenAI API key. Never commit your real API key to GitHub.

### 4. Load the sales data

```powershell
python src/load_data.py
```

This creates `data/sales.db` and loads the sample sales records into the `sales` table.

### 5. Run the tests

```powershell
python -m pytest -v
```

## How It Works

1. The user asks a business question in natural language.
2. The OpenAI model generates a SQL query using the known sales-table schema.
3. The SQL safety validator checks the query.
4. The application executes the query through a read-only SQLite connection.
5. The model summarizes the query results.
6. Matplotlib generates a sales-revenue chart by category.

## Example Business Questions

- What is the total revenue by category?
- Which products are sold in each region?
- What is the total quantity sold by product?

Revenue is calculated as:

`quantity * unit_price`

## Security Notes

- Store API credentials in `.env`.
- Keep `.env` excluded from version control.
- Use SQL validation and a read-only database connection as layers of protection.
- The SQL validator is a basic safeguard, not a complete security boundary. Review and strengthen it before production use.

## Future Improvements

- Generate charts dynamically based on the user's question.
- Add more datasets and business metrics.
- Improve SQL validation and error reporting.
- Add a user interface for interactive analysis.
- Expand automated tests for API failures and unexpected queries.
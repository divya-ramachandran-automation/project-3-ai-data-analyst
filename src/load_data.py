
import sqlite3
import pandas as pd
from pathlib import Path

# Find the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define the CSV and database paths
csv_path = PROJECT_ROOT / "data" / "sales.csv"
db_path = PROJECT_ROOT / "data" / "sales.db"

# Load the sales data
df = pd.read_csv(csv_path)

# Create the SQLite database and table
with sqlite3.connect(db_path) as connection:
    df.to_sql("sales", connection, if_exists="replace", index=False)

print(f"Loaded {len(df)} sales records.")
print(f"Database created at: {db_path}")
print("Table created: sales")

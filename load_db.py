import pandas as pd
import sqlite3

df = pd.read_csv("edgar_raw.csv")

# Connect (creates the file if it doesn't exist)
conn = sqlite3.connect("financials.db")

# Write the raw data to a table
df.to_sql("raw_facts", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("Loaded into financials.db, table 'raw_facts'")
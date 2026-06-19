DoorDash Financial Analysis & Forecast Model

A SQL-driven financial analysis tool analyzing DoorDash and marketplace comps (Uber, Instacart) using public SEC EDGAR filings, with scenario-based Excel forecast modeling.

## Overview

This project demonstrates:
- **Data Engineering**: Python scripts to pull structured XBRL financial data from SEC EDGAR API
- **Data Cleaning**: SQLite database with SQL window functions and CTEs to deduplicate and clean raw filings data across multiple companies and reporting periods
- **Financial Analysis**: Comparative analysis of operating profitability inflection points and margin-expansion trajectories across three marketplace companies
- **Financial Modeling**: Scenario-based Excel forecast (Base, Conservative, Bull cases) with explicit assumptions and sensitivity analysis

## Key Finding

DoorDash reached net profitability in 2024 (+$123M net income) after years of losses, then inflected to its first full-year operating profit of $723M in 2025. Among the three comps, Uber reached operating profitability first (2023) and Instacart in 2024; DoorDash was last to cross into operating profit but shows the steepest margin-expansion trajectory, a ~$760M swing in operating income from 2024 to 2025. This suggests strong operational leverage from scale and marketplace efficiency gains. 

**Forward View:** If DoorDash sustains 2.5–5% operating margins through 2026–2027, operating income would run roughly $400–900M annually (Base case), comparable to Instacart's normalized profitability despite DoorDash's larger revenue base and greater exposure to delivery competition.

## Project Structure
doordash-financial-analysis/

├── pull_edgar.py                      # Fetch financial data from SEC EDGAR API

├── load_db.py                         # Load CSV data into SQLite

├── query_1_quarterly_revenue.sql      # Clean quarterly revenue by company

├── query_2_yoy_growth.sql             # Year-over-year growth analysis

├── query_3_operating_margin.sql       # Operating margin comparison

├── DoorDash_Financial_Analysis.xlsx   # Excel workbook with model and analysis

├── edgar_raw.csv                      # Raw XBRL facts from SEC EDGAR

├── operating_income_annual.csv        # Cleaned operating income data

├── net_income_annual.csv              # Cleaned net income data

└── README.md                          # This file

## How to Run

### 1. Pull data from SEC EDGAR
```bash
python pull_edgar.py
```
This fetches financial data for DoorDash, Uber, and Instacart from the SEC EDGAR API and saves to `edgar_raw.csv`.

**Requirements:** `requests`, `pandas`
```bash
pip install requests pandas
```

### 2. Load data into SQLite
```bash
python load_db.py
```
This creates `financials.db` with a `raw_facts` table containing all XBRL financial data.

**Requirements:** `sqlite3` (included with Python)

### 3. Run SQL queries
Open `financials.db` using **DB Browser for SQLite** (free download: sqlitebrowser.org):
- Click "Execute SQL" tab
- Copy queries from `.sql` files and run them
- Export results to CSV for analysis

Alternatively, use command line:
```bash
sqlite3 financials.db < query_1_quarterly_revenue.sql
```

### 4. Review Excel model
Open `DoorDash_Financial_Analysis.xlsx`:

| Sheet | Purpose |
|-------|---------|
| **Comp Table** | Side-by-side comparison of DoorDash, Uber, Instacart operating and net income (2023–2025) |
| **Forecast** | DoorDash 3-year forecast (2026–2028) with three scenarios and assumption-driven formulas |
| **Summary** | Key insight and drivers from the analysis |
| **Methodology** | Assumption justification and data sources |

## Data Source

All financial data sourced from **SEC EDGAR Company Facts API**:
- API: (https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- Companies: DoorDash (CIK 0001792789), Uber (CIK 0001543151), Instacart (CIK 0001579091)
- Filings: Form 10-K (annual reports), 2023–2025
- Data retrieved: June 2026

See Methodology sheet in Excel for full data source citations.

## Tools & Dependencies

| Tool | Purpose | Install |
|------|---------|---------|
| Python 3.8+ | Data pipeline | python.org |
| pandas | Data manipulation | `pip install pandas` |
| requests | HTTP requests to SEC API | `pip install requests` |
| SQLite 3 | Database | Built into Python |
| DB Browser for SQLite | Query visualization | sqlitebrowser.org |
| Excel / Google Sheets | Financial modeling | N/A |

## Key Insights from Analysis

1. **Profitability Inflection**: DoorDash's path to profitability was delayed vs. Uber and Instacart, but the margin expansion trajectory is steepest ($760M swing YoY).

2. **Operational Leverage**: The inflection from -$38M operating income (2024) to +$723M (2025) reflects scale benefits and take-rate optimization, not just revenue growth.

3. **Forward Outlook**: Base case forecast ($400–900M operating income 2026–2027) is achievable if margins expand 2.5–5% annually, driven by advertising revenue, take-rate optimization, and improved unit economics.

4. **Competitive Positioning**: Despite higher delivery competition exposure vs. Uber, DoorDash's normalized profitability (Base case) is comparable to Instacart's, suggesting a defensible market position.

## Author

**Karsten Latunde**  
UC Berkeley, Economics Major | Class of 2026  
[LinkedIn](https://www.linkedin.com/in/karstenlatunde/)

---

*Last updated: June 2026*

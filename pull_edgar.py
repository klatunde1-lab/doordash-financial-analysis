import requests
import pandas as pd

# SEC requires a User-Agent identifying you — use your real name/email
HEADERS = {"User-Agent": "Karsten Latunde klatunde1@berkeley.edu"}

# The companies we're analyzing, with their CIKs (zero-padded to 10 digits)
COMPANIES = {
    "DoorDash": "0001792789",
    "Uber":     "0001543151",
    "Instacart":"0001579091",
}

# The XBRL "concepts" (line items) we want to pull.
# These are the standardized US-GAAP tags companies report under.
CONCEPTS = {
    "Revenues": "Revenues",
    "CostOfRevenue": "CostOfRevenue",
    "OperatingIncomeLoss": "OperatingIncomeLoss",
    "NetIncomeLoss": "NetIncomeLoss",
    "ResearchAndDevelopmentExpense": "ResearchAndDevelopmentExpense",
}

def pull_company(name, cik):
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    rows = []
    facts = data.get("facts", {}).get("us-gaap", {})
    for concept_key, concept_tag in CONCEPTS.items():
        if concept_tag not in facts:
            continue
        # Each concept reports values in units (usually USD)
        units = facts[concept_tag]["units"]
        for unit_type, entries in units.items():
            for e in entries:
                rows.append({
                    "company": name,
                    "concept": concept_key,
                    "value": e.get("val"),
                    "start": e.get("start"),
                    "end": e.get("end"),
                    "fiscal_year": e.get("fy"),
                    "fiscal_period": e.get("fp"),
                    "form": e.get("form"),  # 10-K, 10-Q, etc.
                    "filed": e.get("filed"),
                })
    return rows

all_rows = []
for name, cik in COMPANIES.items():
    print(f"Pulling {name}...")
    all_rows.extend(pull_company(name, cik))

df = pd.DataFrame(all_rows)
df.to_csv("edgar_raw.csv", index=False)
print(f"Saved {len(df)} rows to edgar_raw.csv")
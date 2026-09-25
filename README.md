# India Green Bond Trend Analysis

An end-to-end data analytics project examining green bond issuance trends in India (2017–2026), using SQL, Python, and Power BI.

## Project Overview

This project analyzes 60 SEBI-registered green bond records (33 unique issuances after removing double-counted maturity tranches) to understand how India's green bond market has evolved: issuance volume, issuer composition, coupon pricing, and market processing efficiency.

**Key question:** Is India's green bond market growing broadly, or is growth concentrated among a small number of large issuers?

## Key Findings

- **Total volume raised:** ₹21,578.59 Cr across 33 unique issuances (2017–2026)
- **Concentration:** the top 5 issuers account for 66.3% of total volume raised
- **Growth pattern:** issuance volume accelerated sharply in 2025–2026, driven in large part by a single ₹10,000 Cr bank issuance
- **Pricing:** coupon rates tracked India's prevailing interest-rate cycle more closely than any green-bond-specific factor (weak tenure–coupon correlation, ~0.27)
- **Market maturity:** average listing lag (issuance to exchange listing) fell from ~16 days in 2019 to 1–3 days by 2024–2026

## Tech

| Tool | Role |
|---|---|
| **MySQL** | Data storage, table creation, SQL aggregation and join queries |
| **Python** (Pandas, NumPy, Matplotlib, Seaborn) | Data cleaning, feature engineering, exploratory data analysis, visualization |
| **SQLAlchemy** | Python-to-MySQL database connection |
| **Power BI** (DAX) | Interactive dashboard for business-facing reporting |

## Project Structure

```
Green_bonds_trend_analysis_project/
├── data/
│   ├── raw/                     # Original SEBI dataset
│   └── processed/                # Cleaned dataset
├── notebooks/
│   ├── db_connection.py          # MySQL connection script (SQLAlchemy)
│   └── green_bond_analysis.ipynb # Data loading, cleaning, EDA, and visualization
├── sql/
│   └── green_bonds_queries.sql   # Table creation, joins, and aggregation queries
├── Dashboard/
│   └── *.pbix                    # Power BI dashboard
├── research papers/
│   ├── Research_Paper_1(Topic_Related).docx
│   └── Research_Paper_2(Technology_Related).docx
├── outputs/                      # Exported cleaned data, charts
├── requirements.txt
└── README.md
```

## Dataset

**Source:** SEBI-registered green bond issuance records
**Fields:** Issuer, Issuer Type, ESG Category, Issuance/Listing/Maturity Dates, Amount Raised (₹ Cr), Coupon Rate (%), Tenure (Years), ISIN

**Note on data quality:** several issuances are structured as *serial bonds* — a single issuance split across multiple maturity tranches, each recorded as a separate row with the same `Sr_No`. A `Unique_Issuance_Row` flag is used throughout this project to prevent double-counting volume in these cases.

## Setup Instructions

1. **Clone/download this project folder.**

2. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database:**
   - Open `sql/green_bonds_queries.sql` in MySQL Workbench
   - Run the database and table creation statements (Section 1)
   - Import the cleaned dataset (`data/processed/`) into the `green_bond_trend_analysis` table

5. **Configure the database connection:**
   - Open `notebooks/db_connection.py`
   - Update `DB_CONFIG` with your MySQL password and database name

6. **Run the analysis notebook:**
   - Open `notebooks/green_bond_analysis.ipynb`
   - Run all cells (loads data from MySQL → cleans → analyzes → visualizes → exports)

7. **Open the Power BI dashboard:**
   - Open the `.pbix` file in the `Dashboard/` folder
   - Refresh the data source if needed to reconnect to your local MySQL instance

## Data Cleaning Notes

- Missing `Coupon_Percent` values filled with the column median
- Issuer name artifacts (stray characters) removed
- `ESG_Category` spelling standardized (e.g., "Sustainability linked" → "Sustainability-Linked")
- Boolean-style columns (`Is_Serial_Tranche`, `Unique_Issuance_Row`) converted from MySQL's text storage back to proper booleans in Python

## Research Papers

This project includes two supporting research papers:
1. **Topic-Related Research** — background on India's green bond market, regulatory evolution (SEBI/RBI), and the academic "greenium" literature
2. **Technology-Related Research** — explanation of the SQL, Python, and Power BI tools used in this project's pipeline

## Author

[Your Name]
[Submission Date]

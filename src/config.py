import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

RAW_DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "green_bond_trend_analysis.csv"
)
PROCESSED_DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "india_green_bonds_cleaned.csv"
)
GRAPH_DATA = os.path.join(
    BASE_DIR,
    "outputs",
    "graphs"
)
ANALYSIS_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "analysis",
    "business_insights.txt"
)
REPORT_PATH = os.path.join(
    BASE_DIR,
    "outputs",
    "reports",
    "Green_Bonds_EDA_Report.pdf"
)
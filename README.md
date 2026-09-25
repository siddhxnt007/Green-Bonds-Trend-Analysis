# GREEN BONDS TREND ANALYSIS

## 1. Project Overview

Green Bonds Trend Analysis is a data analytics project that analyzes SEBI-registered green bond issuance data to understand market trends, issuer behavior, and pricing patterns in India's green bond market.

The project uses Python, Pandas, NumPy, Matplotlib, Seaborn, MySQL, SQL, and Power BI.

The analysis focuses on issuance volume based on issuer type, ESG category, coupon rate, tenure, and yearly trends.

---

## 2. Objectives

The main objectives of this project are:

* Analyze SEBI-registered green bond issuance data.
* Clean and preprocess the raw dataset.
* Perform exploratory data analysis (EDA).
* Analyze issuance volume by issuer type.
* Analyze issuance volume by ESG category.
* Analyze issuance volume by coupon category.
* Analyze issuance volume by year.
* Analyze coupon rate and tenure trends.
* Perform SQL-based analysis.
* Create visualizations using Python.
* Create an interactive Power BI dashboard.
* Generate useful business insights.

---

## 3. Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* MySQL
* SQL
* Power BI
* Jupyter Notebook

---

## 4. Project Workflow

Raw Dataset
↓
Data Cleaning
↓
Cleaned Dataset
↓
Exploratory Data Analysis
↓
Data Visualization
↓
MySQL / SQL Analysis
↓
Power BI Dashboard
↓
Business Insights

---

## 5. Dataset

The project contains two datasets:

### Raw Dataset

`SEBI_Green_Bonds_ESG_Dataset.csv`

This is the original green bond issuance dataset used as the starting point of the project.

### Cleaned Dataset

`india_green_bonds_cleaned.csv`

This dataset is prepared after data cleaning and preprocessing and is used for further analysis.

---

## 6. Data Cleaning

The dataset is checked and prepared before performing analysis.

The cleaning process includes:

* Checking missing values
* Checking duplicate records
* Correcting inconsistent values (e.g., ESG category spelling, issuer name artifacts)
* Standardizing data (e.g., converting MySQL's text-based True/False columns to real booleans)
* Checking data types
* Preparing the cleaned dataset for analysis

---

## 7. Exploratory Data Analysis

EDA is performed using Python and Pandas to understand the green bond issuance data.

The analysis includes:

* Total amount raised
* Number of unique issuances
* Average coupon rate
* Average tenure
* Issuance volume by issuer type
* Issuance volume by ESG category
* Issuance volume by coupon category
* Yearly issuance trends

---

## 8. Data Visualization

Matplotlib and Seaborn are used to create different visualizations.

The project includes visual analysis such as:

* Amount Raised by ESG Category
* Amount Raised by Coupon Category
* Monthly Amount Raised
* Issuance Count by Issuer Type
* Distribution of Bond Tenure
* Box Plot of Amount Raised
* Tenure vs Coupon Rate Scatter Plot
* Correlation Heatmap
* Pair Plot

Different chart types are used to make the issuance patterns easier to understand.

---

## 9. SQL Analysis

SQL is used to analyze the green bond issuance data using MySQL.

The SQL file contains queries for analyzing:

* Total volume raised per year
* Number of issuances per year
* Volume by issuer type
* Top issuers by amount raised
* Average coupon rate by year
* Average tenure by issuer type
* Average listing lag by year
* ESG category split
* Serial (multi-tranche) bond identification
* Year-over-year growth

The SQL analysis provides another way to examine and verify the issuance data.

---

## 10. Python MySQL Connection

The file:

`db_connection.py`

is used for working with the green bond data and MySQL database connection.

It connects the Python analysis workflow with the database for SQL-based analysis.

---

## 11. Power BI Dashboard

The Power BI dashboard is created using the cleaned green bond dataset.

File:

`Green_Bonds_Trend_Analysis.pbix`

The dashboard presents important issuance information using KPI cards, charts, and slicers.

### KPI Cards

The dashboard includes:

* Total Issuances
* Total Amount Raised
* Average Coupon Rate
* Average Tenure
* Green Bond Count
* Average Listing Lag
* YoY Volume Growth %

### Dashboard Analysis

The dashboard contains visualizations for:

* Issuances by Issuer Type
* Issuances by Coupon Category
* ESG Category Distribution
* Issuer Type vs ESG Category
* Amount Raised by Issuance Year
* Average Coupon Rate by Issuer Type

### Slicers

The dashboard can be filtered using:

* Issuer Type
* ESG Category
* Issuance Year

---

## 12. Research Papers

The project contains two research papers:

* `Research_Paper_1_Topic_Related.docx`
* `Research_Paper_2_Technology_Related.docx`

These papers provide supporting information related to the project topic and technologies used.

---

## 13. Project Structure

```text
Green_bonds_trend_analysis_project/
│
├── data/
│   ├── raw/
│   │   └── SEBI_Green_Bonds_ESG_Dataset.csv
│   └── processed/
│       └── india_green_bonds_cleaned.csv
│
├── notebooks/
│   ├── db_connection.py
│   └── green_bond_analysis.ipynb
│
├── sql/
│   └── green_bonds_queries.sql
│
├── Dashboard/
│   └── Green_Bonds_Trend_Analysis.pbix
│
├── research papers/
│   ├── Research_Paper_1_Topic_Related.docx
│   └── Research_Paper_2_Technology_Related.docx
│
├── README.md
└── requirements.txt
```

---

## 14. Requirements

The Python libraries required for the project are listed in:

`requirements.txt`

Install the required libraries before running the Python or Jupyter Notebook files.

---

## 15. Conclusion

This project demonstrates a complete beginner-level data analytics workflow, starting from raw SEBI green bond issuance data and progressing through data cleaning, exploratory analysis, visualization, SQL analysis, and Power BI dashboard development.

The project helps understand India's green bond issuance patterns and presents the analysis in a simple and interactive form.

---

##

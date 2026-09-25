CREATE DATABASE Green_bond_analysis_db;
USE Green_bond_analysis_db;

CREATE TABLE IF NOT EXISTS green_bond_trend_analysis (
    Sr_No               INT,
    Issuer              VARCHAR(255),
    Issuer_Type         VARCHAR(100),
    ESG_Category         VARCHAR(50),
    Issuance_Date        DATE,
    Issuance_Year        INT,
    Listing_Date         DATE,
    Listing_Lag_Days     INT,
    Maturity_Date        DATE,
    Tenure_Years          DECIMAL(5,2),
    Amount_Raised_Cr     DECIMAL(12,2),
    Coupon_Percent       DECIMAL(5,2),
    Is_Serial_Tranche    VARCHAR(10),
    Unique_Issuance_Row  VARCHAR(10),
    ISIN                VARCHAR(20)
);

SELECT * FROM Green_bond_analysis_db.green_bond_trend_analysis;

-- Reference table to enrich issuer type with a risk profile (enables JOINs)
CREATE TABLE IF NOT EXISTS issuer_type_reference (
    Issuer_Type   VARCHAR(100) PRIMARY KEY,
    Risk_Profile   VARCHAR(50),
    Description    VARCHAR(255)
);
 
INSERT INTO issuer_type_reference (Issuer_Type, Risk_Profile, Description) VALUES
    ('Municipal/Urban Local Body', 'Moderate', 'Local government bodies funding urban infrastructure'),
    ('Public/Listed Company', 'Moderate', 'Publicly listed corporates raising green capital'),
    ('Private Company', 'Higher', 'Privately held corporates, typically less liquid'),
    ('Government/PSU Agency', 'Low', 'State-backed agencies with implicit government support'),
    ('Bank/Financial Institution', 'Low', 'Regulated banks issuing green debt'),
    ('REIT/Real Estate Trust', 'Moderate', 'Real estate investment trusts funding green properties'),
    ('Other', 'Unclassified', 'Issuers not matching a defined category');
    
SELECT * FROM Green_bond_analysis_db.issuer_type_reference;

-- 2. DATA EXTRACTION / VERIFICATION

SELECT COUNT(*) AS total_rows FROM green_bond_trend_analysis;
 
SELECT * FROM green_bond_trend_analysis LIMIT 10;

SELECT DISTINCT Unique_Issuance_Row FROM green_bond_trend_analysis;
SELECT DISTINCT Is_Serial_Tranche FROM green_bond_trend_analysis;
SELECT DISTINCT ESG_Category FROM green_bond_trend_analysis;
SELECT DISTINCT Issuer_Type FROM green_bond_trend_analysis;

-- 3. JOIN QUERIES (green_bond_trend_analysis + issuer_type_reference)

-- 1. Total volume raised by issuer type, with risk profile shown
SELECT
    r.Issuer_Type,
    r.Risk_Profile,
    SUM(g.Amount_Raised_Cr) AS Total_Volume_Cr,
    COUNT(*) AS Num_Issuances
FROM green_bond_trend_analysis g
JOIN issuer_type_reference r
    ON g.Issuer_Type = r.Issuer_Type
WHERE g.Unique_Issuance_Row = 'True'
GROUP BY r.Issuer_Type, r.Risk_Profile
ORDER BY Total_Volume_Cr DESC;
 
-- 2. Average coupon rate by risk profile category
SELECT
    r.Risk_Profile,
    ROUND(AVG(g.Coupon_Percent), 2) AS Avg_Coupon
FROM green_bond_trend_analysis g
JOIN issuer_type_reference r
    ON g.Issuer_Type = r.Issuer_Type
WHERE g.Unique_Issuance_Row = 'True'
GROUP BY r.Risk_Profile
ORDER BY Avg_Coupon DESC;
 
-- 3. Number of issuances by risk profile
SELECT
    r.Risk_Profile,
    COUNT(*) AS Num_Issuances
FROM green_bond_trend_analysis g
JOIN issuer_type_reference r
    ON g.Issuer_Type = r.Issuer_Type
WHERE g.Unique_Issuance_Row = 'True'
GROUP BY r.Risk_Profile
ORDER BY Num_Issuances DESC;


-- 4. AGGREGATION QUERIES

-- 1. Total volume raised per year
SELECT Issuance_Year, SUM(Amount_Raised_Cr) AS Total_Volume_Cr
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuance_Year
ORDER BY Issuance_Year;

SELECT DISTINCT Unique_Issuance_Row FROM green_bond_trend_analysis;

-- 2. Number of issuances per year
SELECT Issuance_Year, COUNT(*) AS Num_Issuances
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuance_Year
ORDER BY Issuance_Year;

-- 3. Volume by issuer type
SELECT Issuer_Type, SUM(Amount_Raised_Cr) AS Total_Volume_Cr, COUNT(*) AS Num_Issuances
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuer_Type
ORDER BY Total_Volume_Cr DESC;

-- 4. Top 5 issuers by total amount raised
SELECT Issuer, SUM(Amount_Raised_Cr) AS Total_Raised_Cr
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuer
ORDER BY Total_Raised_Cr DESC
LIMIT 5;

-- 5. Average coupon rate by year
SELECT Issuance_Year, ROUND(AVG(Coupon_Percent),2) AS Avg_Coupon
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuance_Year
ORDER BY Issuance_Year;

-- 6. Average tenure by issuer type
SELECT Issuer_Type, ROUND(AVG(Tenure_Years),2) AS Avg_Tenure_Years
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuer_Type
ORDER BY Avg_Tenure_Years DESC;

-- 7. Average listing lag (days) by year
SELECT Issuance_Year, ROUND(AVG(Listing_Lag_Days),1) AS Avg_Listing_Lag_Days
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuance_Year
ORDER BY Issuance_Year;

-- 8. ESG category split
SELECT ESG_Category, COUNT(*) AS Num_Issuances, SUM(Amount_Raised_Cr) AS Total_Volume_Cr
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY ESG_Category;

-- 9. Identify serial (multi-tranche) bonds
SELECT Sr_No, Issuer, COUNT(*) AS Num_Tranches
FROM green_bond_trend_analysis
WHERE Is_Serial_Tranche = 'True'
GROUP BY Sr_No, Issuer
ORDER BY Num_Tranches DESC;

-- 10. Year-over-year growth %
WITH yearly AS (
  SELECT Issuance_Year, SUM(Amount_Raised_Cr) AS Volume
  FROM green_bond_trend_analysis
  WHERE Unique_Issuance_Row = 'True'
  GROUP BY Issuance_Year
)
SELECT Issuance_Year, Volume,
  ROUND(100.0*(Volume - LAG(Volume) OVER (ORDER BY Issuance_Year)) 
        / LAG(Volume) OVER (ORDER BY Issuance_Year), 1) AS YoY_Growth_Pct
FROM yearly
ORDER BY Issuance_Year;

-- 11. Largest single issuance
SELECT Issuer, Issuance_Date, Amount_Raised_Cr, Coupon_Percent
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
ORDER BY Amount_Raised_Cr DESC
LIMIT 1;


-- Q12: Bonds where the listing lag was longer than average (finds outlier delays)
SELECT Issuer, Issuance_Year, Listing_Lag_Days
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
    AND Listing_Lag_Days > (
        SELECT AVG(Listing_Lag_Days)
        FROM green_bond_trend_analysis
        WHERE Unique_Issuance_Row = 'True'
    )
ORDER BY Listing_Lag_Days DESC;
 
-- Q13: Which issuer types average more than 5 years tenure?
SELECT Issuer_Type, ROUND(AVG(Tenure_Years), 2) AS Avg_Tenure_Years
FROM green_bond_trend_analysis
WHERE Unique_Issuance_Row = 'True'
GROUP BY Issuer_Type
HAVING AVG(Tenure_Years) > 5;
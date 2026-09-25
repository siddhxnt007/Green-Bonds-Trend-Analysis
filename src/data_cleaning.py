import pandas as pd
from src.config import PROCESSED_DATA_PATH

def clean_data(df):
    df = df.copy()


    # Remove duplicates
    df = df.drop_duplicates()


    # clean text columns
    text_columns = [
        "Issuer",
        "ISIN",
        "ESG_Category"
    ]

    for column in text_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
        )

    # Remove stray characters from issuer names
    df["Issuer"] = df["Issuer"].str.replace("*", "", regex=False)

    # Standardize ESG_Category labels
    df["ESG_Category"] = df["ESG_Category"].replace({
        "Sustainability linked": "Sustainability-Linked",
        "Sustainability-linked": "Sustainability-Linked",
    })

    # Date Conversion
    df["Issuance_Date"] = pd.to_datetime(
        df["Issuance_Date"],
        errors="coerce"
    )

    df["Maturity_Date"] = pd.to_datetime(
        df["Maturity_Date"],
        errors="coerce"
    )

    df["Listing_Date"] = pd.to_datetime(
        df["Listing_Date"],
        errors="coerce"
    )

    # Numeric Conversion

    numeric_columns = [
        "Amount_Raised_Cr",
        "Coupon_Percent",
        "Tenure_Years"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


    # Missing Values
    df["Amount_Raised_Cr"] = df["Amount_Raised_Cr"].fillna(
        df["Amount_Raised_Cr"].median()
    )

    df["Coupon_Percent"] = df["Coupon_Percent"].fillna(
        df["Coupon_Percent"].median()
    )

    df["Tenure_Years"] = df["Tenure_Years"].fillna(
        df["Tenure_Years"].median()
    )

    # Remove invalid data

    # Amount_Raised_Cr
    df = df[
        df["Amount_Raised_Cr"] > 0
    ]

    # Coupon_Percent
    df = df[
        df["Coupon_Percent"] > 0
    ]

    # Tenure_Years
    df = df[
        df["Tenure_Years"] > 0
    ]

    # Issuance_Date must be valid
    df = df.dropna(
        subset=["Issuance_Date"]
    )

    # Reset Index
    df = df.reset_index(
        drop=True
    )

    return df

def save_cleaned_data(df):
    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )
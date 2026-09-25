import pandas as pd


def generate_analysis(df):

    analysis = {}

    # Use only unique issuances for amount-based totals (serial bonds repeat
    # the same Amount_Raised_Cr across multiple maturity tranches)
    vol_df = df[df["Unique_Issuance_Row"]]

    # Overall Business Metrics
    analysis["Total Issuances"] = vol_df.shape[0]

    analysis["Total Amount Raised (Cr)"] = vol_df["Amount_Raised_Cr"].sum()

    analysis["Average Coupon Rate (%)"] = df["Coupon_Percent"].mean()

    analysis["Average Tenure (Years)"] = df["Tenure_Years"].mean()

    analysis["Average Amount Raised per Issuance (Cr)"] = vol_df["Amount_Raised_Cr"].mean()

    analysis["Average Listing Lag (Days)"] = vol_df["Listing_Lag_Days"].mean()


    # Issuer Type Analysis
    issuer_type_volume = (
        vol_df.groupby("Issuer_Type")["Amount_Raised_Cr"]
        .sum()
        .sort_values(ascending=False)
    )

    analysis["Best Issuer Type"] = issuer_type_volume.index[0]


    # Year Analysis
    year_volume = (
        vol_df.groupby("Issuance_Year")["Amount_Raised_Cr"]
        .sum()
        .sort_values(ascending=False)
    )

    analysis["Best Issuance Year"] = int(year_volume.index[0])


    # ESG Category Analysis
    esg_volume = (
        vol_df.groupby("ESG_Category")["Amount_Raised_Cr"]
        .sum()
        .sort_values(ascending=False)
    )

    analysis["Most Common ESG Category"] = (
        df["ESG_Category"].mode()[0]
    )


    # Tranche Structure Analysis
    tranche_count = (
        df["Is_Serial_Tranche"].value_counts()
    )

    analysis["Most Common Tranche Type"] = (
        "Serial Tranche" if tranche_count.index[0] else "Single Tranche"
    )


    # Issuer Analysis
    issuer_totals = (
        vol_df.groupby("Issuer")["Amount_Raised_Cr"]
        .sum()
        .sort_values(ascending=False)
    )


    # Top Issuer
    analysis["Top Issuer"] = (
        issuer_totals.index[0]
    )

    return analysis


def save_business_insights(analysis, file_path):

    with open(file_path, "w", encoding="utf-8") as file:

        for key, value in analysis.items():

            if isinstance(value, float):
                value = round(value, 2)

            file.write(
                f"{key}: {value}\n"
            )
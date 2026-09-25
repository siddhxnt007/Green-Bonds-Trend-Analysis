def transform_data(df):

    # Total interest cost over the bond's full tenure
    df["Total_Interest_Cost_Cr"] = (
        df["Amount_Raised_Cr"]
        * (df["Coupon_Percent"]/100)
        * df["Tenure_Years"]
    )

    # Annual interest outgo
    df["Annual_Interest_Cost_Cr"] = (
        df["Amount_Raised_Cr"] * (df["Coupon_Percent"]/100)
    )

    # Interest-to-Principal Ratio (total interest as % of amount raised)
    df["Interest_To_Principal_Ratio"] = (
        df["Total_Interest_Cost_Cr"] / df["Amount_Raised_Cr"].replace(0,1)*100

    )


    # Year
    df["Issuance_Year"] = (df["Issuance_Date"].dt.year)

    # Month
    df["Issuance_Month"] = (df["Issuance_Date"].dt.month)

    # Month Name
    df["Issuance_Month_Name"] = (
        df["Issuance_Date"].dt.month_name()
    )

    # Quarter
    df["Issuance_Quarter"] = (
        df["Issuance_Date"].dt.quarter
    )

    # Coupon Category
    df["Coupon_Category"]=(
        df["Coupon_Percent"].apply(
            classify_coupon
            )
    )
    return df

def classify_coupon(coupon):
    if coupon <= 7:

        return "Low Coupon"

    elif coupon <= 8.5:
        return "Medium Coupon"

    else:
        return "High Coupon"
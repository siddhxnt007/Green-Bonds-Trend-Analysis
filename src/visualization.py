import os
import matplotlib.pyplot as plt
import seaborn as sns


def create_visualization(df, output_path):

    os.makedirs(
        output_path,
        exist_ok=True
    )

    # Amount Raised by ESG Category
    esg_amount = (
        df.groupby("ESG_Category")["Amount_Raised_Cr"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))

    esg_amount.plot(kind="bar")

    plt.title("Amount Raised by ESG Category")
    plt.xlabel("ESG Category")
    plt.ylabel("Amount Raised (Cr)")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_path,
            "amount_by_esg_category.png"
        )
    )

    plt.close()


    # Amount Raised by Coupon Category
    coupon_amount = (
        df.groupby("Coupon_Category")["Amount_Raised_Cr"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))

    coupon_amount.plot(
        kind="bar"
    )

    plt.title("Amount Raised by Coupon Category")
    plt.xlabel("Coupon Category")
    plt.ylabel("Amount Raised (Cr)")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_path,
            "amount_by_coupon_category.png"
        )
    )

    plt.close()


    # Monthly Amount Raised
    monthly_amount = (
        df.groupby("Issuance_Month_Name")["Amount_Raised_Cr"]
        .sum()
    )

    plt.figure(figsize=(10, 5))

    monthly_amount.plot(
        kind="line",
        marker="o"
    )

    plt.title("Monthly Amount Raised")
    plt.xlabel("Month")
    plt.ylabel("Amount Raised (Cr)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_path,
            "monthly_amount_raised.png"
        )
    )

    plt.close()


    # Coupon Category Distribution
    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=df,
        x="Coupon_Category"
    )

    plt.title("Coupon Category Distribution")
    plt.xlabel("Coupon Category")
    plt.ylabel("Number of Issuances")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_path,
            "coupon_category_distribution.png"
        )
    )

    plt.close()


    # Issuance Quarter
    quarter_count = (
        df["Issuance_Quarter"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(7, 5))

    quarter_count.plot(
        kind="bar"
    )

    plt.title("Issuances by Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Number of Issuances")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_path,
            "issuance_quarter.png"
        )
    )

    plt.close()


    # Total Interest Cost by ESG Category
    esg_interest = (
        df.groupby("ESG_Category")["Total_Interest_Cost_Cr"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))

    esg_interest.plot(
        kind="bar"
    )

    plt.title("Total Interest Cost by ESG Category")
    plt.xlabel("ESG Category")
    plt.ylabel("Total Interest Cost (Cr)")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_path,
            "interest_cost_by_esg_category.png"
        )
    )

    plt.close()


    # Coupon vs Annual Interest Cost
    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Coupon_Percent",
        y="Annual_Interest_Cost_Cr"
    )

    plt.title("Coupon Rate vs Annual Interest Cost")
    plt.xlabel("Coupon (%)")
    plt.ylabel("Annual Interest Cost (Cr)")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_path,
            "coupon_vs_interest_cost.png"
        )
    )

    plt.close()
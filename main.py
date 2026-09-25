import os

from src.config import (
    PROCESSED_DATA_PATH,
    GRAPH_DATA,
    ANALYSIS_PATH,
    REPORT_PATH
)

from src.data_loader import (
    load_data
)

from src.data_cleaning import (
    clean_data,
    save_cleaned_data
)

from src.data_transformation import (
    transform_data
)

from src.analysis import (
    generate_analysis,
    save_business_insights
)

from src.visualization import (
    create_visualization
)

from src.report import (
    create_report
)


def main():

    print("Loading data...")

    df = load_data()


    print("Cleaning data...")

    df = clean_data(df)

    save_cleaned_data(
        df
    )


    print("Transforming data...")

    df = transform_data(
        df
    )


    print("Generating analysis...")

    analysis = generate_analysis(
        df
    )


    print("Saving business insights...")

    os.makedirs(
        os.path.dirname(
            ANALYSIS_PATH
        ),
        exist_ok=True
    )

    save_business_insights(
        analysis,
        ANALYSIS_PATH
    )


    print("Creating visualization...")

    create_visualization(
        df,
        GRAPH_DATA
    )


    print("Creating PDF Report...")

    os.makedirs(
        os.path.dirname(
            REPORT_PATH
        ),
        exist_ok=True
    )

    # CREATE PDF REPORT
    create_report(
        analysis,
        REPORT_PATH
    )


    print(
        "\nIndia Green Bond Trend Analysis Completed Successfully"
    )


if __name__ == "__main__":
    main()
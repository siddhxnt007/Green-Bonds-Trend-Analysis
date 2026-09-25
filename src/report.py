from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_report(
        analysis,
        report_path
):
    document = SimpleDocTemplate(
        report_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(
        Paragraph(
            "India Green Bond Trend Analysis Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # Business Insights
    story.append(
        Paragraph(
            "Business Insights",
            styles["Heading2"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    # Add analysis
    for key, value in analysis.items():

        if isinstance(value, float):
            value = round(value, 2)

        text = (
            f"<b>{key}:</b> {value}"
        )

        story.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

        story.append(
            Spacer(1, 8)
        )

    # Build PDF
    document.build(story)

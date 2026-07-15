from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
import datetime


def generate_report(result, disease_info, output_path):

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER
    title.textColor = HexColor("#1E88E5")

    heading = styles["Heading2"]

    body = styles["BodyText"]

    doc = SimpleDocTemplate(output_path)

    story = []

    story.append(Paragraph("BrainInsight AI", title))
    story.append(Paragraph("Intelligent Multi-Class Brain Disease Detection", body))

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Date:</b> {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}",
            body
        )
    )

    story.append(Spacer(1,20))

    story.append(Paragraph("Diagnosis Result", heading))

    story.append(
        Paragraph(
            f"<b>Prediction:</b> {result['prediction']}",
            body
        )
    )

    story.append(
        Paragraph(
            f"<b>Confidence:</b> {result['confidence']:.2f}%",
            body
        )
    )

    story.append(Spacer(1,20))

    story.append(Paragraph("Prediction Probabilities", heading))

    for disease, prob in result["probabilities"].items():

        story.append(
            Paragraph(
                f"{disease} : {prob:.2f}%",
                body
            )
        )

    story.append(Spacer(1,20))

    story.append(Paragraph("Disease Overview", heading))

    story.append(
        Paragraph(
            disease_info["overview"],
            body
        )
    )

    story.append(Spacer(1,20))

    story.append(Paragraph("General Treatment", heading))

    story.append(
        Paragraph(
            disease_info["treatment"],
            body
        )
    )

    story.append(Spacer(1,30))

    story.append(Paragraph("Medical Disclaimer", heading))

    story.append(
        Paragraph(
            "BrainInsight AI is intended only as an AI-assisted screening tool and must not replace professional medical diagnosis.",
            body
        )
    )

    doc.build(story)
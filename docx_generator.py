from docx import Document
from docx.shared import Pt
from datetime import datetime


def generate_docx(report_text: str, output_path: str):
    """
    Generate a DOCX file from the generated report text.
    """

    document = Document()

    # Base style
    style = document.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)

    lines = report_text.split("\n")

    for line in lines:
        if line.strip() == "":
            document.add_paragraph("")
            continue

        # Headings
        if line.isupper():
            p = document.add_paragraph(line)
            p.runs[0].bold = True
            p.alignment = 1  # center
        else:
            document.add_paragraph(line)

    document.save(output_path)

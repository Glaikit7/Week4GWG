#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    title = Paragraph(title, styles["h1"])
    paragraph = Paragraph(paragraph, styles["BodyText"])
    emp_line = Spacer(1, 20)
    report.build([title, emp_line, paragraph, emp_line])
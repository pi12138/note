# -*- coding: UTF-8 -*-
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import time


doc = SimpleDocTemplate("./file/form_letter.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

story = list()

logo = "./image/python.png"
mag_name = "Pythonista"
issue_num = 12 
sub_price = "99.00"
limited_date = '03/05/2010'
free_gift = "tin foil hat"
formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ['411 State St.', 'Marshalltown, IA 50158']
im = Image(logo, 2*inch, 2*inch)

story.append(im)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))

ptext = '<font size=12>{}</font>'.format(formatted_time)
story.append(Paragraph(ptext, styles['Normal']))
story.append(Spacer(1, 12))

ptext = '<font size=12>{}</font>'.format(full_name)
story.append(Paragraph(ptext, styles['Normal']))

for part in address_parts:
    ptext = '<font size=12>{}</font>'.format(part.strip())
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))

ptext = '<font size=12>Dear: {}</font>'.format(full_name.split()[0].strip())
story.append(Paragraph(ptext, styles['Normal']))
story.append(Spacer(1, 12))

ptext = '<font size=12>{}</font>'.format(mag_name)
story.append(Paragraph(ptext, styles['Justify']))
story.append(Spacer(1, 12))

story.append(Paragraph("导出PDF", styles['Normal']))
# story.append()

doc.build(story)
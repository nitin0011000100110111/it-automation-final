#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,20)
  paragraph = Paragraph(paragraph)
  return report.build([report_title, empty_line, paragraph])

# filename = '/tmp/processed.pdf'
# title = "Processed Update on {}".format(format(datetime.now(), "%B %d, %Y"))
# data = gen_json('./supplier-data/descriptions/')
# additional_info = gen_additional_info(data)
# generate_report(filename, title, additional_info)


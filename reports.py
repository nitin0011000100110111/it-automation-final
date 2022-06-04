#!/usr/bin/env python3

from run import gen_json
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def gen_additional_info(data):
    additional_info = ""
    for item in data:
        additional_info += f"name: {item['name']}<br/><br/>weight: {item['weight']} lbs<br/><br/>"
    return additional_info

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,20)
  additional_info = Paragraph(additional_info)
  return report.build([report_title, empty_line, additional_info])


def main():
    # filename = 'C:/Users/Nitin/OneDrive/Desktop/report.pdf'
    filename = '/tmp/processed.pdf'
    title = "Processed Update on {}".format(format(datetime.now(), "%B %d, %Y"))
    data = gen_json('./supplier-data/descriptions/')
    additional_info = gen_additional_info(data)
    generate_report(filename, title, additional_info)

if __name__ == '__main__':
    main()

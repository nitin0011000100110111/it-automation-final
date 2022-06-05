#!/usr/bin/env python3

import os
import reports
import emails
from datetime import datetime

def process_data(source_dir):
  paragraph = ""
  for file in os.listdir(source_dir):
    with open(file, 'r') as f:
      lines = f.readlines()
      paragraph += f"name: {lines[0].strip()}<br/>weight: {lines[1].strip()}<br/><br/>"
      f.close()
  return paragraph
  
def main():
  filename = "/tmp/processed.pdf"
  title = "Processed Update on {}".format(format(datetime.now(), "%B %d, %Y"))
  paragraph = process_data("./supplier-data/descriptions/")
  reports.generate_report(filename, title, paragraph)

  sender = "automation@example.com"
  recipient = "username@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits uploaded to our website sucessfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  message = emails.generate(sender, recipient, subject, body, attachment)
  emails.send(message)

  if __name__ == "__main__":
    main()

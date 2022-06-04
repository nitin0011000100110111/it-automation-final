#!/usr/bin/env python3
from numpy import rec
import emails
import reports
from datetime import datetime



def main():
  attachment = '/tmp/processed.pdf'
  title = "Processed Update on {}".format(format(datetime.now(), "%B %d, %Y"))
  data = reports.gen_json('./supplier-data/descriptions/')
  paragraph = reports.gen_additional_info(data)
  reports.generate_report(attachment, title, paragraph)
  sender = 'automation@example.com'
  recipient = 'user@example.com'
  subject = 'Upload Completed - Online Fruit Store'
  body =  'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    
  message = emails.generate(sender, recipient, subject, body, attachment)
  emails.send(message)


if __name__ == "__main":
  main()

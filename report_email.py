#!/usr/bin/env python3

import emails

def main():
  sender = "automation@example.com"
  recipient = "username@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits uploaded to our website sucessfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  message = emails.generate(sender, recipient, subject, body, attachment)
  emails.send(message)

  if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys
import psutil
import shutil
import socket
import emails

def check_cpu_usage():
	"""Returns True if the cpu is having too much usage, False otherwise"""
	return psutil.cpu_percent(1) > 80

def check_disk_space():
    """Returns True if there is enough space, False otherwise"""
    du = shutil.disk_usage('/')
    percent_free = 100 * du.free / du.total
    if percent_free < 20:
        return True
    return False

def check_memory():
    mem = psutil.virtual_memory().available / 1000000
    if mem < 500:
        return True
    return False

def check_connection():
    try:
        socket.gethostbyname('localhost')
        return False
    except:
        return True

def main():
    checks = [
        (check_cpu_usage, "Error - CPU usage is over 80%."),
        (check_disk_space, "Error - Available disk space is less than 20%."),
        (check_memory, "Error - Available memory is less than 500MB"),
        (check_connection, "Error - localhost cannot be resolved to 127.0.01")
    ]

    everything_ok = True
    subject = ""
    sender = "automation@xample.com"
    recipient  = "user@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    for check, msg in checks:
        if check():
            if len(subject) != 0:
                "<br/>".join([subject, msg])
            subject = msg
            everything_ok = False
    if not everything_ok:
        message = emails.generate(sender, recipient, subject, body)
        emails.send(message)
        print(subject)
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()

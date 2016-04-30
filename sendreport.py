#!/usr/bin/env python
# coding=utf-8

"""
Quick'n'dirty mailing script - usage: sendreport.py from to filename
"""

from email.mime.text import MIMEText
import sys
import smtplib


fp = open(sys.argv[3], "r")
msg = MIMEText(fp.read())
fp.close()


msg_from = sys.argv[1]
msg_to = sys.argv[2]

msg['Subject'] = "Nove motoinzeraty"
msg['From'] = msg_from
msg['To'] = msg_to

s = smtplib.SMTP('localhost')
s.sendmail(msg_from, [msg_to], msg.as_string())
s.quit()

#!/usr/bin/env python
# coding=utf-8

"""
Quick'n'dirty mailing script.
"""

import argparse
from email.mime.text import MIMEText
import smtplib


def main(args):
    fp = open(args.filename, "r")
    msg = MIMEText(fp.read())
    fp.close()

    msg_from = args.from_
    msg_to = args.to

    msg['Subject'] = args.subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    s = smtplib.SMTP('localhost')
    s.sendmail(msg_from, [msg_to], msg.as_string())
    s.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument("-s", "--subject", help="email subject",
                               required=True)
    required_args.add_argument("-f", "--from", help="email for the From header",
                               dest="from_", required=True)
    required_args.add_argument("-t", "--to", help="email for the To header",
                               required=True)

    parser.add_argument(
        "filename", help="file which will be read and send as a body")

    main(parser.parse_args())

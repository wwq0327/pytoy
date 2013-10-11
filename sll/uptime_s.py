#!/usr/bin/env python

import subprocess
import smtplib

MAX_LOAD = 1
DEFAULT_FROM_EMAIL = 'postmaster@sll.mailgun.org'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@sll.mailgun.org'
EMAIL_HOST_PASSWORD = '5yh0dp3nk5m3'
TO_MAIL = 'wwq0327@gmail.com'

def check_load(load_string):
    load_string = load_string.strip()
    s = load_string.split(' ')
    load_value = float(s[-1])

    if load_value >= MAX_LOAD:
        return True
    else:
        return False

def get_load_string():
    p = subprocess.Popen('uptime', shell=True, stdout=subprocess.PIPE)

    return p.stdout.readlines()[0]

def mail(tomail, string):
    msg_head = ["From:"+DEFAULT_FROM_EMAIL, "To:"+tomail, 'Subject:SLL WEB SERVER ERROR']
    msg_body = [string]
    msg = '\r\n\r\n'.join(['\r\n'.join(msg_head), '\r\n'.join(msg_body)])
    s = smtplib.SMTP(EMAIL_HOST)
    s.starttls()
    s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    s.sendmail(DEFAULT_FROM_EMAIL, tomail, msg)
    s.quit()

def main():
    load_string = get_load_string()
    load = check_load(load_string)
    if load:
        mail(TO_MAIL, load_string)        

if __name__ == '__main__':
    main()



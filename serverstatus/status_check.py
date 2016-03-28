#!/usr/bin/python

import email.message
import smtplib
import urllib

code = urllib.urlopen("<server addr>").getcode()

msg = email.message.Message()
msg['Subject'] = 'Server down'
msg['From'] = 'Sender email'
msg['To'] = 'Receiver email'
msg.set_payload('Server is down')

if code == 503:
    smtpObj = smtplib.SMTP("smtp_domain", "port", "smtp_host")
    smtpObj.ehlo()
    smtpObj.starttls()
    #if authentication is required
    smtpObj.login('user_name', 'password')

    sender = 'sender_email'
    #list of receiver emails, comma separated
    receivers = ['receiver_emails']

    try:
        smtpObj.sendmail(sender, receivers, msg.as_string())
        print "Successfully sent email"
    except Exception:
        print "Error: unable to send email"
else:
    print "Server is up and running"

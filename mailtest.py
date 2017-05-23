import smtplib

# example for use outside of function
mailFrom =  'some@email.org'
mailTo =  'your@email.com'
mailSubject =  'Python Test'
smtpserver = 'smtp.server.com'
headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (mailFrom, mailTo, mailSubject)
message = "This is a test python e-mail. Really simple to send this e-mail..."
mssg = headers + message
session = smtplib.SMTP(smtpserver)
smtpresult = session.sendmail(mailFrom, mailTo, mssg)


# Example inside of function

def send_email(mfrom, mto, msubject, message, smtpserver):
    headers = "From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n".format(mfrom, mto, msubject)
    mssg = headers + message
    session = smtplib.SMTP(smtpserver)
    smtpresult = session.sendmail(mailFrom, mailTo, mssg)


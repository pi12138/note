import smtplib
from email.mime.text import MIMEText

email_content = """<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <h1>this is a email</h1>
</body>
</html>
"""
msg = MIMEText(email_content, _subtype = 'html', _charset = 'utf-8')

from_addr = '18790065681@163.com'
from_pwd = 'zhou199893'

to_addr = '18790065681@163.com'

smtp_server = 'smtp.163.com'

try:
    print("1")
    srv = smtplib.SMTP_SSL(smtp_server.encode(), 465)
    print("2")
    srv.login(from_addr, from_pwd)
    print("3")
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
    print("success")
except Exception as e:
    print("false")
    print(e)

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
	name, addr = parseaddr(s)
	print(name, addr)
	return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = "1558255789@qq.com"
password = "akvytxhmmrvghjhf"
to_addr = "18790065681@163.com"
smtp_server = "smtp.qq.com"


msg = MIMEText('hello, send by Python.....', 'plain', 'utf-8')
msg['From'] = _format_addr("Python <{}>".format(from_addr))
msg['To'] = _format_addr("管理员 <{}>".format(to_addr))
msg['Subject'] = Header("来自smtp的邮件", 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
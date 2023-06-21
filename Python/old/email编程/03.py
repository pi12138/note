import smtplib
# 构建附件使用
from email.mime.text import MIMEText
# 构建基础邮件使用
from email.mime.multipart import MIMEBase, MIMEMultipart


content = 'this is a string'
# 构建邮件
mail_multipart = MIMEMultipart()
# 构建邮件正文
mail_text = MIMEText(content, _subtype = 'plain', _charset = 'utf-8')
# 把构建好的邮件正文添加到邮件中
mail_multipart.attach(mail_text)

# 构建邮件附件
# 构建附件需要从本地读取文件
# 打开本地文件，以rb格式打开
with open(r'01.html', 'rb') as f:
	s = f.read()
	# 设置附件MIME和文件名
	m = MIMEText(s, 'base64', 'utf-8')
	m['Content-Type'] = 'application/octet-stream'
	# 需要注意
	# 1. attachment后分好为英文状态
    # 2. filename 后面需要用引号包裹，注意与外面引号错开
	m['Content-Disposition'] = "attachment; filename = '01.html'"
    # 添加邮件附件到邮件
	mail_multipart.attach(m)

from_addr = '18790065681@163.com'
from_pwd = 'zhou19981118'
to_addr = '1558255789@qq.com'

smtp_server = "smtp.163.com"
try:
	print("1")
	srv = smtplib.SMTP_SSL(smtp_server.encode(), 465)
	print("2")
	srv.set_debuglevel(1)
	# print("2.1")
	# srv.ehlo()
	# print("w.2")
	# srv.starttls()
	print("3")
	srv.login(from_addr, from_pwd)
	print("4")
	srv.sendmail(from_addr, [to_addr], mail_multipart.as_string())
	print('success')
except Exception as e:
	# print('')
	print("false:", e)
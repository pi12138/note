import smtplib
# 多用途互联网邮件扩展（MIME，Multipurpose Internet Mail Extensions）
from email.mime.text import MIMEText
# MIMEText三个主要参数
# 1. 邮件内容
# 2. MIME子类型，在此案例我们用plain表示text类型
# 3. 邮件编码格式

# help(MIMEText)
#  __init__(self, _text, _subtype='plain', _charset=None, *, policy=None)
#  |      Create a text/* type MIME document.
#  |
#  |      _text is the string for this message object.
#  |
#  |      _subtype is the MIME sub content type, defaulting to "plain".
#  |
#  |      _charset is the character set parameter added to the Content-Type
#  |      header.  This defaults to "us-ascii".  Note that as a side-effect, the
#  |      Content-Transfer-Encoding header will also be set.
# 
str1 = "Hello, my name is zyp, I'm using python to email you!"
msg = MIMEText(str1, _subtype = 'plain', _charset = 'utf-8')

# 发送邮件的账号以及授权码
from_addr = '18790065681@163.com'
from_password = 'zhou199893'

# 收件人邮箱
to_addr = '18790065681@163.com'


# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值，
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱所的smtp地址是 smtp.qq.com
smtp_srv = "stmp.163.com"

# help(smtplib.SMTP_SSL)

try:
	# 两个参数
	# 第一个是服务器地址，但一定是bytes格式，所以需要编码
	# 第二参数是服务器的访问端口
	# srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
	print("1")
	srv = smtplib.SMTP(smtp_srv.encode(), 465)
	print("2")
	srv.set_debuglevel(1)
	# smtp.ehlo()
	# smtp.starttls()
	# 登录邮箱发送
	srv.login(from_addr, from_password)
	print("login success")
	# 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接受地址，必须是list形式
    # 3. 发送内容，作为字符串发送
	srv.sendmail(from_addr, [to_addr], msg.as_string())
	srv.quit()
	print("success")
except Exception as e:
	print("false")
	print(e)
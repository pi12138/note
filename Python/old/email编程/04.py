import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
msg = MIMEText("Hello wold",  "plain", "utf-8")
# 下面代码故意写错，说明，所谓的发送者的地址，只是从一个Header的第一个参数作为字符串构建的内容
# 用utf8编码是因为很可能内容包含非英文字符
header_from = Header("从图灵学院邮箱发出去的<TuLingXueYuan@qq.cn>", "utf-8")
msg['From'] = header_from
 
# 填写接受者信息
header_to = Header("去王晓静的地方<wangxiaojing@sina.com>", 'utf-8')
msg['To'] = header_to
 
header_sub = Header("这是图灵学院的主题", 'utf-8')
msg['Subject'] = header_sub
 
 
 
# 构建发送者地址和登录信息
from_addr = "18790065681@163.com"
from_pwd = "zhou199893"
 
 
# 构建邮件接受者信息
to_addr = "18790065681@163.com"
 
smtp_srv = "smtp.163.com"
 
 
try:

	print('1')
	srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
	srv.set_debuglevel(1)
	print('2')
	srv.login(from_addr, from_pwd)
	print('3')
	srv.sendmail(from_addr, [to_addr], msg.as_string())
	srv.quit()
	# print("1")
	# server = smtplib.SMTP()
	# print("2")
	# server.set_debuglevel(1)
	# print("3")
	# server.connect(smtp_srv)
	# print("4")
	# server.login(from_addr, from_pwd)
	# print("5")
	# server.sendmail(from_addr, [to_addr], msg.as_string())
	# print("6")
	# server.quit()

except Exception as e:
	print("false")
	print(e)

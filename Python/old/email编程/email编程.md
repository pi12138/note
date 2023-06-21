# 1.mail编程
	- https://blog.csdn.net/ydw_ydw/article/details/81914326
	- 邮件工作流程：
		- MUA(MailUserAgent)邮件用户代理
		- MTA(MailTransferAgent)邮件传输代理
		- MDA(MailDeliverAgent)邮件投递代理
		- 1.MUA—>MTA，邮件已经在服务器上了
		  2.qq MTA->........->sina MTA,邮件在sina服务器上
		  3.sina MTA ->sina MDA，此时邮件已经在你的邮箱里了
		  4.sina MDA ->MUA(Foxmail/Outlook),邮件下载到本地电脑
	- 编写程序
		- 发送：MUA -> MTA with SMTP:SimpleMailTransferProtocal, 包含MTA -> MTA
		- 接受：MDA -> MUA with POP3 and IMAP:PostOfficeProtocal v3 and v4

	- 准备工作
		- 注册邮箱(以qq邮箱为例)
		- 第三方邮箱需要特殊设置，以qq邮箱为例
			- 进入设置中心
			- 取得授权码
				- 2059233910@qq.com
				- antwbfckyfpcjibh
			

	- Python for mail
		- SMTP协议负责发送邮件
			- 使用email模块构建邮件
				- 纯文本邮件，案例01.py
			- HTML格式邮件发送
				- 准备HTML代码作为内容
				- 把邮件的subtype设为html
				- 案例02.py
			- 发送带附件的邮件
				- 可以把邮件看作是一个文本邮件和一个附件的合体
				- 一封邮件如果涉及到多个部分，需要使用MIMEMultipart格式构建
				- 案例03.py
			- 添加邮件头，抄送等信息
				- mail['From']：表示发送者的信息，包括姓名和邮件
				- mail['To']:表示接收者信息，包括姓名和邮件地址
				- mail['Subject']：表示摘要或者主题信息
				- 案例04.py
			- 同时支持html和text格式
				- 构建一个MIMEMultipart格式邮件
				- MIMEMultipart的subtype设置成alternative格式
				- 添加html和text邮件

			- 使用smtplib模块发送邮件


		- POP3协议接受邮件
			- 本质上是MDA到MUA的一个过程
			- 从 MDA下载下来的是一个完整的邮件结构体，需要解析才能得到每个具体可读的内容
			- 步骤：
            	1. 用poplib下载邮件结构体原始内容
                	1. 准备相应的内容（邮件地址，密码，POP3实例）
                	2. 身份认证
                	3. 一般会先得到邮箱内邮件的整体列表
                	4. 根据相应序号，得到某一封信的数据流
                	5. 利用解析函数进行解析出相应的邮件结构体
            	2. 用email解析邮件的具体内容

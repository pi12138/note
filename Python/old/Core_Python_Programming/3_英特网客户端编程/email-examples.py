from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


SMTPSVR = 'smtp.qq.com'
POP3SVR = 'pop.qq.com'

from_addr = '1558255789@qq.com'
to_addr = '2059233910@qq.com'
passwd = 'ngqedkkpiesqjeie'


def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('hello world!\r\n', 'plain')
    email.attach(text)
    html = MIMEText('<html><body><h1>hello world!</h1></body></html>', 'html')
    email.attach(html)

    return email


def make_img_msg(fn):
    with open(fn, 'rb') as f:
        data = f.read()

    email = MIMEMultipart('alternative')
    
    img = MIMEImage(data, name=fn)
    img.add_header('Content-Disposition', 'attachment; filename="{}"'.format(fn))
    email.attach(img)

    return email


def send_msg(from_addr, to_addr, msg):
    s = SMTP(SMTPSVR)
    s.login(from_addr, passwd)
    errs = s.sendmail(from_addr, [to_addr], msg)
    s.quit()


if __name__ == "__main__":
    print("Sending multipart alternative msg...")
    msg = make_mpa_msg()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'multipart alternative test'
    send_msg(from_addr, to_addr, msg.as_string())

    print('Sending image msg...')
    msg = make_img_msg('1.jpg')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'image file test'
    send_msg(from_addr, to_addr, msg.as_string())
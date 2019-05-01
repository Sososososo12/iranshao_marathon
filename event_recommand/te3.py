import os
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText

#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.yeah.net'
username = 'youamg2@yeah.net'
password='mikiyd299N'
sender='youamg2@yeah.net'
#receiver='XXX@126.com'
#收件人可以为多个收件人
receiver=['244300721@qq.com']

message = MIMEText('Python 邮件发送测试to yeah邮箱', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件发送测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(smtpserver, 25)    # 25 为 SMTP 端口号
    smtpObj.login(username,password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
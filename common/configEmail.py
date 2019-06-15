# coding:utf-8
__author__ = 'lenovo'

# 1--读取config.ini的email配置
# 2--配置邮件属性
# 3--发送邮件

import smtplib,os,time
from readConfig import ReadConfig
from email.mime.text import MIMEText
from email.header import Header

class configMyEmail():

    # 读取配置
    re = ReadConfig()
    host = re.get_email('mail_host')
    sender = re.get_email('sender')
    receiver = re.get_email('receiver')
    # print(host,sender)
    user = re.get_email('mail_user')
    pwd = re.get_email('mail_pass')
    subject = re.get_email('subject')
    content = re.get_email('content')

    # 邮件内容
    msg = MIMEText(_text=content,_subtype='plain',_charset='utf-8')
    msg['sender'] = sender
    msg['From'] = sender
    msg['To'] = receiver
    msg['subject'] = Header(subject,'utf-8')

    def send_email(self):
        try:
            r = smtplib.SMTP()
            r.connect(host=self.host)
            print(self.user,self.pwd)
            r.login(user=self.user,password=self.pwd)
            r.sendmail(self.sender,self.receiver,msg=self.msg.as_string())
            print('邮件发送成功')
        except Exception as msg:
            print('发送邮件失败')
            print(msg)
        else:
            print('邮件发送成功')
        finally:
            r.close()

c = configMyEmail()
c.send_email()




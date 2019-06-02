# coding:utf-8
__author__ = 'lenovo'


# 发送html内容的邮件
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header

class SendMail():
    def send_mail_html(self,file):
        sender = '2918264721@qq.com'
        receive = '1433236420@qq.com'
        # 发送邮件主题
        t = time.strftime('%Y-%M-%D %H-%M-%S',time.localtime())
        subject = '自动化测试结果'+ t
        # 发送邮箱服务器
        smtpserver = 'smtp.qq.com'
        # 发送邮箱用户名/密码
        usename = ''
        password = ''
        # 读取html文件内容
        f = open('file','wb')
        mail_body =f.read()
        f.close()

        # 组装邮件内容和标题，中文需参数'utf-8',单字节字符不需要
        msg = MIMEText(mail_body,_subtype='html',_charset='utf=8')
        msg['subject'] = Header(subject,'utf-8')
        msg['From'] = sender
        msg['To'] = receive

        # 登录并发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(usename,password)
            smtp.sendmail(sender,receive,msg.as_string())
        except:
            print('邮件发送失败')
        else:
            print('邮件发送成功')
        finally:
            smtp.quit()

    def find_new_file(self):



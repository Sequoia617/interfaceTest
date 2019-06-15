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
    # 查找最新文件
    def find_new_file(self):
        # 获取当前路径
        current_path = os.path.dirname(os.path.abspath(__file__))
        # print('current',current_path)
        # 获取报告的存放路径
        filePath = os.path.dirname(current_path.dirname(current_path) + '/' + 'report')
        print('filePath',filePath)

        fileList = os.listdir(filePath)
        # print(fileList)
        fileDict = {}
        fileTime = []
        for i in fileList:
            filename = filePath + '/' + i
            iTime = os.path.getmtime(filename)
            fileTime.append(iTime)
            fileDict[iTime] = i
        print(fileDict,fileTime)

        sendfilekey = max(fileTime)
        sendfile = fileDict[sendfilekey]
        print(sendfile)
        sendfile = filePath + '/' + sendfile
        return sendfile
    # 发送邮件
    def send_mail(self):
        self.config_file()
        try:
            s = smtplib.SMTP()
            print(self.mail_host,self.mail_user,self.mail_pass,self.sender,self.receivers)
            s.connect(self.mail_host,25) # 25为 SMTP 端口号
            # s.set_debuglevel(1)
            s.login(self.mail_user,self.mail_pass)
            s.sendmail(self.sender,self.receivers,self.msg.as_string())
            print('邮件发送成功')
        except smtplib.SMTPException as msg:
            # print(msg)
            print('Error:无法发送邮件')

# if __name__ == '__main__':
#     pass
# c = ConfigEmail()
# c.send_mail()




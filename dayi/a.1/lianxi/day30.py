# import schedule #专门定时的工具
# import time
# from datetime import datetime
#
# def job():
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{now}]执行任务...")
# schedule.every(1).minutes.do(job) # every 每
#             # minutes 分钟
# schedule.every().hour.do(job)     #  h 小时
# schedule.every().day.at("10:30").do(job)
# schedule.every().thursday.do(job)
# schedule.every(5).to(10).seconds.do(job) #seconds 秒
#
# def greet(name):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{now}]--- {name}")
# schedule.every(7).seconds.do(greet,name = 'Ciallo～(∠・ω< )⌒★')
# count = 0
# def job1():
#     global count  #全局的 我要用外面那个
#     print("正在运行///")
#     count += 1
#     print("执行任务，次数：", count)
#     if count >= 3:
#         print("次数够了，取消任务")
#         schedule.cancel_job(task) #取消任务
# task = schedule.every(5).seconds.do(job1)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


import schedule
import time_
from datetime import datetime


# count = 0
# def print_time():
#     global count
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     count += 1
#     if count == 1:
#         schedule.cancel_job(da)
#         print("已经取消任务")
# da = schedule.every(1).minutes.do(print_time)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


import os
import smtplib  #连接邮箱的内置模块
from email.mime.text import MIMEText #在邮件里面写字的
from email.header import Header #解决中文乱码的

#邮件配置
smtp_server = "smtp.qq.com"
smtp_port = 587
sender = "3602781622@qq.com"
password = os.getenv('QQ_shouquanma') # get 获取 env 环境变量

receiver = ["3602781622@qq.com"," 3586597170@qq.com"]

#构建邮件内容
subject = "python 自动发邮件测试 " # 标题
# content = "Ciallo～(∠・ω< )⌒★ 第三封 " # 正文
content = """
<p style="font-size: 16px;">
    <span style="color: #ff69b4;">Ciallo～(∠・ω< )⌒★</span>
    <span style="color: #90ee90;"> 第三封 </span>
    <span style="color: #87ceeb;">看你什么时候会注意到莫名其妙多了三封邮件</span>
    <span style="color: #90ee90;"> 桀桀桀 </span>
</p>
"""   #html好看

# msg = MIMEText(content,"plain","utf-8") # 核心 第一个是刚刚写的正文 第二个表示是纯文本的邮件
msg = MIMEText(content,"html","utf-8") # 核心 第一个是刚刚写的正文 第二个表示是html 的就是可以好看
msg["From"] = Header(sender) # Header 加不加都行  from是发送的地址
# msg["To"] = Header(receiver) # to 是收件人地址 发给单人
msg["To"] = Header(", ".join(receiver)) # 发给多人
            # 原因：msg["To"] 只能接收字符串，不能直接放列表。
            # 用 ", ".join(receiver) 把列表变成 "a@qq.com, b@qq.com, c@qq.com" 这样的字符串，邮箱才能正确显示所有收件人。
msg['Subject'] = Header(subject, "utf-8")

# try:
#     server = smtplib.SMTP(smtp_server,smtp_port) # 地址，端口号
#     server.starttls() #启用 TLS 加密 防止截取别人偷看
#     server.login(sender,password) #登录邮箱 你的地址，授权码
#     # server.sendmail(sender,[receiver],msg.as_string()) #真正发邮件的一步 单人必须加[] 因为仅支持列表形式
#     server.sendmail(sender,receiver,msg.as_string()) #所以多人不用加[]
#     print("邮件发送成功")
# except Exception as e:
#     print(f"发送失败: {e}")
# finally:
#     server.quit()



# 使用 MIMEMultipart 构建复合邮件
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg["From"] = Header(sender)
msg["To"] = Header(", ".join(receiver))
msg['Subject'] = Header(subject)

#添加正文
body = MIMEText(content,"html","utf-8")
msg.attach(body) # attach 是附件必须的

filename = r"D:\za\旮旯给木\二周目.png"
with open(filename,"rb") as f:
            # rb就是read binary，不管是文本、图片还是压缩包，都得这么读。
    part = MIMEBase("application","octet-stream")
            #空附件容器 都这么读 通用的
    part.set_payload(f.read()) # set_payload()：把文件内容放进刚才创建的附件容器里
    encoders.encode_base64(part) #把文件内容编码成邮件能传输的格式。
    part.add_header("Content-Disposition",f"attachment; filename= {filename}")
            # Content-Disposition     attachment   告诉邮箱：这部分内容是「附件」
    msg.attach(part) #附加上去

try:
    server = smtplib.SMTP(smtp_server,smtp_port) # 地址，端口号
    server.starttls() #启用 TLS 加密 防止截取别人偷看
    server.login(sender,password) #登录邮箱 你的地址，授权码
    # server.sendmail(sender,[receiver],msg.as_string()) #真正发邮件的一步 单人必须加[] 因为仅支持列表形式
    server.sendmail(sender,receiver,msg.as_string()) #所以多人不用加[]
    print("邮件发送成功")
except Exception as e:
    print(f"发送失败: {e}")
finally:
    server.quit()




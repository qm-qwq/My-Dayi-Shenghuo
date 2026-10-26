import os
import smtplib  #连接邮箱的内置模块
from email.mime.text import MIMEText #在邮件里面写字的
from email.header import Header #解决中文乱码的
# 使用 MIMEMultipart 构建复合邮件
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from matplotlib import pyplot as plt
import schedule
import time
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False #修复画图的中文警告

# 生成最近7天数据
dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
categories = ['电子产品', '服装', '家居用品']

data = []
for d in dates:
    for cat in categories:
        data.append({
            '日期': d,
            '产品类别': cat,
            '销售额': np.random.randint(2000, 10000),
            '订单数': np.random.randint(10, 100)
        })

df = pd.DataFrame(data)
df.to_excel('daily_sales.xlsx', index=False)
print("模拟数据已生成：daily_sales.xlsx")


def load_today():
    df = pd.read_excel('daily_sales.xlsx')
    df['日期'] = pd.to_datetime(df['日期']) #to转为  datetime 日期时间类型
    # 假设数据中包含多天，我们取最近一天 就是取最大值
    latest_date = df['日期'].max()
    today_data = df[df['日期'] == latest_date]
    return today_data, latest_date.strftime('%Y-%m-%d')

def calculate (df):
    zxxe = df['销售额'].sum()
    dds = df['订单数'].sum()
    pjdj = zxxe / dds if dds != 0 else 0 # 变量 = 条件成立时的值 if 条件 else 条件不成立时的值
    return zxxe, dds, pjdj
def generate(df,date_str):
    cat = df.groupby('产品类别')['销售额'].sum() #对每个产品分别求和

    plt.figure(figsize=(10,10))
    bars = plt.bar(cat.index,cat.values,color='skyblue') # plt.bar(x轴数据，y轴数据)
    plt.title(f'{date_str} 各产品类别销售额')
    plt.xlabel('产品类别')
    plt.ylabel('销售额（元）')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2,yval + 100,f'{yval:,.0f}',ha = 'center')
            #bar.get_x() 是柱子左边起点 bar.get_width()/2 是柱子正中间位置 加一百是防止重叠 格式化不带小数
            #ha = “center” 水平对齐
    plt.tight_layout() #自动布局防截断
    plt.savefig('daily_chart.png')
    plt.close() #关闭图表防止占用内存
    return 'daily_chart.png'

sender = "3602781622@qq.com"
password = os.getenv('QQ_shouquanma')
receiver = "3602781622@qq.com"

def send_email(metrics,date_str,path):
    zxxe, dds, pjdj = metrics

#构建邮件内容
    subject = f"python 销售日报 - {date_str}"
    html = f"""
    <html>
    <body>
    <p style="font-size: 16px;">
        <span style="color: #ff69b4;">Ciallo～(∠・ω< )⌒★</span>
        <span style="color: #90ee90;"> 饿啊怎么吧手机号放这里了 </span>
        <span style="color: #87ceeb;">不许涩涩</span>
        <span style="color: #90ee90;"> 桀桀桀 </span>
    </p>
        # <hr>
        #     <h2>销售日报（{date_str}）</h2>
        #     <p><strong>总销售额：</strong> {zxxe:,.0f} 元</p>
        #     <p><strong>总订单数：</strong> {dds} 笔</p>
        #     <p><strong>平均客单价：</strong> {pjdj:.2f} 元</p>
        #     <p>详细图表请见附件。</p>
        # <hr>
        # <p><i>本邮件由 Python 自动发送</i></p>
    </body>
    </html>
    """
    #html好看

    msg = MIMEMultipart() #附件专用
    msg["From"] = Header(sender)
    msg["To"] = Header(receiver if isinstance(receiver,str) else ", ".join(receiver))
                #isinstance 判断是不是某种类型 如果是单个就是字符串 直接是字符串防止拆开 如果多人那就是列表 join只能是列表的形式
    msg['Subject'] = Header(subject)

    #添加正文
    body = MIMEText(html,"html","utf-8")
    msg.attach(body) # attach 是附件必须的

    filename = 'daily_chart.png'
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
        server = smtplib.SMTP("smtp.qq.com", 587,timeout=10)# 地址，端口号
        server.starttls()
        server.login(sender, password)  # 登录邮箱 你的地址，授权码
        server.sendmail(sender,[receiver],msg.as_string()) #真正发邮件的一步 单人必须加[] 因为仅支持列表形式
        print("邮件发送成功")
    except Exception as e:
        print(f"发送失败: {e}")

#===================================================================
def main():
    data, date_str = load_today()
    if data.empty: #判断表格是不是空的
        print("没有找到当天数据")
        return
    metrics = calculate(data)
    generate(data,date_str)
    send_email(metrics,date_str,'daily_chart.png')
    print("日报任务完成")
if __name__ == '__main__':
    main()
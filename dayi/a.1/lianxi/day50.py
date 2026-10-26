import os # 简单操作文件的
import shutil # 批量操作文件的
import smtplib # 发邮件的
import argparse # 操作命令台的
import time # 定时暂停
import schedule # 定时固定时间任务
from email.mime.text import MIMEText #邮件的TExt也就是正文
from email.header import  Header # 邮件标题防乱码
from datetime import datetime #专门处理时间的


#-------------邮件配置-------------
# os.environ.get 读取系统环境变量
SMTP_SERVER = os.environ.get('SMTP_SERVER',"smtp.qq.com") #获取SMTP服务器地址 默认qq
SMTP_PORT = int(os.environ.get('SMTP_PORT',465)) #获取SMTP的端口号 默认465
SENDER = os.environ.get("QQ_yx","") # 获取发件人邮箱地址
PASSWORD = os.environ.get("QQ_shouquanma","") # 获取授权码
RECEIVER = os.environ.get("QQ_yx","") # 收件人邮箱
#测试用
#print("读取到的邮箱：", SENDER)
#print("读取到的授权码：", PASSWORD)

#------------系统检查---------------
def get_disk_usage(path="C:/"):
    """获取磁盘使用率（百分比）和详细信息（默认C盘）"""
    usage = shutil.disk_usage(path) # 查询指定路径的磁盘空间信息 disk 磁盘硬盘 usage使用占用
    percent = (usage.used / usage.total) * 100 # 计算磁盘使用率的百分比（已经是应用的/总共的）
    return {
        "path": path,
        "total": usage.total // (2 ** 30), # //整除 2**30 -> 1GB对应的字节数  就是把单位换算成GB
        "used": usage.used // (2 ** 30),
        "free": usage.free // (2 ** 30),
        "percent": round(percent, 2) # round 保留两位小数 percent 百分比
    }

def get_hostname():
    return os.uname().nodename if hasattr(os,'uname') else "Unknown"
    # 返回 读取的系统主机名 如果 os模块有uname方法的话 否则返回 不知道

#--------------邮件发送------------
def send_alert(disk_info,threshold): #disk_info磁盘空间信息 threshold 阈值界限
    """发送告警邮件"""
    if not SENDER or not PASSWORD or not RECEIVER: #如果任意一个邮件的内容为空
        print("邮件配置不完整，请设置环境变量 QQ_yx, QQ_shouquanma, QQ_yx")
        return

    subject = f"【告警】磁盘使用率超过阈值 - {get_hostname()}"
    html = f"""
    <html>
    <body>
        <h2>磁盘使用率告警</h2>
        <p><strong>主机：</strong>{get_hostname()}</p>
        <p><strong>分区：</strong>{disk_info['path']}</p>
        <p><strong>使用率：</strong>{disk_info['percent']}%(阈值{threshold}%)</p>
        <p><strong>已用空间：</strong> {disk_info['used']} GB</p>
        <p><strong>剩余空间：</strong> {disk_info['free']} GB</p>
        <p><strong>总容量：</strong> {disk_info['total']} GB</p>
        <p><strong>时间：</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <hr>
        <p><i>此邮件由监控系统自动发送</i></p>
       </body>
       </html>
    """
    msg = MIMEText(html, "html", "utf-8") #TExt正文
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(SENDER)
    msg['To'] = Header(RECEIVER)

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) #SMTP服务的放一块 创建客户端连接服务器
        server.login(SENDER, PASSWORD) # 登录账号
        server.send_message(msg) # 发送正文
        server.quit() # 关闭
        print("告警邮件发送成功")
        return True

    except Exception as e:
        print(f"邮件发送失败: {e}")
        return False

#-------------主检查函数-----------------------
def check_and_alert(path="C:/",threshold=80): # 阈值80%
    disk = get_disk_usage(path) #鼠标放上去就能看是啥
    print(f"[{datetime.now().strftime('%H:%M:%S')}]{path}使用率：{disk['percent']}%")
    if disk["percent"] > threshold:
        print(f"!!!超过阈值{threshold}%,发邮件警告，木嘿嘿嘿嘿嘿嘿")
        send_alert(disk,threshold)
    else:
        print("正常")

#---------------------命令行入口---------------
def main():
    parser = argparse.ArgumentParser(description="磁盘监控警告脚本")
    #description 是运行脚本时候的提示 反正这个就是一个固定的开场白 先创建 最最后打包
    parser.add_argument("--path","-p",default="C:/",help="要检查的分区路径，默认 C:/")
    parser.add_argument("--threshold","-t",type=float,default=80,help="阈值百分比，默认 80")
    parser.add_argument("--interval","-i",type=int,help="定时检查间隔（分钟），若指定则循环执行")
    args = parser.parse_args() #落幕解析打包
    if args.interval: # 检测是否传入时间间隔参数
        print(f"开始定时监控（间隔{args.interval}分钟），按ctrl + c 停止")
        schedule.every(args.interval).minutes.do(check_and_alert,args.path,args.threshold) #每分钟做一次 按顺序执行（后面俩参数）
        check_and_alert(args.path,args.threshold) #这个意思是启动的时候先执行一次再等预定时间再执行一次
        while True: # 循环执行 间隔60秒喵
            schedule.run_pending()
            time.sleep(60)
    else: # 否则只执行一次
        check_and_alert(args.path,args.threshold)

if __name__ == "__main__":
    main()

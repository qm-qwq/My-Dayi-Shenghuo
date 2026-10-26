import os # 处理文件的
import shutil # 复制文件夹的
import argparse # 命令行参数
import hashlib # 判断是否重复的
import json # 处理json数据的
import zipfile # 解压的
from datetime import datetime # 获取当前时间的
import schedule #定时加自动执行的
import time # 等待时间的

STATE_FILE = 'backup_state.json'

def get_file_hash(filepath):
    """计算文件的MD5哈希（用于判断是否修改）"""
    hash_md5 = hashlib.md5() # 生成文件/文字的唯一指纹 用来查重校验加密 创建一个MD5工具算
    # MD5是文件的唯一身份证
    with open(filepath, 'rb') as f: # rb 是专门读非文本的文件 用二进制形式打开
        for chunk in iter(lambda:f.read(4096), b''):
            #一次读4096字节 iter（）一直读到文件结束（到b''停）
            hash_md5.update(chunk) # chunk每次读到的一片数据  不一次读完都是为了防卡
    return hash_md5.hexdigest() #输出32位md5字符串 就算身份证

def load_state():
    """加载上次备份的状态（文件路径->修改时间和哈希）"""
    if os.path.exists(STATE_FILE): # 判断文件是否存在 存在读 不存在就返回{}
        with open(STATE_FILE, 'r') as f:
            state = json.load(f) # 转成python字典
    return{}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2) # 把数据写到文件里面（要保存的数据，---）缩进2个空格

def need_backup(filepath,state,incremental):
    """判断文件是否需要备份"""
    if not incremental: # 如果不是备份改过的文件
        return True # 需要备份
    if filepath not in state: # 备份state
        return True
    mtime = os.path.getmtime(filepath) #拿到文件的最后一个修改时间
    if mtime != state[filepath].get('mtime'):
        return True
    return False

def copy_file(src,dst,relative_path): # (源文件，目标文件，相对路径）
    """复制单个文件到目标目录，保留相对路径结构"""
    dst_full = os.path.join(dst,relative_path) # 拼一个完整的目标路径
    os.makedirs(os.path.dirname(dst_full),exist_ok=True) #创建目标文件夹 那个true是有的话就不建
    shutil.copy2(src,dst_full) #copy2是复制文件加保留文件修改的时间 适合备份
    print(f"已复制：{relative_path}")

def create_zip(backup_dir,zip_name=None):
    """将backup_dir 内所有文件压缩为zip，并且删除原目录"""
    if zip_name is None:
        zip_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        # 创建一个空的zip压缩包 zipfile.ZIP_DEFLATED 开启压缩
        for root,_,files in os.walk(backup_dir): # os.walk 地毯式搜索文件夹和for搭配使用
            for file in files:
                full_path = os.path.join(root,file)
                arcname = os.path.relpath(full_path,start = os.path.dirname(backup_dir))
                #relpath是相对路径 (文件完整路径，起点) dirname取文件夹部分不要文件名字  backup_dir 是上一级目录
                zf.write(full_path,arcname)

    #删除原目录
    shutil.rmtree(backup_dir)
    print(f"已压缩并且删除原目录{zip_name}")
    return zip_name

def backup(src,dst,incremental=True,zip_output=False,log_file=None):
    # src 源目录 dst 目标目录 incremental=True默认开启增量备份 默认不压缩 日志log
    """执行备份"""
    if not os.path.exists(src):
        print(f"源目录不存在：{src}")
        return
    os.makedirs(dst,exist_ok=True) # 创建文件夹

    state = load_state() if incremental else {} # 上次备份记录
    new_state = {}
    backed_up = 0 # 统计已备份文件数
    skipped = 0 # 统计跳过文件数

    for root,dirs,files in os.walk(src):
        for file in files:
            src_full = os.path.join(root,file) # 文件完整源路径
            relative = os.path.relpath(src_full,start = src) # 相对路径
            dst_full = os.path.join(dst,relative) # 备份目标路径
            if need_backup(src_full,state,incremental):
                copy_file(src_full,dst,relative)
                backed_up += 1
                #记录新状态
                new_state[src_full] = {
                    "mtime": os.path.getmtime(src_full),
                    "hash": get_file_hash(src_full),
                } # 同时记录当前文件修改时间和MD5 哈希存入
            else:
                skipped += 1
                # 保留旧状态
                new_state[src_full] = state[src_full]
    if incremental:
        save_state(new_state) # 增量备份模式下，把本次新的文件状态写入 JSON 文件，作为下次备份的参照依据

        #日志记录
        log_msg = f"{datetime.now()} - 备份完成：{backed_up} 个文件已复制，{skipped} 个跳过"
        print(log_msg)
        if log_file:
            with open(log_file,'a', encoding="utf-8") as f:
                f.write(log_msg + "\n")

        if zip_output:
            zip_path = create_zip(dst)
            return zip_path
        return dst

def run_scheduled_backup(args):
    """定时任务的包装函数"""
    print(f"执行定时备份: {datetime.now()}")
    backup(args.src,args.dst,incremental=args.incremental,zip_output=args.zip,log_file=args.log)
    # 结合前面 argparse 解析的终端指令，接收你在命令行输入的所有配置，启动整套备份流程。

def setup_schedule(args): # 参数是下面命令行里面用的
    """设置定时计划"""
    if args.schedule == 'daily':
        schedule.every().day.at(args.time).do(run_scheduled_backup,args)
        # schedule.every().day.at(时间) 设定每天指定时刻运行
        print(f"已设置每日 {args.time} 执行备份")
    elif args.schedule == 'hourly':
        schedule.every().hour.do(run_scheduled_backup, args)
        print("已设置每小时执行备份")
    else:
        # 自定义间隔（单位分钟）
        if args.interval:
            schedule.every(args.interval).minutes.do(run_scheduled_backup, args)
            # every(数值n).minutes 每隔n分钟运行一次  args.interval是命令行传入的分钟数
            print(f"已设置每 {args.interval} 分钟执行备份")

    print("按 Ctrl+C 停止定时备份")
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt: #按 ctrl+c会触发异常
        print("定时备份已停止")

def main():
    parser = argparse.ArgumentParser(description="目录备份工具（支持全量/增量，定时，压缩）")
    # 创建一个命令行参数解析器 专门读取在终端输入的指令 description 是运行脚本时 -h 查看帮助会显示
    parser.add_argument("--src",required=True,help="源目录") # required=True 表示参数必须传
    parser.add_argument("--dst",required=True,help="目标目录")
    parser.add_argument("--incremental",action="store_true",help="增量备份（默认全量）")
    # ,action="store_true" 开关类参数
    parser.add_argument("--zip",action="store_true",help="备份后压缩为zip文件")
    parser.add_argument("--log",help="日志文件路径")
    parser.add_argument("--schedule",choices=['daily','hourly'],help="定时模式")
    parser.add_argument("--time",default="09:00",help="每日备份的时间（仅当schedule=daily时有效）")
    # default="09:00“ 默认值
    parser.add_argument("--interval",type=int,help="定时间隔（分钟）")

    args = parser.parse_args() # 解析器 打包这些命令的

    if args.schedule or args.interval: # 如果定时或者自定义时间 就按照模式定时
        setup_schedule(args)
    else: # 否则先备份
        backup(args.src, args.dst, incremental=args.incremental,zip_output=args.zip,log_file=args.log)

if __name__ == "__main__":
    """自动定时备份脚本"""
    main()


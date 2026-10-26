import argparse
import json
import logging
import os
import time
from logging import Logger #官方标准库的日志模块
from logging.handlers import RotatingFileHandler # 导入轮转文件处理器


# 创建一个 config.json，集中存放常用参数，避免每次都要输入。 里面邮件还是要填邮箱
def lod_config(path="config.json"):
    if os.path.exists(path):
        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)
    return {}

# 实现自动轮转（避免日志无限增长）
def setup_logger(name,log_file,max_bytes=5*1024*1024,backup_count=3):
    # name 日志器的唯一名称 log_file 日志输出的文件路径 max_bytes 单个文件最大容量 这里是5MB backup——count 最多保留的备份日志数量
    """设置带轮转的日志记录器"""
    logger: Logger = logging.getLogger(name) #根据名称获取日志器对象
    logger.setlength(logging.INFO) # 设置日志的最低记录级别 等级低的不记录
    if not logger.handlers:
        handler = RotatingFileHandler(log_file,maxBytes=max_bytes,backupCount=backup_count,encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # 定义每一条日志的排版格式 里面的占位符会自动替换成 （时间-名称-内容）
        handler.setFormatter(formatter) # 把定义好的格式绑定给文件处理器
        logger.addHandler(handler) # 同样绑定
        return logger #返回方法可以用,info()这样调用

def get_file_age_days(file_path):
    """返回文件最后有一次修改距今天数"""
    mtime = os.path.getmtime(file_path)
    return (time.time() - mtime)/86400 #86400秒=1天

def clean_old_files(directory,days,dry_run=False,ext=None):
    # （目标文件路径，文件保留天数，预览模式开关，文件后缀过滤）
    """删除指定目录下超过 days 天未修改的文件"""
    deleted_count = 0
    for root,dirs,files in os.walk(directory): #遍历所有
        for file in files:
            file_path = os.path.join(root,file)
            if ext and not file.endswith(ext):
                continue
            if get_file_age_days(file_path) > days:
                if dry_run:
                    print(f"[预览] 将删除: {file_path}")
                else:
                    os.remove(file_path)
                    print(f"已删除: {file_path}")
                deleted_count += 1
    mode = "预览" if dry_run  else "执行"
    print(f"{mode}完成，共处理{deleted_count}个文件")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="清理过期文件")
    parser.add_argument("--directory","-d",required=True,help="目标目录")
    parser.add_argument("--days","-t",type=int,default=30,help="过期天数，默认30天")
    parser.add_argument("--ext","-e",help="只处理指定扩展名（如.log）")
    parser.add_argument("--dir-run","-n",action="store_true",help="预览模式，不实际删除")
    args = parser.parse_args()

    clean_old_files(args.directory,args.days,args.dir_run,args.ext)
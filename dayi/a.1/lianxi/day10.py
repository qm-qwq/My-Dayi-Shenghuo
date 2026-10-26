# import random
# random.random() 返回 [0.0, 1.0) 的随机浮点数
# random.randint(a, b)	返回 [a, b] 的随机整数
# random.choice(seq)	从序列中随机选一个元素
# random.shuffle(lst)	原地打乱列表顺序
# random.sample(范围,抽几个)  不放回抽样
import code
# strftime	机器时间 → 人类时间	给人看、存、用
# strptime	人类时间 → 机器时间	给机器算、处理
import datetime
import os
from sys import path

now = datetime.datetime.now()
print(now)

print(now.strftime("%Y/%m/%d %H:%M:%S"))

dt = datetime.datetime.strptime("2026/04/16", "%Y/%m/%d")
print(dt)

today = datetime.date.today()
cha = today + datetime.timedelta(days=7)
print(cha)

os.getcwd ()   #获取当前工作目录
print(os.getcwd)
# os.listdir(path)   #列出目录下的文件和文件夹
# os.path.join(a,b)   跨平台拼接路径
# os.path.exists(path)    判断路径是否存在
# os.path.isfile(path)    判断是否为文件
# os.path.isdir(path)     判断是否为目录
# os.mkdir(path)          创建目录（父目录必须存在）
# os.makedirs(path)       创建目录（自动创建父目录）
# os.remove(path)         删除文件
# os.rmdir(path)          删除空目录
# import os
# print(os.getcwd())
# print(os.listdir("."))
# if not os.path.exists("date"):
#     os.mkdir("date")
#
# sys.argv 命令行参数列表（argv[0] 是脚本名）
# sys.exit([code]) 退出程序，code 0 表示正常
# sys.path  模块搜索路径列表
# sys.version Python 版本信息
# sys.stdin /sys.stdout  标准输入/输出（一般不直接用，用 input() 和 print()）

import sys
if len(sys.argv) > 1:
    print(f"第一个参数是：{sys.argv[1]}")
else:
    print("没有提供参数")

# JSON
# json.dumps(obj)     将 Python 对象转为 JSON 字符串
# json.loads(s)       将 JSON 字符串转为 Python 对象
# json.dump(obj,file)     将 Python 对象写入文件（JSON 格式）
# json.load(file)     从 JSON 文件中读取并转为 Python 对象

import json
# 转为 JSON 字符串
date = {"name":"张三","age": 18, "city": "北京"}
json_str = json.dumps(date, ensure_ascii=False) # ensure_ascii=False 保留中文
print(json_str)

with open("data.json","w",encoding="utf-8") as f:
    json.dump(date,f,ensure_ascii=False)


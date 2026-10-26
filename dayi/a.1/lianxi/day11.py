# import datetime
# date = datetime.datetime.now()
# d = date.strftime("%Y-%m-%d %H:%M:%S")
# print(d)
#
# import os
# print(os.getcwd())
#
# s = os.listdir(r"\python\a.1\lianxi")
# for i in s:
#     print(i)


import datetime
data = []
print("--- 命令行笔记本 ---\n")
print("1.写日记")
print("2.查看所有日记")
print("3.按日期搜索")
print("4.退出")
d = datetime.datetime.now()
d1 = d.strftime("%Y-%m-%d %H:%M:%S")
while True:
    m = input("请输入操作（1-4）")
    if m == "1":
        n = input("请输入内容：（换行结束）")
        if n == "\n":
            with open(r"D:\python\diary.txt", "a", encoding="utf-8") as f:
                nn = f.write(n)
            with open(r"D:\python\diary.txt", "r", encoding="utf-8") as f:
                data = f.readlines()
            print("已保存")
            continue
    if m == "2":
        with open(r"D:\python\diary.txt", "r", encoding="utf-8") as f1:
            f1 = f1.read()
        for i in data:
            print(i + "." + "[" + d1 + "]" + "\n" + data)  #遍历的时候可能给其他行加序号
    if m == "3":
        p = input("请输入要搜索的日期（格式：YYYY-MM-DD）：")
        # try:
        #     # date.               查找不会
    if m == "4":
        print("baibai")
        break

































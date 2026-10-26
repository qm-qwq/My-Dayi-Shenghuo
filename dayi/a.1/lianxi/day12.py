import datetime
data = []
print("--- 命令行笔记本 ---\n")
print("1.写日记")
print("2.查看所有日记")
print("3.按日期搜索")
print("4.退出")

while True:
    m = input("请输入操作（1-4）")
    if m == "1":
        n = input("请输入内容：（换行结束）")
        if n.strip():

            d = datetime.datetime.now()
            d1 = d.strftime("%Y-%m-%d %H:%M:%S")

            with open(r"D:\python\diary.txt", "a", encoding="utf-8") as f:
                f.write(f"[{d1}] {n}\n")
            print("已保存")
            continue
    elif m == "2":
        with open(r"D:\python\diary.txt", "r", encoding="utf-8") as f1:
            l = f1.readlines()
        for i,l in enumerate(l,1):
            print(f"{i}.{l.strip()}")  #遍历的时候可能给其他行加序号
    elif m == "3":
        p = input("请输入要搜索的日期（格式：YYYY-MM-DD）：")
        with open(r"D:\python\diary.txt", "r", encoding="utf-8") as f1:
            l = f1.readlines()
            for li in l:
                if li.startswith(f"[{p}"):
                    print(f"{li.strip()}")
    elif m == "4":
        print("baibai")
        break
    else:
        print(" 请输入1-4之间的数字！")
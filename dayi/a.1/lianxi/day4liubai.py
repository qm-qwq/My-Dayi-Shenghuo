dit = []

while True:
    print("---代办任务管理系统---"
          "1.添加任务"
          "2.删除任务"
          "3.显示所有"
          "4.标记任务完成"
          "5，退出")
    a = input("请选择操作（1-5）：")

    if a == "1":
        n = input("请输入内容：")
        dit.append({"name": n,"zt": False})
        print(f"已添加：{n}")

    elif a == "2":
        c = input("请输入要删除项目的序号")
        del dit[c]
        print(f"已删除{c}")
    elif a == "3":
        print(dit)
    elif a == "4":
        d = input("请标记完成内容：")
    elif a == "5":
        break
    else:
        print("请输入正确数字")



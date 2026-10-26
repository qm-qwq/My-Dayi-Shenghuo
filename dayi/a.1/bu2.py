#  day4 数组练习

t = []
def p():
    print("\n--- 待办清单管理系统 ---")
    print("1. 添加任务")
    print("2. 删除任务")
    print("3. 显示所有任务")
    print("4. 标记任务完成")
    print("5. 退出")
def s():
    if not t:
        print("无任务")
        return
    print("\n当前待办清单：")
    for m,n in enumerate(t,1):
        d = "✔" if n["co"] else ""
        print(f"{m}. [{d}]  {n["name"]}")
def a():
    name = input("请输入内容")
    t.append({"name": name,"co": False})
def d():
    s()

    try:
        n = int(input("请输入要删除的任务编号："))
        if 1 <= n <= len(t):
            r = t.pop(n - 1)  # 因为索引从0 输入的多一
            print(f"已删除任务：{r['name']}")
        else:
            print("编号无效")
    except:
        print("编号无效")
def c():
    s()

    try:
        n = int(input("请输入完成的任务编号："))
        if 1 <= n <= len(t):
            t[n - 1]["co"] = True
            print(f"已将任务“{t[n - 1]['name']}”标记为完成")
        else:
            print("编号无效")

    except ValueError:
        print("请输入数字")
while True:
    p()
    x = input("请选择操作（1-5）：")
    if x == "1":
        a()
    elif x == "2":
        d()
    elif x == "3":
        s()
    elif x == "4":
        c()
    elif x == "5":
        break
    else:
        print("无效选择，请重新输入")








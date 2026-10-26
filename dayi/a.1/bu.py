# 计算机练习 day7

# 补充知识点！！！！！！！！！！
# for 第一个变量, 第二个变量 in enumerate(对象, 序号):
# 第一个变量 = 序号
# 第二个变量 = 对象
#
#


def jia(a,b):
    return a + b
def jian(a,b):
    return a - b
def cheng(a,b):
    return a * b
def chu(a,b):
    return a / b
def mi(a,b):
    return a ** b
o = {
    '+':(jia,"+"),
    '-':(jian,"-"),
    '*':(cheng,"*"),
    '/':(chu,"/"),
    '**':(mi,"**")
}
h = []
print("欢迎使用命令行计算器！ 请带空格输入比如（1 + 5）")
print("支持运算：+ - * / **")
print("输入格式：数字 运算符 数字")
print("特殊命令：h查看历史, c清除全部, q退出")

while True:
    i = input("请输入")
    if i == "q":
        break
    elif i == "h":
        if not h:
            print("无记录")
        else:
            for t,r in enumerate(h,1):
                print(f"{t},  {r}")
        continue
    elif i == "c":
        h.clear()
        print("已清空")
        continue

    p = i.split()   #解包 把数提出来
    if len(p) != 3:
        print("请正确输入，格式错误")
        continue
    a,op,b = p
    if op not in o:
        print(f"错误：不支持的运算符 '{op}'，支持：+ - * / **")
        continue

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("错误：数字格式无效，请输入数字")
        continue
    m,n = o[op]   #在o里面找到op 对应的值 刚好对应俩 m  n
    try:
        r = m(a,b)
    except ZeroDivisionError as e:  # 除0错误
        print(f"错误：{e}")
        continue
    ex = f"{a} {op} {b} = {r}"
    print(ex)
    h.append(ex)  #记录历史





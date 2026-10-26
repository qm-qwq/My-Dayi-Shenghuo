import math

print(math.sqrt(16)) # 平方根

import math as m
print(m.sqrt(16))

from math import sqrt, pi
print(sqrt(16))   # 可以直接用 sqrt，不需要 math.
print(pi)

# import math → 用的时候要写 math.sqrt()
# from math import * → 直接写 sqrt()，更省事

# def f(x , y):
#     return x + y
# if __name__ == "__main__": # 在另一个文件调用时不会打印；但直接在当前运行时会打印。
#     print("ceshi",f(2,3))
# def ff(n):
#   return  f"hi,{n}"
# if __name__ == "__main__":
#     print(ff(2))
#
#



#
# y = []
# while True:
#     print('欢迎')
#     print("仅支持+-*/**运算"
#           "h查看历史记录 c清除所以 q退出")
#     try:
#         a = int(input("数字"))
#         x = input("运算符")
#         b = int(input("数字"))
#
#     except:
#         if a == "q":
#             break
#
#         print("请正确输入")
#         continue
#
#     if x == "+":
#         c = a + b
#         print(c)
#     elif x == "-":
#         d = a - b
#         print(d)
#     elif x == "*":
#         e = a * b
#         print(e)
#     elif x == "/":
#         f = a / b
#         print(f)
#     elif x == "**":
#         g = a ** b
#         print(g)
#     else:
#         print("请正确输入")
#














































# fi = open(文件,方式)
# 直接写完整路径，电脑就会精准定位
# fi = open(r"D:\python\a.txt", "r")
# c = fi.read()
# print(c)
#
# fi.close()

# f = open(r"D:\python\a.txt", "r")
# l1 = f.readlines()
# l2 = f.readline()
# f.close()
# print(l1)
# print(l2)


# 推荐下面这个
ff = open(r"D:\python\a.txt", "r")
for line in ff:
    print(line,end='')
ff.close()

fff = open(r"D:\python\a.txt", "w")
fff.write('eieio~')
fff.write('杂鱼~')
fff.close()

fff = open(r"D:\python\a.txt", "r")
for line in fff:
    print(line,end='')
fff.close()

fff = open(r"D:\python\a.txt", "a")
fff.write("添饭")
fff.close()
fff = open(r"D:\python\a.txt", "r")
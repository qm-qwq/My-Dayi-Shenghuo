# # 英文名自动正确书写
# Y = input("请输入一串英文 会自动首字母大写其他字母小写")
# y = Y.capitalize()
# print(f"Hi~ o(*￣▽￣*)ブ{y}")

# # 判断分数
# f = int(input("请输入分数（1——100）自动判断你的等级"))
# if int(f) >= 90:
#     print("A")
# elif 80<= int(f) < 90:
#     print("B")
# elif 70<= int(f) < 80:
#     print("C")
# elif 60<= int(f) < 70:
#     print("D")
# else:
#     print("E")

# # 计算1+到100结果
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 1
#     print(sum)

# # 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}",end="\t")
#     print()
# # 随机数小游戏
#
# print("欢迎猜数字"
#           "我想好了一个1-100的数字 来猜"
#           "10次机会")
#
# while True:
#     import random
#
#     s = random.randint(1, 100)
#
#     print("不服气就再来")
#     guess_count = 0
#
#     while True:
#         try:
#             m = int (input("请输入数字"))
#         except:
#             print("请输入数字整数")
#             continue
#         guess_count += 1
#         if guess_count == 10:
#             print("次数限制 杂鱼")
#             print(f"一共猜了{guess_count}次杂鱼")
#             break
#         if  m < s:
#             print("猜小了╰(*°▽°*)╯")
#
#         elif m > s:
#             print("猜大了捏(*^▽^*)")
#
#         else :
#             print("猜对了喵(≧∇≦)ﾉ")
#             print(f"一共猜了{guess_count}次杂鱼")
#             break
#     print("游戏结束 请输入y/n 决定再次游玩")
#     x = input()
#     if x == "n":
#         break

# # 学生管理
# print("---学生名单管理系统---"
#       "1.添加学生"
#       "2.删除学生"
#       "3.显示所有学生"
#       "4.退出")
# student = []
# while True:
#     f = input("请选择操作(1-4)")
#     if f== "1":
#         a = input('添加name')
#         student.insert(0, a)
#     elif f== "2":
#         b = input('删除name')
#         student.remove(b)
#     elif f== "3":
#         print(f"{student}")
#     elif f== "4":
#         break
#     else:
#         print("请检查输入是否正确")

# 1到10平方列表不同方法对比
# for i in range(1,11):
#     s = i**2
#     print(s)
#
# a = [b**2 for b in range(1,11)]
#
# print(a)
# x = [y**2 for y in range(1,11) if y%2==0]

# 索引和解包
student = ("苯",23,"计算机系")
name = student[0]
age = student[1]
zhuanye = student[2] #索引
name,age,zhuanye = student#解包
print(f"{name},{age},{zhuanye}")













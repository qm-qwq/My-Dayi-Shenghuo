# def s(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(s(1,3,4,5,6,8,10))
# print(s(1,2))
# print(s())
# print(s(1))

# def s(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}, {value}")
# print(s(name = "张三", age = 18, city = "北京"))
# s(name = "张三", age = 18, city = "北京")

# def f(a,b,*args,**kwargs):
#     print(f"a = {a}, b = {b}, "
#           f"args = {args},"
#           f"kwargs = {kwargs}")
# f(1,2,3,4,12,2,3,4,x = 5,y=6,z=7)

# x = 10
# def m():
#     global x # 在函数里面修改外面的变量
#     x = 20
# m()
# print(x)

# def s(*args):
#     n = 0
#     for arg in args:
#         n += arg
#     return n
# print(s(1,2,3))
# print(s(1.1,2.2,3.3))
# print(s())
#
# a = 100
# def test():
#     a = 200
#     print(a)
# test()
#      # 200





# 匿名函数
# x = lambda x, y: x + y
# print(x(1,2))
#
# n = [1,2,3,4,5]
# s = map(lambda i: i * 2, n)
# print(list(s))   # 要写list才能打印
#
# # map(函数, 对象) 让所有对象都经历一遍函数洗礼
# # filter(函数, 对象) 筛选对象
#
# nn = [1,2,3,4,5,6]
# ss = filter(lambda i: i % 2 == 0, nn)
# print(list(ss))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# m = filter(lambda i: i % 2 == 0, numbers)
# print(list(m))





# def ff(n):
#     if n == 1:
#         return 1
#     else:
#         return n * ff(n - 1)
# print(ff(8))
#
# # 用循环
# def ff2(n):
#     mms = 1
#     for i in range(2, n + 1):
#         mms *= i
#     return mms
# print(ff2(8))







# try:
#     # 可能引发异常的代码
#     代码块
# except 异常类型:   except Exception as e:优先
#     # 发生该异常时执行的代码
#     处理代码


# try:
#     number = int(input("Enter a number: "))
#     print(f'{number}')
# except Exception as e:
#     print("Please enter a number")
#     print(f"错误类型：{type(e).__name__}")  # 错误名字
#     print(f"错误详情：{e}")                 # 错误原因
#     # 也可以直接打印e，最省事
#     # print(e)

# try:
#     num = int(input("请输入数字："))
# except ValueError:
#     print("输入无效")
# else:
#     print(f"你输入了{num}，平方是{num**2}")
# finally:
#     print("程序结束")

# raise 主动抛出异常
# def p(n):
#     if n < 0:
#        raise ValueError("CUOWU")
#
# try:
#     p(-5)
# except ValueError:
#     print("代码错误")






# while True:
#     try:
#         i = input("请输入一个数,q退出循环")
#     except :
#         print("请正确输入")
#         continue
#     if i == "q":
#             break
#     if True:
#         print(int(i) ** 2)
#         break

while True:
    i = input("请输入一个数,q退出循环")
    if i == "q":
        break
    try:
        a = int(i) # 判断放try里面 input永远是ture  try无意义
        print(int(i) ** 2)
        break
    except:
        print("请正确输入")
























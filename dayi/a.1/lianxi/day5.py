# def add(a,b):
#     return a+b
#
# print(add(3,4))
# print(add(5,5))
# print(add(5,4))
#
# def g(n,m="xx"):
#     print(f"{n},{m}")
#
# g("你好","ss")
# g("hi",)  # 提前定义不会报错
#
# def s():
#     print("hello")
# r = s()


rnp = int(input('判段是否为闰年'))
def rn(b):
    if b % 4 == 0 and b % 100 != 0 or b % 400 == 0 :
        print("ture")
    else:
        print("flase")

rn(rnp)
# def()里面的参数是他自己的 纯爱
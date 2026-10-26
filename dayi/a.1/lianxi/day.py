# for ch in "python":
#     print(ch)
# fruits = ["苹果","香蕉","橙子"]
# for fruit in fruits:
#     print(f"我喜欢吃{fruit}")
# try:
#     m = int(input())
# except:
#     print("baka")
# empty_list = []
# nunbers = [1,2,3,4,5]
# names = ["alice","bob","charlie"]
# mixed = [10,"hello",3.14,True]
# chare = list ("abc")
# fruits = ["苹果","香蕉","橙子","葡萄"]
# print(fruits[0])
# print(fruits[2])
# print(fruits[-1])
# print(fruits[-2])
# fruits[1] = "草莓"
# print(fruits)
# fruits.append("耙耙柑")
# fruits.insert(1,"草莓")
# fruits.extend(["梨子","芒果"])
# print(fruits)
# fruits.remove("草莓")
# last = fruits.pop()
# del fruits[0]
# print(fruits)
#
# nums = [0,1,2,3,4,5,6,7,8,9]
# print(nums[2:5])
# print(nums[:4])
# print(nums[5:])
# print(nums[::2])
# print(nums[::-1])
# numss = [3,1,4,5,2,1,9]
# # numss.sort()
# # print(numss)
# new_numss = sorted(numss)
# print(new_numss)
# print(numss)

# names = ["alice",'bob',"charlie"]
# unames = [name.upper() for name in names]
# results = [i if i % 2 == 0 else -1 for i in range(5)]
# coords =[(x,y) for x in range (3) for y in range (2)]
# nums = [3,1,4,1,5,9,2,6,5]
# print(nums.count(1)) #数数1有几次
# print(nums.index(4))#查找位置，从0开始数数
# nums.reverse()#反转
# print(nums)
# o = [1,2,3]
# new = o.copy()
# new[0] = 4
# print(new)
empty = (3,) #加逗号，不加就是int，加了才是元组 单个的情况
# 多个元素不加括号也可以
p = (3,4)
x,y = p
print(x,y)

a,b = 13,2
a,b = b,a
print(a,b)

t = (1,2,3,4,5,5)
s,*m = t
print(s,m)

_,d,_ = (19,34,52)
print(d)













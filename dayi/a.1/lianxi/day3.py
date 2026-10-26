# # 集合
# s1 = {1,2,3,2,1}
# # s2 = set([1,2,2,3])
# s3 = set ('hello')
# air_set = set()
# not_set ={}
#
# s1.add(4)
# s1.remove(3)
# s1.discard(19) #不会报错
# POPPed = s1.pop()
# print(POPPed)
# print(s1)
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# print(A & B)           # 交集: {3, 4}
# print(A | B)           # 并集: {1, 2, 3, 4, 5, 6}
# print(A - B)           # 差集: {1, 2}
# print(B - A)           # 差集: {5, 6}
# print(A ^ B)           # 对称差集: {1, 2, 5, 6}
#
# print({1,2} <= A)      # True
# print({1,5}.isdisjoint(A))  # False（因为1在A中）     不相交s1.isdisjoint(s2)
# # 集合推导式
# sss = {x**2 for x in range(5)}
# print(sss)
# www = {x for x in range(10) if x % 2 ==0}
# print(www)
# e = {ch for ch in "hello world" if ch.isalpha()}
# print(e)


list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]
s1 = set(list1)
s2 = set(list2)
s = s1 & s2
print(s)
s3 = list(s)
print(s3)
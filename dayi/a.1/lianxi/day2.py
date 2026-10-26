# # 字典
# empty = {}
# person = {"name":"张三","age":18,"city":"beijing"}
# person2 = dict(name="李四",age=20)   #键不要引号
# pairs = [("name","王五"),("age",22)]
# person3 = dict(pairs)
# print(person["name"])
# print(person.get("name"))
# print(person.get("namww"))  #找不到值也不会报错 （和直接打印的区别）
# print(person.get("namww","weizhi"))
# person2["city"] = "tianjing" #不存在就添加
# print(person2)
# person["city"] = "henan" #存在就改
# print(person)
# person.update({"name":"zs","gender":"nan"})
# # print(person)
# # del person["age"]
# # print(person)
# # city = person.pop("city")
# # print(city)
# # print(person)
# # person.clear()
# # print(person)
# for key in person.keys():
#     print(key)
# for value in person.values():
#     print(value)
# for key,values in person.items():
#     print(f"{key}:{values}")
#
#
#
# a = input("请输入英语进行统计")
# b = a.lower()
# count = {}
# for c in b:
#     if c.isalpha():
#         count[c] = count.get(c,0)+1
# print("结果：")
# for w,d in count.items():
#     print(f"{w}:{d}")
#
#
#
#   s = "hello"
#   xha = {c:s.count(c) for c in set(s)}
#   print(xha)      #和上面那个挺像
# o = {'a':1,'b':2,'c':3,'d':4,'e':5}
# r = {w:y for y,w in o.items() }
# print(r)
# words = ['apple','banana','orange','grape','mango']
# word = {w : len(w) for w in words if len(w) >5}
# print(word)
#     .setdefault() 和 .get区别是 这玩意返回值之后看你没有就给你补上了
# d = {'a':1}
# v = d.setdefault("b",2)
# print(d)
# print(v)
# v2 = d.setdefault("a",99)
# print(d)
# print(v2)
# s = 'hellocosplay'
# count = {}
# for i in s:
#     count[i] = count.setdefault(i,0)+1
# print(count)
# from collections import defaultdict
# # dd = defaultdict(int)
# # dd['a'] +=1
# # print(dd['a'])
# # print(dd['b'])
# aa = defaultdict(list)
# aa['colors'].append('red')
# print(aa['colors'])
# def e():
#     return "n/a"
# ss = defaultdict(e)
# print(ss['miss'])
# d1 = {'a':1,'b':2}
# d2 = {'c':3,'d':4}
# # d1.update(d2)
# # print(d1)
#
#
# merged = {**d1,**d2}
# print(merged)
# print(d1)
#
# m = d1 | d2
# print(m)

dict1 = {'a':1,'b':2,'c':3}
dict2 = {'b':4,'d':3}
dict1.update(dict2)
print(dict1)
m = dict1 | dict2
print(m)
s = {**dict1,**dict2}
print(s)
dict1 |= dict2
print(dict1)
import re
# text = "我的电话号码是 123-4567，你的号码是 987-6543。"
#
# print(re.findall(r"\d{3}",text))
#
# match = re.search(r"\d{3}-\d{4}",text)
# if match:
#     print(match.group())
# new =re.sub(r"\d{3}-\d{4}","123456",text)
# print(new)
#
#
# text = "联系我: alice@example.com 或 bob@163.com"
# emails = re.findall(r"\w+@\w+\.\w+", text)
# print(emails)


text = """张三，电话：13812345678，邮箱：zhangsan@qq.com。
        李四，电话：010-87654321，邮箱：lisi@163.com。
        王五，电话：18888888888，邮箱：wangwu@gmail.com。"""
match = re.findall(r"\d{11}|\d{3,4}-\d{7,8}",text)

print(match)


emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)
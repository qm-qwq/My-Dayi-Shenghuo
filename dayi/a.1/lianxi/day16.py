# # # class Task:
# # #     def __init__(self,name,completed = False):
# # #         self.name = name
# # #         self.completed = completed
# # #     def __str__(self):
# # #         if self.completed:
# # #             return f"[✔]{self.name}"
# # #         else:
# # #             return f"[]{self.name}"
# # # class TodoList:
# # #     def __init__(self):
# # #         self.tasks = []
# # #     def add(self,name):
# # #         self.tasks.append(Task(name))
# # #         return self.tasks
# # #     def delete(self,index):
# # #         self.tasks.pop(index)
# # #         return self.tasks
# # #     def show(self):
# # #         for i,take in enumerate(self.tasks,1):
# # #             print(f"{i}. {take}")
# # #     def complete(self,index):
# # #         self.tasks[index].completed = True
# # #         return self.tasks
# # # t = TodoList()
# # # while True:
# # #     print("---待办清单，用类重构---\n")
# # #     print("1.添加任务")
# # #     print("2.删除任务")
# # #     print("3.显示所有任务")
# # #     print("4.标记任务完成")
# # #     print("5.退出")
# # #     n = input("请输入数字（1-5）")
# # #
# # #     if n == "1":
# # #         m = input("请输入文本")
# # #         t.add(m)
# # #         print()
# # #     elif n == "2":
# # #         x = int(input("请输入要删除的任务"))
# # #         t.delete(x - 1)
# # #         print()
# # #     elif n == "3":
# # #         t.show()
# # #     elif n == "4":
# # #         y = int(input("请输入要标记完成的任务"))
# # #         t.complete(y - 1)
# # #         print()
# # #     elif n == "5":
# # #         print("baibai")
# # #         break
# # #     else:
# # #         print("请正确输入")
# # #
# #
# #
# #
# # import requests
# # print("requests 导入成功！版本：", requests.__version__)
# # import requests
# #
# #
# # # 用一个公开的、国内可访问的API
# # url = "https://jsonplaceholder.typicode.com/posts/1"
# # response = requests.get(url)
# #
# # if response.status_code == 200:
# #     print("请求成功！")
# #     print(response.json())
# # else:
# #     print(f"请求失败，状态码：{response.status_code}")
# #
# from asyncio import events
#
# import requests
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# print(response.status_code)
# print(response.text)
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# data = response.json()
# print(type(data))
# print(len(data))
# print(data)
#
# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)
# events = response.json()
# for i, post in enumerate(events[:5],1):
#     print(f"{i}. 用户{post['userId']}的文章：{post['title']}")




import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print(response.status_code)
print(response.text)
data = response.json()
print(type(data))
events = response.json()
for i, event in enumerate(events[:5],1):
    print(f"{i}. event{"userID"} - {event["title"]}")










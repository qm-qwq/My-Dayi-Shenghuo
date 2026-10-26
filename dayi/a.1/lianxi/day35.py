# from datetime import datetime
# class Note:
#     def __init__(self,title,content,tags = None): # 标题，内容，标签（默认是Nome）
#         self.id = None  # 给笔记留一个空的id属性 后面有用
#         self.title = title
#         self.content = content
#         self.create_time = datetime.now()
#         self.tags = tags if tags else [] #三元表达式 如果是就用tags 如果不是就空列表
#                     #条件正确返回的值 ， 条件 ， 条件错误返回的值
#     def __str__(self): #打印结果
#         return f"[{self.id}] {self.title} - {self.create_time.strftime('%Y-%m-%d %H:%M:%S')}"
#
# class NoteManager:
#     def __init__(self):
#         self.notes = []
#         self.next_id = 1 #第一条笔记从1开始 自动递增
#
#     def add_note(self,title,content,tags=None):
#         note = Note(title,content,tags) #接收用户传入的数据保存里面
#         note.id = self.next_id
#         self.notes.append(note) #把新增的这条放列表里面
#         self.next_id += 1
#         return note.id
#     def list_notes(self):
#         for note in self.notes:
#             print(note)
#     def get_note(self,note_id):
#         for note in self.notes:
#             if note.id == note_id:
#                 return note
#             return None #找不到返回空
#     def delete_note(self,note_id):
#         note = self.get_note(note_id) #找的时候已经遍历了
#         if note:
#             self.notes.remove(note)
#             return True
#         return False
#






from datetime import datetime


class Day__:
    def __init__(self, name,nerong,biaoqian = None):
        self.id0 = None
        self.name = name
        self.nerong = nerong
        self.data_time = datetime.now()
        self.biaoqian = biaoqian if biaoqian else []

    def __str__(self):
        return f"[{self.id0}] {self.name} - {self.data_time.strftime('%Y-%m-%d %H:%M:%S')}"

class Day_guanli:
    def __init__(self):
        self.id0 = 1
        self.datee = []

    def add(self,name,nerong,biaoqian = None):
        datee = Day__(name,nerong,biaoqian)
        datee.id0 = self.id0
        self.datee.append(datee)
        self.id0 += 1
        return datee.id0

    def list(self):
        for datee in self.datee:
            print(datee)
    def cha(self,id0):
        id0 = int(id0)
        for datee in self.datee:
            if datee.id0 == id0:
                return datee
        return None
    def delete(self,id0):
        dateee = self.cha(id0)
        if dateee:
            self.datee.remove(dateee)
            return True
        return False

m = Day_guanli()
ad1 = m.add("Python学习笔记", "今天学了类和对象", ["学习", "编程"])
ad2 = m.add("生活备忘录", "明天要交水电费")
while True:

    i = input("请输入文本 1添加 2查看 3删除 4退出")
    if i == "1":
        c = input("请输入至少一个标题和内容")
        name,nerong =c.split(",")
        d = m.add(name,nerong)
        print("ok")
    if i == "2":
        s = input("输入数字索引")
        n = m.cha(s)
        print(n)
    if i == "3":
        s1 = input("输入数字删除")
        m.delete(s1)
        print("ok")
    if i == "4":
        break






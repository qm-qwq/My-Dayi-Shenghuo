#先创建一个json文件
import json
import os
from datetime import datetime


DATA_FILE = 'notes.json'

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,'r',encoding='utf-8') as f:
        return json.load(f) # 把json转化为当地也就是python 的文件格式

def save_notes(notes):
    with open(DATA_FILE,'w',encoding='utf-8') as f:
        json.dump(notes,f,ensure_ascii=False,indent=2)
                #dump 转存 存储 （要保存的数据 ，文件 f是文件 不是动作”w“才是动作 防止中文乱码 自动分段）
def get_notes(notes):
    if not notes:
        return 1
    return max(note["id"] for note in notes) + 1 #遍历找出最大的id 再去加1

def add_note(title, content, tags=None):
    notes = load_notes()
    new_id = get_notes(notes)
    note = {
        "id": new_id,
        "title": title,
        "content": content,
        "created_at":datetime.now().isoformat(), #.isoformat() 把时间变成固定标准格式的字符串
        "tags": tags or []
    }
    notes.append(note)
    save_notes(notes)
    print(f"笔记已添加，ID: {new_id}")
def list_notes():
    notes = load_notes()
    if not notes:
        print("暂无笔记")
        return
    for note in notes:
        print(f"[{note['id']}]{note['title']}({note['created_at'][:10]})") #完整的时间

def delete_note(note_id):
    notes = load_notes()
    now_notes = [n for n in notes if n["id"] != note_id] #如果不等于 那就是新的数据
    if len(now_notes) == len(notes): #如果新旧笔记长度一样 那就是没有找到
        print(f"未找到 ID 为 {note_id} 的笔记")
        return
    save_notes(now_notes) #要不然保留原始的 只删掉你输入的
    print(f"已删除 ID: {note_id}")


def main():
    while True:
        print("\n--- 个人笔记系统 ---")
        print("1. 添加笔记")
        print("2. 列出所有笔记")
        print("3. 删除笔记")
        print("4. 退出")
        choice = input("请选择").strip() #去掉空格的
        if choice == "1":
            title = input("标题: ")
            content = input("内容: ")
            tags = input("标签（逗号分隔）: ").split(",")
            tags = [t.strip() for t in tags if t.strip()] #如果t去掉空格后还是有意义的 那就保留
            add_note(title, content, tags)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            try:
                nid = int(input("请输入要删除的笔记ID: "))
                delete_note(nid)
            except ValueError:
                print("ID必须是数字")
        elif choice == "4":
            print("再见！")
            break
        else:
            print("无效输入")


def search_note(keyword):  # 按照标题或者内容搜
    notes = load_notes()
    key = keyword.lower()
    results = []
    for note in notes:
        if key in note['title'].lower() or key in note['content'].lower():
            results.append(note)
    return results


def search_tag(tag):
    notes = load_notes()
    key = tag.lower()
    results = [note for note in notes if any(t.lower() == key for t in note.get) in note['tags']]
    # note.get()拿到标签要不然就返回空列表
    # any（）只要有一个满足就选中
    # t.lower() == key 改小写
    # 在笔记本里面选中所有满足的改成小写 挺好查找是否在tags里面
    return results



if __name__ == '__main__':
    main()

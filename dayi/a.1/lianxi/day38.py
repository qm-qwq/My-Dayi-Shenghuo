import json
import os
from datetime import datetime


DATA_FILE = 'notes.json'

#------------------数据-------------------------
def load_notes():
    if not os.path.exists(DATA_FILE):
        sample = [
            {"id": 1, "title": "学习Python", "content": "今天学习了函数", "created_at": datetime.now().isoformat(),
             "tags": ["编程"]},
            {"id": 2, "title": "购物清单", "content": "牛奶、面包", "created_at": datetime.now().isoformat(),
             "tags": ["生活"]}
        ]
        save_notes(sample)
        return sample
    with open(DATA_FILE,"r",encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(notes,f,ensure_ascii=False,indent=2) #写入文件

#---------------业务------------------
def list_notes(notes):
    if not notes:
        print("暂无笔记")
        return
    for n in notes:
        tags = f"[{','.join(n["tags"])}]" if n["tags"] else ""
                # ','.join(n['tags' 用逗号连接字符串 变成字符串的形式 转格式
        print(f"{n['id']},{n['title']}{tags}({n["created_at"][:10]}")

def edit_note_by_id(notes, note_id, new_title=None, new_content=None, new_tags=None):
    for note in notes:
        if note["id"] == note_id:
            if new_title is not None:
                note["title"] = new_title
            if new_content is not None:
                note["content"] = new_content
            if new_tags is not None:
                note["tags"] = new_tags
        note['updated_at'] = datetime.now().isoformat()
        save_notes(note)
        print(f"笔记 ID {note_id} 已更新")
        return True
    print(f"未找到 ID {note_id}")
    return False

#--------------------交互-------------------

def main():
    notes = load_notes()
    print("当前笔记列表：")
    list_notes(notes)
    try:
        nid = int(input("\n请输入要编辑的笔记ID: "))
        # 查找是否存在
        target = next((n for n in notes if n['id'] == nid), None)
# next(..., None)找到第一个符合条件的笔记，立刻返回它 如果找不到，就返回 None（不会报错）
        if not target:
            print("ID不存在")
            return
        print(f"当前内容：{target['title']} - {target['content'][:30]}...")
        new_title = input("新标题（直接回车保留原值）: ").strip()
        new_content = input("新内容（直接回车保留原值）: ").strip()
        new_tags_str = input("新标签（逗号分隔，直接回车保留原值）: ").strip()
        # 处理输入
        if new_title == "":
            new_title = None
        if new_content == "":
            new_content = None
        if new_tags_str == "":
            new_tags = None
        else:
            new_tags = [t.strip() for t in new_tags_str.split(",") if t.strip()]
        edit_note_by_id(notes, nid, new_title, new_content, new_tags)
        # 显示更新后的列表
        print("\n更新后的笔记列表：")
        list_notes(load_notes())

    except ValueError:
        print("ID必须是数字")

if __name__ == "__main__":
    main()


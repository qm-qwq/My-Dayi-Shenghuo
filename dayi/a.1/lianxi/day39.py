import json
import os
from datetime import datetime

DATA_FILE = "notes.json"

# ---------- 数据加载（如果没有则创建示例数据）----------
def load_notes():
    if not os.path.exists(DATA_FILE):
        sample = [
            {"id": 1, "title": "学习Python函数", "content": "函数定义、参数、返回值", "created_at": datetime.now().isoformat(), "tags": ["编程", "Python"]},
            {"id": 2, "title": "购物清单", "content": "牛奶、面包、鸡蛋", "created_at": datetime.now().isoformat(), "tags": ["生活"]},
            {"id": 3, "title": "Python 装饰器", "content": "装饰器是闭包的一种应用", "created_at": datetime.now().isoformat(), "tags": ["编程", "进阶"]},
            {"id": 4, "title": "周末计划", "content": "看电影、运动", "created_at": datetime.now().isoformat(), "tags": ["生活"]},
            {"id": 5, "title": "数据分析入门", "content": "pandas 读取 CSV", "created_at": datetime.now().isoformat(), "tags": ["数据"]}
        ]
        save_notes(sample)
        return sample
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

# ---------- 搜索功能 ----------
def search_by_keywords(notes, keyword_str):
    """多关键词（空格分割），所有词都出现在标题或内容中（AND）"""
    keywords = keyword_str.lower().split()
    results = []
    for note in notes:
        text = (note['title'] + note['content']).lower()
        if all(k in text for k in keywords):
            results.append(note)
    return results

def search_by_tag(notes, tag):
    tag_lower = tag.lower()
    return [n for n in notes if any(t.lower() == tag_lower for t in n.get('tags', []))]

# ---------- 分页显示 ----------
def display_paged(notes, title="搜索结果", page_size=3):
    total = len(notes)
    if total == 0:
        print("没有找到笔记")
        return
    start = 0
    while start < total:
        end = min(start + page_size, total)
        print(f"\n-----------{title}(第{start//page_size + 1}页,共{total}条---------")
        for i in range(start, end): #从0开始索引所以最后一个开没关系 比如结尾是7 那从0开始的索引到6刚好是7个数
            n = notes[i]
            tags_str = f"[{','.join(n['tags'])}]" if n['tags'] else ""
            print(f"{n['id']}. {n['title']} {tags_str}")
            print(f"   {n['content'][:50]}")
            print(f"   时间：{n['created_at'][:10]}")
        start = end #结束是end 才能保留记忆继续执行 比如之前是3 下次是在3 的基础上而不是从0
        if start < total:
            cmd = input("按 Enter 继续下一页，输入 q 退出：").strip().lower()#按enter结束是因为直接往下运行
            if cmd == 'q':
                break
def main():
    notes = load_notes()
    while True:
        print("\n=== 笔记搜索与浏览 ===")
        print("1. 关键词搜索（支持多个词，空格分隔）")
        print("2. 按标签搜索")
        print("3. 显示所有笔记（分页）")
        print("4. 退出")
        choice = input("请选择: ").strip()
        if choice == '1':
            kw = input("请输入关键词（多个用空格分隔）: ").strip()
            if kw:
                results = search_by_keywords(notes, kw)
                display_paged(results, f"包含 '{kw}' 的笔记")
            else:
                print("关键词不能为空")
        elif choice == '2':
            tag = input("请输入标签: ").strip()
            if tag:
                results = search_by_tag(notes, tag)
                display_paged(results, f"标签 '{tag}' 的笔记")
            else:
                print("标签不能为空")
        elif choice == '3':
            display_paged(notes, "所有笔记")
        elif choice == '4':
            print("再见")
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 这两行都是 **“说明性注释”**：
# 第一行：给 Linux/macOS 系统看的，指定用 python3 运行脚本
# 第二行：给 Python 解释器看的，指定文件编码为 UTF-8
import json
import os
import argparse #让命令行控制代码
from datetime import datetime

from pyparsing import results

D = "notes0.json"
#------------------------存储层----------------------------
def load_notes():
    if not os.path.exists(D): #os.path.exists(文件路径) 判断这个文件/文件夹存在不 返回布尔值
        return []
    with open(D,"r",encoding="utf-8") as f:
        return json.load(f) #吧f文件转为当地的列表

def save_notes(notes):
    with open(D,"w",encoding="utf-8") as f:
        json.dump(notes,f,ensure_ascii=False,indent=2) #json.dump 把列表转化为json的格式存D里面 因为f是方式
                    #ensure_ascii=False 让中文正常显示 indent=2文件自动换行缩进

def next_id(notes):
    return max((n["id"] for n in notes),default = 0) + 1 #default是当一条都没有的时候返回0

#-------------------业务逻辑--------------------------
def add_note(title,content,tags_str):
    notes= load_notes()
    tags = [t.strip() for t in tags_str.split(",")] if tags_str else [] #strip 除空
    note = {
        "id":next_id(notes),
        "title":title,
        "content":content,
        "created_at":datetime.now().isoformat(), #.idodormat转化为标准的时间
        "tags":tags
    }
    notes.append(note)
    save_notes(notes)
    print(f"笔记添加成功，ID：{note["id"]}")

def list_notes(page_size=5):
    notes= load_notes()
    if not notes:
        print("没笔记")
        return
    total = len(notes)
    start = 0
    while start < total:
        end = min(start + page_size,total)
        print(f"\n-----------笔记列表（第{start//page_size + 1}页，共{total}条-----------")
        for i in range(start,end):
            n = notes[i]
            tags = f"[{','.join(n['tags'])}]"if n['tags'] else "" #对字符串拼接
            print(f"{n['id']}.{n['title']}{tags}({n['created_at'][:10]})")
            print(f"{n['content'][:60]}")
        start = end
        if start < total:
            cmd = input("按 enter 继续，输入 q 退出：").strip().lower()
            if cmd == "q":
                break

def del_note(note_id):
    notes= load_notes()
    new_notes = [n for n in notes if n["id"] != note_id] #把不等于输入的留下来 生成新列表
    if len(new_notes) == len(notes):
        print(f"未找到ID为{note_id}的笔记")
        return
    save_notes(new_notes)
    print(f"已删除ID：{note_id}")

def edit_note(note_id,title=None,content=None,tags_str=None): #可传可不传
    notes= load_notes()
    for n in notes:
        if n["id"] == note_id:
            if title is not None:
                n["title"] = title
            if content is not None:
                n["content"] = content
            if tags_str is not None:
                n["tags"] = [t.strip() for t in tags_str.split(",")if t.strip()]
            n["created_at"] = datetime.now().isoformat()
            save_notes(notes)
            print(f"笔记ID{note_id}已更新")
            return
    print(f"未找到ID{note_id}")

def search_by_keywords(keyword_str):
    notes= load_notes()
    keywords = keyword_str.lower().split()
    results = []
    for n in notes:
        text = (n["title"] + n["content"]).lower()
        if all(k in text for k in keywords):
            results.append(n)
    return results

def search_by_tag(tag):
    notes= load_notes()
    tag_lower = tag.lower()
    return [n for n in notes if any(t.lower() == tag_lower for t in n.get("tags",[]))]

def show_results(notes,title):
    if not notes:
        print("没有找到匹配的")
        return
    total = len(notes)
    print(f"\n---{title}(共{total}条)---")
    for n in notes:
        tags = f"[{','.join(n['tags'])}]" if n['tags'] else ""
        print(f"{n['id']}.{n['title']}{tags}")
        print(f"{n['content'][:60]}")
        print(f"{n['created_at'][:10]}\n")

#-----------------命令行入口-----------------
def main():
    parser = argparse.ArgumentParser(description="个人笔记系统-命令行版本") #创建有一个命令行解析器 用 -h显示说明文字description
    subparsers = parser.add_subparsers(dest="cmd",help="子命令")
                    #这个给程序加子命令 让在cmd里面用
    #add_argument 添加一个选项 subparsers.add_parser 新增一个子命令
    #add
    p_add = subparsers.add_parser("add",help="添加笔记")
    p_add.add_argument("-t","--title",requird = True,help="标题") #requird = True霸道系统强制爱 必须写标题
    p_add.add_argument("-c", "--content", required=True, help="内容")
    p_add.add_argument("-g", "--tags", default="", help="标签，逗号分隔") #default="" 不填就是空字符

    #list
    subparsers.add_parser("list",help="列出所有笔记（分页）")

    #delete
    p_del = subparsers.add_parser("delete",help="删除笔记")
    p_del.add_argument("id",type=int,help="笔记ID")

    #edit
    p_edit = subparsers.add_parser("edit",help="编辑笔记")
    p_del.add_argument("id",type=int,help="笔记ID")
    p_edit.add_argument("-t", "--title", help="新标题")
    p_edit.add_argument("-c", "--content", help="新内容")
    p_edit.add_argument("-g", "--tags", help="新标签，逗号分隔")

    #search
    p_search = subparsers.add_parser("search",help="关键词搜索（支持多个 )")
    p_search.add_argument("keyword",help="关键词，多个用空格分隔")

    #tag
    p_tag = subparsers.add_parser("tag",help="按照标签搜索")
    p_tag.add_argument("tag",help="标签名")

    args = parser.parse_args() #读取输入的东西 翻译器

    if args.cmd == "add":
        add_note(args.title,args.content,args.tags)
    elif args.cmd == "list":
        list_notes()
    elif args.cmd == "delete":
        del_note(args.id)
    elif args.cmd == "edit":
        edit_note(args.id,args.title,args.content,args.tags_str)
    elif args.cmd == "search":
        results = search_by_keywords(args.keyword)
        show_results(results,f"包含’{args.keyword}‘的笔记")
    elif args.cmd == "tag":
        results = search_by_tag(args.tag)
        show_results(results, f"包含’{args.tag}‘的笔记")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

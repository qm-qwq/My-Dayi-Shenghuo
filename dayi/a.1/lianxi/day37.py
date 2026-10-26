import argparse #让程序可以用命令行指令运行

from lianxi.day36 import add_note, list_notes, delete_note,search_note


def main():
    parser = argparse.ArgumentParser(description = "个人笔记系统") #创建命令解析器 就是起名字
    subparsers = parser.add_subparsers(dest = "command",help = "子命令")# 这个有用
            #创建子命令 add /list/delete） 存在 args.command 里 就是上面那个dest 让程序用命令执行
    # 添加笔记
    parser_add = subparsers.add_parser('add',help = "添加笔记")
    parser_add.add_argument("--title",required = True) #加了一个必填输入框 required=True：这个框必须填！不填的话程序会直接报错，不让运行
    parser_add.add_argument("--content",required = True)
    parser_add.add_argument('--tags', help='逗号分隔标签') # 没写 required=True，说明用户可以不填这个
    # 添加笔记
    parser_list = subparsers.add_parser('list',help="列出所有笔记")
    # 删除笔记
    parser_del = subparsers.add_parser('delete', help='删除笔记')
    parser_del.add_argument('id',type = int) #因为这个必须填一个数 所以不用上面的ture #有--的为非必须的 后面加ture就是必须
    # 搜索（关键词）
    parser_search = subparsers.add_parser('search', help='按关键词搜索')
    parser_search.add_argument('keyword')
    # 按标签搜索
    parser_tag = subparsers.add_parser('tag', help='按标签搜索')
    parser_tag.add_argument('tag')

    args = parser.parse_args() #解析官 会把结果存args里面 具体如下

    if args.command == "add":
        tags = args.tags.split(",") if args.tags else [] #判断有没有标签 有的话就分开没有级就空列表
        add_note(args.title,args.content,tags)
    elif args.command == "list":
        list_notes()
    elif args.command == "delete":
        delete_note(args.id)
    elif args.command == "search":
        result = search_note(args.keyword)
        if result:
            for note in result:
                print(f"[{note['id']}] {note['title']} - 标签: {note.get('tags', [])}")
        else:
                print("未找到该标签的笔记")
    else:
        parser.print_help()


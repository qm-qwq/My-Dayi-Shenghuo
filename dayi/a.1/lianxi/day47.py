#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os # 和系统打交道
import argparse # 解析命令行参数
import glob #查文件路径的



def get_file(directory,ext = None): #ext文件后缀
    pattern = "*" if ext is None else f"*{ext}" #三元表达式 如果不传惨就是原来 如果传就是参数后面跟上传的后缀
    files = glob.glob(os.path.join(directory,pattern)) # glob.glob()查找文件路径返回列表 里面那个拼接路径
    return [f for f in files if os.path.isfile(f)] #判断是不是文件

def generate_new_name(old_path,index,prefix,suffix,number,start,digits,pattern):
    dirname = os.path.dirname(old_path) # dirname 拿走路径里面的文件夹部分
    basename = os.path.basename(old_path) # basename 只拿文件名
    name,ext = os.path.splitext(basename) # splitext()把括号里面的拆成名字加后缀

    if pattern: # 自定义格式
        num_str = f"{index:0{digits}d}" if number else "" # 自动补零 {digits}是位数 0d是补零 限定位数不够的补零
        new_name = pattern.format(name = name, num = num_str, ext = ext) # 。format 按顺序填空比input方便
    else:
        # 默认规则：前缀 + 原名称 + 后缀 + 序号 + 扩展名
        num_part = f"_{index:0{digits}d}" if number else ""
        new_name = f"{prefix}{name}{suffix}{num_part}{ext}"

    return os.path.join(dirname,new_name)

def main():
    parser = argparse.ArgumentParser(description="批量重命名文件（）") #ArgumentParser 命令解析器（说明书+接收）
                # description 介绍
    parser.add_argument("--directory","-d",default=".",help="目标目录，默认为当前目录")
                # defafult 默认值 .是当前目录的意思 add_argument加设置
    parser.add_argument("--ext","-e",help="只处理指定扩展名的文件（如.txt）")
    parser.add_argument("--prefix","-p",default="",help="添加前缀")
                # default="" 不加东西 前面是文件夹默认所以是“.”
    parser.add_argument("--suffix","-s",default="",help="添加后缀")
    parser.add_argument("--number","-n",action="store_true",help="添加序号") #action 设置 n就是true
    parser.add_argument("--start", type=int, default=1, help="序号起始值，默认1")
    parser.add_argument("--digits", type=int, default=2, help="序号位数，默认2")
    parser.add_argument("--pattern", help="自定义格式，如 '{name}_{num}{ext}'，优先级高于前缀后缀")
    parser.add_argument("--execute", action="store_true", help="实际执行重命名（否则只预览）")
    parser.add_argument("--yes", "-y", action="store_true", help="跳过确认提示（需与 --execute 同时使用）")

    args = parser.parse_args() #接收器

    files = get_file(args.directory,args.ext)
    if not files:
        print("没有找到符合条件的文件。")
        return

    files.sort()
    changes = []
    for idx,old_path in enumerate(files,start=args.start):
        new_path = generate_new_name(
                old_path, idx,
                prefix=args.prefix, suffix=args.suffix,
                number=args.number, start=args.start, digits=args.digits,
                pattern=args.pattern
        )
        changes.append((old_path,new_path)) # 添加的是元组所以是俩括号


    # 显示预览
    print("重命名预览：")
    for old, new in changes:
        print(f"{old} -> {new}")

    if not args.execute:
        print("\n【预览模式】未实际重命名。加上 --execute 执行。")
        return

    # 确认
    if not args.yes:
        confirm = input("\n确认执行以上重命名？(y/N): ").strip().lower()
        if confirm != 'y':
            print("已取消。")
            return

    # 执行
    for old, new in changes:
        try:
            os.rename(old, new)
            print(f"重命名成功: {os.path.basename(new)}")
        except Exception as e:
            print(f"重命名失败: {old} -> {new}, 错误: {e}")

    print("批量重命名完成。")


if __name__ == "__main__":
    """批量重命名脚本"""
    main()


# import os
#
# print(os.getcwd()) #获取当前工作目录
#
# items = os.listdir("./") # 列出目录下的所有文件和文件夹 包括当前 '.'就是当前及以下的意思
# print(items)
#
# # or.rename('旧名.txt','新名.txt') #重命名
# os.remove('无用文件.txt') #删除文件
#
# os.mkdir('新文件夹') #父目录必须存在 创建文件夹用的
# os.makedirs('a/b/c') #自动创建中间目录
#
# os.rmdir('空文件夹') #删除的是空目录
#
#
# #跨平台拼接
# path = os.path.join('folder','sub','file.txt') #'folder'（文件夹）、'sub'（子文件夹）、'file.txt'（文件名）
#
# dirpath = os.path.dirname('/a/b/c.txt') #去掉c.txt
# filename = os.path.basename('/a/b/c.txt') #去掉前面 保留c.txt
#
# root,ext = os.path.splitext('photo.jpg') # 把文件和后缀名分开 比如 photo.jpg 拆成 photo 和 .jpg
#             # 这个在批量修改文件后缀、处理图片 / 文档时超好用～
#
# if os.path.exists('data.txt'): #os.path.exists 检查路径文件夹是否存在，返回布尔值
#     print('存在')
# else:
#     print('不存在')
#
# os.path.isfile('file.txt') # os.path.isfile()判断是否是文件 返回布尔值
# os.path.isfile('folder')
#
# os.path.isdir(path) # os.path.isdir() 判断是否为文件夹
#
# import shutil
#
# shutil.copy('源文件.txt','目标文件.txt') #复制内容 + 权限
# shutil.copy2('源文件.txt','目标文件.txt') #完美复制 甚至连修改时间都复制
#
# shutil.copytree('源目录','目标目录') #复制整个目录
#
# shutil.move('old.txt','new.txt') #移动文件/目录 也可以重命名
# shutil.rmtree('目标路径') #删除非空目录 慎用
#
#
#
            # import os
            # path1 = r"D:\python\test"
            # items = os.listdir(path1)
            # print(items)
            # os.rename(os.path.join(path1,'a.txt'),os.path.join(path1,'001_a.txt'))
            # os.rename(os.path.join(path1,'b.jpg'),os.path.join(path1,'002_b.jpg'))
            # os.rename(os.path.join(path1,'c.pdf'),os.path.join(path1,'003_c.pdf'))
            # print(items)
import os
folder = "rest_files"
if not os.path.exists(folder):
    os.mkdir(folder)
    for name in ['a.txt', 'b.jpg', 'c.pdf']:
        with open(os.path.join(folder,name), 'w') as f:
            f.write("test") #往里面都写入test
items = os.listdir(folder)
files = [f for f in items if os.path.isfile(os.path.join(folder,f))] #先拼接再判断是不是文件
files.sort() #按照字母排序

for i,filename in enumerate(files,start=1):
    new_name = f"{i:03d}_{filename}" #03d 前面不足的补0 3位数字
    old_path = os.path.join(folder,filename) #filename 单独列出来的每一个
    new_path = os.path.join(folder,new_name)
    os.rename(old_path,new_path)
    print(f"{filename} -> {new_path}")
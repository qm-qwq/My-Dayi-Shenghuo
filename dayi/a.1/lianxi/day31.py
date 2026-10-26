# import os #管理电脑的 文件读写、批量处理文件 脑力活
# import time
# # os.path 就是 os 模块里专门处理路径的工具
#
# mtime = os.path.getmtime("day31.txt") # get = 获取  m = modify（修改） time = 时间
# readable = time.ctime(mtime) #转化为人能看懂的 和strftime的区别是这个简单
#
# import shutil #复制移动删除 体力活
# shutil.copy2("day31.txt",r"D:\python\test/day31().txt")

                                        # import os
                                        # import time
                                        # import schedule
                                        # m = os.path.getmtime("date")
                                        # r = time.ctime(m)
                                        # print(r)
                                        # def mm():
                                        #     print(r)
                                        # schedule.every(3).scheduler.do(mm)
import os
import time_
import shutil

y = "yuanwj_dir"
b = "kaobei_dir"

os.makedirs(y,exist_ok=True) # os.makedirs()创建多级文件夹 exist_ok = True 保证不报错 有的就跳过 没有就创建
os.makedirs(b,exist_ok=True)

def get_file_state(path):
    state = {}
    for root,dirs,files in os.walk(path):  # os.walk 把所以文件夹都找出来 只是进文件夹里面
        # for 每个文件夹:
        #     for 每个文件:
        #         处理这个文件
        # os.walk(...)每次循环只会固定返回 3 个东西：
        # 1：当前文件夹路径 比如 C:/桌面/我的照片/2025年
        # 2：里面的子文件夹列表 ["一月", "二月", "三月"]是在2025年里面的文件夹 一个一个的文件夹
        # 3：里面的文件列表 就是2025年的东西就在2025这个文件夹里面
        for file in files: #只有files 里面装着文件
             full_path = os.path.join(root,file) #os.path.join 拼接的意思
             state[full_path] = os.path.getmtime(full_path)    #获取最后被修改的时间并且存进state字典里面
    return state # 遍历完之后就存state字典里面
def backup_file(yuan,base): #源文件 备份文件
    rel = os.path.relpath(yuan,y) #相对路径 看源文件和y的相对路径 并且只取交集
    dest = os.path.join(base,rel) #连接拷贝的和相对的 不懂桌面有图片可以看
    os.makedirs(os.path.dirname(dest),exist_ok=True) # makedirs 是创建文件夹 dirname是创建和源文件一样的路径
    shutil.copy2(yuan,dest)
    print(f"备份: {yuan} -> {dest}")

#对比这次扫描和上次扫描
def compare_and_backup(oldwj,newwj,baocun):
    for filepath,mtime in newwj.items():
        if filepath not in oldwj:
            print(f"新增文件：{filepath}")
            backup_file(filepath,baocun) #调用备份保存
        else:
            if mtime != oldwj[filepath]:
                print(f"修改文件：{filepath}")
                backup_file(filepath,baocun)
    for filepath in oldwj:
        if filepath not in newwj:
            print(f"删除文件：{filepath}")

if __name__ == '__main__':
    print(f"开始监控 {y}，备份到 {b}")
    oldwj = get_file_state(y)
    try:
        while True:
            time.sleep(3)
            newwj = get_file_state(y)
            compare_and_backup(oldwj,newwj,b)
            oldwj = newwj
    except KeyboardInterrupt:
        print("\n监控停止")

# with open(r'D:\python\a.txt','a',encoding="utf-8") as f:
#     f.write("感觉 我的问题吗\n")
import csv

# import csv
# with open(r'D:\python\ceshide.csv','r',encoding="utf-8") as ff:
#     reader = csv.reader(ff)
#     # h = next(reader)  # 跳过第一行表头
#     for row in reader:
#         print(row)
# date = [
#     ['姓名', '语文', '数学', '英语'],
#     ['张三', 85, 92, 88],
#     ['李四', 78, 89, 94],
#     ['王五', 90, 87, 91]
# ]
# with open(r'D:\python\ceshide.csv','w',newline='', encoding="utf-8") as ff:
#     writer = csv.writer(ff)
#     writer.writerows(date)





# s = []

# with open(r"D:\python\ceshide.csv","r",encoding="utf-8") as f:
#     r = csv.reader(f)
#     header = next(r)
#     for row in r:
#         n = row[0]
#         ss = list(map(int,row[1:])) # row[1:] 就是从索引 1 开始，到末尾的所有元素
#         t = sum(ss)
#         avg = t / len(ss)
#         s.append([n] + ss + [t,round(avg,2)])
# new_header = header + ["总分", "平均分"]
# with open(r"D:\python\ceshide.csv", "w", newline="", encoding="utf-8") as ff:
#     writer = csv.writer(ff)
#     writer.writerow(new_header)
#     writer.writerows(s)
#     print()







# with open(r'D:\python\a.txt','r',encoding="utf-8") as i,open(r'D:\python\b.txt','a',encoding="utf-8") as g :
#     g.write(i.read())


# with open(r"D:\python\ceshide.csv",encoding="utf-8",newline="") as fi:
#     re = csv.reader(fi) # 普通读
#     for u in re:
#         print(u)
#
#     fi.seek(0)
#     e = csv.DictReader(fi)  # 转化成字典读
#     for ee in e:
#         print(ee)
# ro = [
# {'姓名': '张3', '语文': '85', '数学': '92', '英语': '88', '总分': '265', '平均分': '88.33'},
# {'姓名': '李4', '语文': '78', '数学': '89', '英语': '94', '总分': '261', '平均分': '87.0'},
# {'姓名': '王5', '语文': '90', '数学': '87', '英语': '91', '总分': '268', '平均分': '89.33'},
# ]
# fname = ['姓名', '语文', '数学', '英语','总分','平均分']
# with open(r"D:\python\ceshide.csv",'a',encoding="utf-8",newline="") as fi:
#     wr = csv.DictWriter(fi,fieldnames = fname)
#     wr.writerows(ro)

# import sys
# for p in sys.path:
#     print(p)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        a,b = map(float,sys.argv[1:3])
        print(f"相加结果：{add(a, b)}")
    else:
        print("用法：python day9.py <数字1> <数字2>")


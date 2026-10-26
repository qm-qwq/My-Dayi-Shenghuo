import requests #网络请求工具
import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

#采集数据
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url) #向网址发送一个请求返回结果
data = response.json() #吧结果
# 转换成Python能看懂的


df = pd.DataFrame(data) #转换成Excel表格
print("原始数据形状:", df.shape)
print(df.head())


df['userId'] = df['userId'].astype(int) #把爬下来的1 从字符串类型转为int


user_counts = df['userId'].value_counts().sort_index() #.value_counts()统计数字出现了多少次 .sortindex()排序
print("\n每个用户的发文数量：")
print(user_counts)

plt.figure(figsize = (10,6))
user_counts.plot(kind='bar',color = 'skyblue')
plt.title('每个用户的发文数量（JSONPlaceholder 模拟数据）')
plt.xlabel('用户ID')
plt.ylabel('文章数量')
plt.xticks(rotation = 0) #强制x轴文字不旋转
plt.grid(axis='y',linestyle='--',alpha=0.7) #grid网格线 axis='y'只画y轴的横线 线的样式是虚线 alpha透明度
plt.tight_layout() #tight紧凑 layout布局 自动调整布局
plt.savefig('user_posts.png')
plt.show()


with open('report.txt', 'w',encoding='utf-8') as f:
    f.write("模拟文章数据统计报告\n")
    f.write('='*30 + "\n")
    f.write(f"总文章数：{len(df)}\n")
    f.write(f"用户数：{df['userId'].nunique()}\n") #nunique 不重复
    f.write(f"平均每用户文章数：{df.groupby('userId').size().mean():.2f}\n") #size统计文章数量 .mean计算平均值 保留两位小数
    f.write("发文最多的用户：userId{}\n".format(user_counts.idxmax())) #idxmax 找到user_countss里面最大的那个值
                #"……".format(……)另一种格式化字符串的写法 把idmaxmax的结果填到{}里面
print("报告已保存到 report.txt")
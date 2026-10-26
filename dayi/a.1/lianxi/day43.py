# import pandas as pd #导入表格处理的工具
# import matplotlib.pyplot as plt #导入画图表的工具
#
# #设置中文显示
# plt.rcParams["font.sans-serif"] = ["SimHei","Microsoft YaHei"] # Windows
#             #plt 工具 rcParams 设置参数 font 字体 sans-serif 无衬线字体 SimHei 黑体 Microsoft YaHei 微软雅黑
# plt.rcParams['axes.unicode_minus'] = False
#             #axex 坐标轴 unicode_minus 负号  让图表里面的负号正常显示 不变乱码
# df = pd.read_csv("douban_cleaned.csv")
# print(df.head())
#
#
# plt.figure(figsize=(10,6)) # figure创建画布 figsize 画布大小
# plt.hist(df['评分'],bins=10,edgecolor = 'black',alpha = 0.7) #hist画直方图 bins分成10个柱子 edgecolor柱子边框 alpha透明度
# plt.title('电影评分分布直方图')
# plt.xlabel('评分')
# plt.ylabel('电影数量')
# plt.grid(axis = 'y',alpha = 0.3) #grid网格线 alpha 透明度（线的）
# plt.savefig('rating_histogram.png')
# plt.show()
#
#
# director_counts = df['导演'].value_counts().head(10) #valur_counts 统计每个值出现的次数 head 只取前10个
# plt.figure(figsize=(10,6))
# director_counts.plot(kind="bar",color='skyblue') # plot  开始绘图（工具 bar 柱形图
# plt.title('导演执导电影数量 Top 10')
# plt.xlabel('导演')
# plt.ylabel('电影数量')
# plt.xticks(rotation=45,ha = 'right') #x 轴刻度文字 rotation 文字旋转45度 ha=’right‘文字靠右对齐
# plt.tight_layout() #自动调整布局
# plt.savefig('director_bar.png')
# plt.show()
#
#
# bins = [0,8.0,8.5,9.0,10]
# labels = ['<8.0','8.0-8.5','8.5-9.0','>=9.0']
# df['评分等级'] = pd.cut(df['评分'],bins=bins,labels=labels,right=False) #新增一列叫评分等级 pd.cut分段工具 bins 分段 labels=labels按照上面名字贴标签  right左闭右开
#
# rating_level_counts = df['评分等级'].value_counts() #value_counts 统计每个等级有多少部电影
# plt.figure(figsize=(8,8))
# plt.pie(rating_level_counts,labels=rating_level_counts.index,autopct='%1.1f%%',startangle=90) # pie饼图 autopct="%1.1f%%"显示百分比 startangle从90度开始画
# plt.title('电影评分占比')
# plt.axis('equal') #让饼图正圆
# plt.savefig('rating_pie.png')
# plt.show()
#
#
# print("=== 电影数据统计报告 ===")
# print(f"总电影数量：{len(df)}")
# print(f"平均评分：{df['评分'].mean():.2f}") #:,2f保留两位小数
# print(f"最高评分：{df['评分'].max()}")
# print(f"最低评分：{df['评分'].min()}")
# print(f"评价人数总和：{df['评价人数'].sum():,}") # :,数字加千位分隔符
# print(f"导演数量：{df['导演'].nunique()}") #.nunique() 不重复的数量（多个只算一个）








import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv("douban_cleaned.csv")
print(df)


plt.figure(figsize=(7,7))
plt.hist(df['评分'],bins = 5,edgecolor='black',alpha = 0.8)
plt.title('电影评分分布直方图')
plt.xlabel('评分')
plt.ylabel('电影数量')
plt.grid(axis="y",alpha=0.5)
# plt.show()


dy_counts = df['导演'].value_counts().head(5)
plt.figure(figsize=(8,8))
dy_counts.plot(kind='bar',color='red')
plt.title('导演执行的电影数量前5排行')
plt.xlabel('导演')
plt.ylabel('电影数')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# plt.show()


bs = [0,8.5,9.0,9.5,10]
ls = ['<8.5','8.5-9.0','9.0-9.5','9.5-10']
df['评分等级'] = pd.cut(df['评分'],bins=bs,labels=ls)

rs = df['评分等级'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(rs,labels= rs.index,autopct='%1.1f%%',startangle=90)
plt.title('电影评分占比')
plt.axis('equal')
plt.show()
print("=== 电影数据统计报告 === (图表是按照前5画的)")
print(f"总电影数量: {len(df)}")
print(f"平均评分: {df['评分'].mean():.2f}")
print(f"最高评分: {df['评分'].max()}")
print(f"最低评分: {df['评分'].min()}")
print(f"评价人数总和: {df['评价人数'].sum():.}")
print(f"导演数量: {df['导演'].nunqiue()}")

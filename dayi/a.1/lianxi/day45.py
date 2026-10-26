import sqlite3
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# 直接读取清洗好的 CSV
df = pd.read_csv("douban_cleaned.csv")
conn = sqlite3.connect('douban.db')

df.to_sql('douban', con=conn, if_exists='replace', index=False) #存数据库中 表名 连接数据库 如果重复就覆盖 不保留行序号
conn.close()
print("数据已保存到 douban.db 的 douban 表中")

conn = sqlite3.connect('douban.db')
df_check = pd.read_sql_query("select * from douban", conn)
print(df_check)
conn.close()












import matplotlib.pyplot as plt #pyplot 画图的核心工具
df = read_csv("douban_cleaned.csv")
plt.hist(df["评分"],bins = 7,edgecolor = "black") #hist 直方图 bins 柱子 edgecolor 黑边
plt.title('豆瓣Top250评分分布')
plt.xlabel('评分')
plt.ylabel('电影数量')
plt.savefig('rating_hist.png')
plt.show()

director_counts = df['导演'].value_counts() #value_counts统计出现的次数 pandas专有的数数
director_counts.plot(kind='barh') #bar 柱子 barh 横向柱状图
plt.title('作品数量最多的导演')
plt.xlabel('电影数量')
plt.tight_layout()
plt.show()

def rating_level(score):
    if score >= 9.0: return 'S级 (≥9.0)'
    elif score >= 8.5: return 'A级 (8.5-8.9)'
    elif score >= 8.0: return 'B级 (8.0-8.4)'
    else: return 'C级 (<8.0)'
df["等级"] = df['评分'].apply(rating_level) #apply 应用 对每一行都做相当于pandas的专用遍历
level_counts = df['等级'].value_counts()
plt.pie(level_counts, labels=level_counts.index, autopct='%1.1f%%') #画饼图 用的数据 标签 自动百分比保留一位
plt.title('评分等级占比')
plt.show()

with open('douban_cleaned.csv', 'w', encoding='utf-8') as f:
    f.write(f"总电影数: {len(df)}\n")
    f.write(f"平均评分: {df['评分'].mean():.2f}\n")
    f.write(f"最高评分: {df['评分'].max()}\n")
    f.write(f"最低评分: {df['评分'].min()}\n")
    f.write(f"总评价人数: {df['评价人数'].sum():,}\n")
    f.write(f"最早年份: {int(df['年份'].min())}\n")
    f.write(f"最晚年份: {int(df['年份'].max())}\n")
import pandas as pd

df = pd.read_csv("douban_raw.csv")
print("原始数据")
print(df)
print("\n数据信息")
df.info() #查看csv的基础信息

#清洗数据
df['评价人数'] = df['评价人数'].str.replace(',',"").fillna('0').astype(int)
            # str.replace(',','')删掉数字里的逗号 => str.replace 替换的意思 把‘,’替换成‘’
            # fillna('0') 空数据填充0
            # astype(int) 把文字转化成整数 方便计算排序-->本来是字符串
df['评分'] = df['评分'].astype(float)        #astype 把数据类型转换成浮点数（小数）
df.dropna(subset=['导演'],inplace = True) # dropna 删除空数据 subset 只检查[]里面的 inplace=True 直接修改原表格

print("清洗后的数据：")
print(df)

df.to_csv("douban_cleaned.csv", index=False, encoding="utf-8-sig")
            #index=False 否定把自动生成的索引行序号存入文件
print("已保存到 douban_cleaned.csv")

import sqlite3 #轻量数据库

conn = sqlite3.connect("movies.db") #connect 连接 。db是数据库后缀
df.to_sql("movies",conn,if_exists="replace",index=False)
            # to_sql 存入数据库
            # if_exists 如果数据表存在 replace 直接覆盖掉
print("已保存到 movies.db 数据库中的 movies 表")

query = "select * from movies;" #select查询 *所有列数据
result = pd.read_sql_query(query,conn) # read_sql_query(要执行的查询命令，用哪个数据库连接) 执行查询语句获得数据
print("数据库中读取的数据：")
print(result)

conn.close() #关闭数据库
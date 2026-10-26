# import pandas as pd
# df = pd.read_csv(r'D:/python/ceshide.csv')
# print(df)
# df = pd.read_csv(r'D:/python/ceshide.csv',header=None,names=['x','y','z','w','e','r'])
# print(df)
# df1 = pd.read_csv(r'D:/python/ceshide.csv',encoding='utf-8')
# print(df1)


# import pandas as pd
#
# # 1. 先创建数据
# df = pd.DataFrame({
#     '姓名': ['张三', '李四', '王五'],
#     '语文': [85, 78, 90],
#     '数学': [92, 89, 87]
# })
#
# # 2. 保存成Excel文件（自动生成data.xlsx）
# df.to_excel('data.xlsx', index=False, sheet_name='Sheet1')
#
# # 3. 读取自己生成的Excel文件
# df_read = pd.read_excel('data.xlsx', sheet_name='Sheet1')
# print("读取自己生成的Excel文件：")
# print(df_read)
#
# print(df_read.head()) #前n行 默认5行
# print(df_read.info()) #详细信息
# print(df_read.describe()) #数值列统计 （均值 标准差 四分位数等）
# print(df_read['姓名'].value_counts()) #分类各值的频次
# df.to_csv('output.csv', index=False, encoding='utf-8')
# #df.to_csv保存为csv  index=False不把行索引保存 'output.csv'保存的文件名
# df_r = pd.read_csv('output.csv')
# print(df_r)



#
# import pandas as pd
# df = pd.read_csv(r'D:/python/ceshide.csv')
# print(df)
# print(df.head(3))
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# df['语文数学分和'] = df['语文'] + df['数学']
# df.to_csv('cheng_ji.csv', index=False)

# 布尔索引
# import pandas as pd
# df = pd.DataFrame({
#     '姓名': ['张三', '李四', '王五', '赵六'],
#     '年龄': [25, 30, 28, 22],
#     '城市': ['北京', '上海', '北京', '上海']
# })
# print(df)
# print(df[df['年龄'] > 25])  #年龄大于25的行
# print([df['城市'] == '北京']) #城市为北京的行
# # 外面套一层df就 直接打印值 不是只判断了
#
# #多条件表示
# print(df[(df['年龄'] > 25) & (df['城市'] == '北京')])
# print(df[(df['年龄'] > 30) | (df['城市'] == '上海')])
# # &表示且 |表示或

# df[df['年龄'].between(23,28)] #between 筛选区间
#
# avg_age = df['年龄'].mean() #平均值
# df[df['年龄'] > avg_age] #年龄大于平均值
#
# print(df.loc[df['年龄'] > 25,['姓名', '年龄']]) #按照标签筛选
# # df.loc[ 行筛选条件 , 列筛选条件 ] 先行再列
#
# df_sorted = df.sort_values('年龄') #升序排列
# print(df_sorted)
# df_sorted = df.sort_values('年龄',ascending=False) #降序排列
# print(df_sorted)
# df_sorted = df.sort_values(['城市', '年龄'], ascending=[True, False]) #城市正序 年龄降序 城市按首字母排序

# group = df.groupby('城市')['年龄'].mean() #按照城市分组，计算各城市平均年龄
# print(group)

# result = df.groupby('城市').agg({   # agg 对城市这一  “”“列”“”   一次性算出 总和、平均值、最大值
#     '年龄':["mean",'max','min'],    # 对年龄求这些
#     '姓名':'count'                  # 对姓名数数
# })
# print(result)
#
# for city,group in df.groupby('城市'): #分组遍历
#     print(f"{city}: {len(group)}人")






import pandas as pd
df = pd.DataFrame({
    '产品':['A','B','C','D'],
    '销量':[120, 80, 150, 90],
    '价格':[10,20,15,25]
})
print(df)
a = df['销量'].mean()
print(df[df['销量'] > a])
df_sort = df.sort_values("价格", ascending=False)
print(df_sort)
re = df.groupby('产品').agg({
    '价格':'mean'
})
re1 = df.groupby ('产品')['价格'].mean()
print(re1)
print(re)








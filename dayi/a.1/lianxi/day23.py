# import numpy as np

# # np.where(条件, 满足条件时的值, 不满足条件时的值)
# arr = np.array([1,2,3,4,5])
# result = np.where(arr > 3,99,0) #把大于3的元素替换成99，其余替换成0
# print(result)
#
# arr2 = np.random.randn(3,4)
# filtered = np.where(arr2 < 0,0,arr2) #把负的替换成0 正数不变
# print(filtered)


# np.random.seed(44) #固定随机种子
# a = np.random.rand(2,3)
# b = np.random.randn(100)
# c = np.random.randint(1,10,size=(3,3)) #下限是1，上限是9 不包含10，三行三列的随机数





# import numpy as np
# a11 = np.random.randint(1, 100, size=(4, 5))
# print(a11)
# print(np.mean(a11,axis=1))
# print(np.where(a11 >50,1,0))







# import pandas as pd
# s1 = pd.Series([1,3,5,7])
# print(s1)
#
# s2 = pd.Series([1,3,5,7],index=['a','b','c','d'])
# print(s2)
#
# s3 = pd.Series({'apple':3,'banana':5,'pear':7})
# print(s3)
#
# print(s2['b'])
# print(s2.iloc[0])
# print(s2 > 3)
# print(s2.mean())
# print(s2[s2>3])
#
#
#
# data = {
#     '姓名': ['张三', '李四', '王五'],
#     '年龄': [25, 30, 28],
#     '城市': ['北京', '上海', '广州']
# }
# df = pd.DataFrame(data)
# print(df)

# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# df2 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
# print(df2)
#
# data = [['张三', 25], ['李四', 30], ['王五', 28]]
# df3 = pd.DataFrame(data, columns=['姓名', '年龄'])
# print(df3)
#
# df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})
# print(df.shape) #形状字典的键 'A'、'B' → 会变成列名（表头），所以是 2 列
# # 每个键对应的列表 [1,2,3]、[4,5,6] → 每列有 3 个元素，对应3 行
# print(df.columns)
# print(df.head(2))
# print(df.describe())

# df['姓名']
# df.姓名
# df[['姓名','年龄']]
# df.loc[0]
# df.loc[0:2] #loc根据标签索引
# df.iloc[0]
# df.iloc[0:2] #iloc根据位置索引
#
# df.loc[0:1,['姓名','城市']] # 取前两行的姓名和城市
# df.iloc[0,1] # 取第1行第2列（整数位置）

import pandas as pd
data = {
    '产品': ['张三', '李四', '王五'],
    '价格': [25, 30, 28],
    '库存': [1,4,6]
}
df = pd.DataFrame(data)
print(df)
print(df.info())
print(df[['价格','库存']].mean())






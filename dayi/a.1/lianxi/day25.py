# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({
#     'A': [1, 2, np.nan, 4],
#     'B': [5, None, 7, 8],
#     'C': ['x', 'y', np.nan, 'z']
# })
# print(df)

# print(df.isna())
# print(df.notna())

# print(df.isna().sum())
# print(df.isna().any(axis=1)) # any  只要有一个满足就返回ture

# df_clean = df.dropna()  # dropna() 删除缺失值 默认 axis=0 就是列 x=0
# print(df_clean)
# df_clean2 = df.dropna(axis=1)
# print(df_clean2)
# df.dropna(how='all') # 删除所有值都为缺失的行（how='all'）
# a = df.dropna(thresh=2)  # thresh=n 至少n个“”不是缺失“”的值保留少于n个直接删掉 简单来说thresh是非空 然后前面是删除
#                          # 不一样的就是至少没有<>好
# b = df.dropna(subset=['B', 'C']) #subset其实就是 “限定范围” 的意思  英文：subset = 子集
# print(a)
# print(b)

# df_filled = df.fillna(0)  #fillna填充缺失值 所有缺失值填为0
# print(df_filled)
# c = df.ffill()  #method方法 用上面一行填充下面一行缺失的
# d = df.bfill()  #用下一行填充
# print(c)
# print(d)

# mean_val = df['A'].mean()
# d = df['A'].fillna(mean_val)
# print(d)
#
# a = df.fillna({'A':0,'B':99,'C':"缺失"})
# print(a)

# c = df.ffill(limit=1) # 最多填充1次连续的none
# print(c)

import pandas as pd
import numpy as np


data = {'分数': [85, 92, np.nan, 78, np.nan, 88], '年级': [1,1,2,2,3,3]}
df = pd.DataFrame(data)
print(df)

zws = df['分数'].median()
f = df['分数'].fillna(zws)
e = df.fillna(zws)
d = df.dropna(subset=['年级'])
print(e)
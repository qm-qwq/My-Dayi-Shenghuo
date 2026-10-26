

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 生成最近7天数据
dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
categories = ['电子产品', '服装', '家居用品']

data = []
for d in dates:
    for cat in categories:
        data.append({
            '日期': d,
            '产品类别': cat,
            '销售额': np.random.randint(2000, 10000),
            '订单数': np.random.randint(10, 100)
        })

df = pd.DataFrame(data)
df.to_excel('daily_sales.xlsx', index=False)
print("模拟数据已生成：daily_sales.xlsx")



df = pd.read_excel('daily_sales.xlsx')
zxxe = df['销售额'].sum()

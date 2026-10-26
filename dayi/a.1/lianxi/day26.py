# import matplotlib.pyplot as plt #导入画图工具

# 简单折线图
# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
#
# plt.plot(x,y,'ro-') #绘制折线图  # r:红色, o:圆点标记, -:实线
# plt.xlabel('x轴')
# plt.ylabel('y轴') #给标签命名
# plt.title('平方函数')
# plt.grid(True) #显示网格
# plt.show() #显示图形
#
#
# # 柱状图
# heng = ['A', 'B', 'C', 'D']
# h =  [15, 30, 45, 20]
#
# plt.bar(heng, h,color='skyblue')
# plt.xlabel('类别')
# plt.ylabel('数值')
# plt.title('柱状图示例')
# plt.grid(True)
# plt.show()
#
# # 多图叠加
# plt.plot(x,y1,label='y1')
# plt.plot(x,y2,label='y2')
# plt.legend() #显示图例便于区分y1 y2
#
# plt.xlim(0,10)
# plt.ylim(0,30) #限定范围
#
# plt.savefig('plot.png',dpi=150)  # dpi是清晰度 默认很低
# # 同时绘制
# fig,(ax1,ax2) = plt.subplots(1,2) #一行两列也就是并排
# # fig 整个画布对象 ax1 2 是画笔
# ax1.plot(x,y)
# ax2.bar(heng,h)
# plt.show()

# import pandas as pd
# from matplotlib import pyplot as plt
#
# df = pd.DataFrame({'x': [1,2,3,4], 'y': [10,20,15,30]})
# df.plot(x='x', y='y', kind='bar')  #bar 是柱形图 line 是折线图
# df.plot(x='x', y='y', kind='line')  #bar 是柱形图 line 是折线图
# plt.show()

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'x': [1,2,3,4,5], 'y': [1,4,9,16,25]})
df.plot(x='x', y='y', kind='line')
plt.show()



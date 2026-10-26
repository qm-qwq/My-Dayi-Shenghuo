import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel
from openpyxl.styles.builtins import title

# 配置中文显示（不用记忆）
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# df = pd.DataFrame({
# '月份': ['1月', '2月', '3月', '4月'],
#     '销售额': [120, 135, 98, 145],
#     '成本': [80, 90, 70, 95]
# })
# df.plot(x = '月份',y = '销售额', kind = 'line') # kind 图形种类
# plt.show()
# df.plot(x = '月份',y = '销售额', kind = 'bar') # kind 图形种类
# plt.show()
#
# ax = df.plot(
#     x = '月份',
#     y = ['销售额','成本'],
#     kind = 'bar',
#     figsize = (10,5), #图形大小 （宽，高）
#     title = '销售与成本对比',
#     color = ['blue','orange'],
#     grid = True, #显示网格
#     legend = True, #显示图例
#     xlabel = '月份',
#     ylabel = '金额（万元）',
# )
#
#
# df.plot(kind = 'bar')
# plt.savefig('sales.png',dpi=300,bbox_inches='tight')  # bbox_inches='tight'更好看
# plt.show()







df = pd.DataFrame({
'月份': ['1月', '2月', '3月', '4月','5月','6月'],
    '销售额': [120, 135, 98, 145,44,245],
})
ax = df.plot(
    x = '月份',
    y = '销售额',
    kind = 'bar',
    title = "标题",
    grid = True,
    legend = True,
    xlabel = '月份',
    ylabel='金额（万元）'
)
plt.savefig('monthly_sales.png', dpi=300, bbox_inches='tight')
plt.show()
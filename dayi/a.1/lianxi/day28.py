import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from matplotlib import pyplot as plt

np.random.seed(42)
dates = [datetime(2025, 1, 1) + timedelta(days=i) for i in range(180)]  # 半年数据
categories = ['电子产品', '服装', '家居用品', '食品']
regions = ['华东', '华南', '华北', '西南']

data = {
    '日期': np.random.choice(dates, 500),
    '产品类别': np.random.choice(categories, 500),
    '区域': np.random.choice(regions, 500),
    '销售额': np.random.randint(100, 5000, 500),
    '销量': np.random.randint(1, 100, 500)
}
df = pd.DataFrame(data)
df['日期'] = pd.to_datetime(df['日期'])
df.to_csv('sales_data.csv', index=False, encoding='utf-8-sig')
print("模拟数据已生成：sales_data.csv")

                    # nn = pd.read_csv('sales_data.csv',encoding='utf-8-sig')
                    # print(nn)
                    # df['总销售额'] = df['销售额'].sum()
                    # df['总销量'] = df['销量'].sum()
                    # print(df)
                    # ax = df.plot(
                    #     x='日期',
                    #     y='销售额',
                    #     kind='bar',
                    #     title='2025年上半年月度销售额',
                    #     xlabel='月份',
                    #     ylabel='销售额（万元）',
                    #     color='skyblue'
                    # )
                    # plt.show()
                    # lb = df.groupby('产品类别').agg({
                    #     "家居用品":sum,
                    #     "食品":sum,
                    #     "电子产品":sum,
                    # })
                    # print(lb)

plt.rcParams['font.sans-serif'] = ['SimHei','Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('sales_data.csv',parse_dates=['日期']) #直接识别成「日期格式」
print('数据预览：')
print(df.head())
print('\n数据信息：')
df.info() #体检

if df.isna().sum().sum() > 0:
    print("\n存在缺失值，执行删除")
    df.dropna(inplace=True)
        # 1. df.isna() 检查每个单元格是不是空值（np.nan）是空 → True不是空 → False
        #
        # 2. df.isna().sum() 统计每一列有多少个空值
        #
        # 3. df.isna().sum().sum() 把所有空值加起来，算总共有多少个空值
        #
        # 4. if ... > 0: 如果总数 > 0 → 说明真的有缺失值
        #
        # 5. df.dropna(inplace=True) 直接删除所有包含空值的整行！

total_sales = df['销售额'].sum()
total_quantity = df['销量'].sum()
print(f"\n总销售额：{total_sales:,.0f} 元")
        # ,：给数字加上千位分隔符，比如 123456 会变成 123,456，读起来更方便
        # .0f：把数字按浮点数处理，保留0 位小数（也就是自动四舍五入成整数）
print(f"总销量：{total_quantity} 件")

df['月份'] = df['日期'].dt.to_period('M').astype(str)
        # .dt
        # 专门用来提取日期里的年 / 月 / 日
        #  .to_period('M')
        # 把日期变成「年月格式」
        # 2025-01-15 → 2025-01
        # 2025-02-20 → 2025-02
        #  .astype(str)
        # 转成普通文本格式，方便画图、分组
monthly_sales = df.groupby('月份')['销售额'].sum().reset_index()
        # reset_index() 把表格变回正常格式（必须加，不然画图会报错）
print("\n月度销售额：")
print(monthly_sales)

plt.figure(figsize=(10,6))
plt.bar(monthly_sales['月份'], monthly_sales['销售额'], color='skyblue')
        # plt.bar( x, y )
plt.title('月度销售额趋势')
plt.xlabel('月份')
plt.ylabel('销售额（元）')
plt.xticks(rotation=45) #把x上面的字旋转45度
for i,v in enumerate(monthly_sales['销售额']):
    plt.text(i,v + 500,f'{v:,.0f}',ha='center')
        # v + 500  v = 柱子高度   +500 = 往上挪一点点，不挡住柱子 （数字高一点，好看）
        # ha = 'center' 文字水平居中，正好对准柱子
        # plt.text( ) 在图上写字
plt.tight_layout()  #= 让 matplotlib 自动调整布局，把所有元素都舒舒服服放好，不打架
plt.savefig('monthly_sales.png')
plt.show()

category_sales = df.groupby('产品类别')['销售额'].sum().sort_values(ascending=False)
            # ascending=False = 降序
print("\n各类别销售额：")
print(category_sales)

#画饼图
plt.figure(figsize=(8,8))
plt.pie(category_sales,labels=category_sales.index,autopct='%1.1f%%',startangle=90)
            # category_sales 饼图的数值= 每一类卖了多少钱
            # labels=category_sales.index 饼图外面的文字标签= 电子产品、服装、食品…
            # autopct='%1.1f%%' 显示百分比 保留 1 位小数
            # startangle=90 饼图从正上方开始画 更好看、更标准
plt.title('各产品类别销售额占比')
plt.axis('equal')  #到底干嘛？ 一句话：让 X 轴和 Y 轴的比例相等 → 保证饼图是【正圆形】，不是椭圆！
plt.savefig('category_pie.png')
plt.show()

max_month = monthly_sales.loc[monthly_sales['销售额'].idxmax(),'月份']
            # monthly_sales['销售额'].idxmax()：找到「销售额」列中最大值对应的行索引
            # .loc[行索引, '月份']：根据这个索引，取出对应的「月份」值
best_category = category_sales.idxmax()
print("\n--- 分析结论 ---")
print(f"1. 总销售额为 {total_sales:,.0f} 元，总销量为 {total_quantity} 件。")
print(f"2. 销售额最高的月份是 {max_month}，当月销售额为 {monthly_sales['销售额'].max():,.0f} 元。")
print(f"3. 销售额最高的产品类别是 {best_category}，贡献了 {category_sales.max()/total_sales:.1%} 的销售额。")


# from openpyxl import Workbook
#
# wb = Workbook() #创建     创一个全新的空白 Excel 文件  \\ Workbook() = 新建 Excel 工作簿
# ws = wb.active #激活
# ws.title = "销售数据"
# ws['A1'] = "产品"
# ws['B1'] = "销售额"
# ws['A2'] = "笔记本"
# ws['B2'] = 12000
# ws['A3'] = "手机"
# ws['B3'] = 8500
# wb.save('sales.xlsx')
#
# ws.append(["平板", 6200])
# wb.save('sales.xlsx')
#
# from openpyxl import load_workbook
#
# wb = load_workbook('sales.xlsx')
# ws = wb.active
#
# print(ws['A1'].value)
#
# row = ws[2]
# for cell in row:
#     print(cell.value) #打印2列的值
#
# for row in ws.iter_rows(min_row=2,values_only=True):
#     print(row)
#                             # values_only=True 这个参数是 “只取单元格的值”
#                             # ws.iter_rows()是专门遍历这种文件的方法
#                             # min_row=2 从第二行开始




# from openpyxl import Workbook
#
# wb = Workbook()
# ws = wb.active
#
# ws.title = "成绩表"
# ws['A1'] = '姓名'
# ws['B1'] = '语文'
# ws['C1'] = '数学'
# ws['D1'] = '英语'
#
# # 写入学生数据
# ws['A2'] = "yiyi"
# ws['B2'] = 11
# ws['C2'] = 22
# ws['D2'] = 33
#
# ws['A3'] = "erer"
# ws['B3'] = 22
# ws['C3'] = 33
# ws['D3'] = 33
#
# ws['A4'] = "sansan"
# ws['B4'] = 33
# ws['C4'] = 33
# ws['D4'] = 33
# wb.save('学生成绩.xlsx')
# from openpyxl import load_workbook
# wb = load_workbook('学生成绩.xlsx')
# ws = wb.active
# for row in ws.iter_rows(values_only=True):
#     print(row)
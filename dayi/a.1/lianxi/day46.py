#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import time
import os
from bs4 import BeautifulSoup
import random
time.sleep(random.uniform(1, 3))


#====================配置=====================
BASE_URL = "https://movie.douban.com/top250"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
}
                # User-Agent 伪装成浏览器
                # Accept 告诉服务器接收的格式内容
                # Accept-Language 告诉服务器优先看中文
                # Connection 保持连接
OUTPUT_DIR = "output" #保存的文件夹
os.makedirs(OUTPUT_DIR, exist_ok=True) #创建这个文件夹 存在不报错

#====================爬虫==================
def fetch_movies():
    """爬取豆瓣TOP250所有的电影，返回列表"""
    all_movies = []
    for start in range(0, 250, 25): #range生成10个数 循环10次，第一次0开始第二次25开始
        url = f"{BASE_URL}?start={start}"#?start={start}分页参数 {start}就是上面循环的0，25……
        print(f"正在抓取: {url}")
        try:
            r = requests.get(url, headers=HEADERS,timeout=10) #headers伪装身份
            r.raise_for_status()  # 检查HTTP请求是否成功

            # 可选：检查返回内容长度，如果过短则可能被拦截
            if len(r.text) < 10000:
                print(f"警告：第{start // 25 + 1}页返回内容过短，可能被拦截")
                continue

            if r.status_code != 200:
                print(f"请求失败。状态码：{r.status_code}")
                continue
            soup = BeautifulSoup(r.content, "html.parser") #吧网页代码变成好看的汤 =>整理成清晰结构
            items = soup.find_all("div", class_="item") #找所有符合条件的（要找的，找class叫item的）
            if not items:
                print("未找到电影条目，请检查请求头或网络。")
                break

            for item in items:
                rank_em = item.find("em")# 找排名
                rank = rank_em.text if rank_em else "0"
                title_span = item.find("span", class_="title")#找中文名
                title = title_span.text if title_span else "未知"
                rating_span = item.find("span", class_="rating_num") #评分
                rating = rating_span.text if rating_span else "0"
                star_div = item.find("div", class_="star") # 评价人数（带“人评价”的span
                if star_div:
                    spans = star_div.find_all("span")
                    if len(spans) >= 2:
                        people_text = spans[-1].text
                        people = people_text.replace( "人评价","").strip()
                    else:
                        people = 0
                else:
                    people = 0
                #   = 导演和年份 =
                bd = item.find("div", class_="bd")
                if bd:
                    p = bd.find("p") #在bd区域找到<p>标签 拿出来 就是到语言那块
                    if p:
                        info_text = p.text.strip() #拿到
                        if "导演" in info_text:
                            director = info_text.split("导演：")[1].split("\n")[0].strip()#
                                    #split()把里面的切开 【1】取第二段 再把后面多余的主演啥的全切了 去空格
                        else:
                            director = "未知"
                        lines = info_text.split("\n") #按照换行切割 保存为列表
                        year_line = lines[1] if len(lines) > 1 else "" #判断文本是否有第二个 第二个是年份 拿取 #找网页里面的年份 拿第二行
                        year = "" #定义空变量存年份
                        for part in year_line.split("/"):
                            if part.strip().isdigit(): #strip 去空格 isdigit判断是不是数字
                                year = part.strip() #对空变量赋值 循坏外
                                break
                    else:
                        director = "未知"
                        year = ""
                else:
                    director = "未知"
                    year = ""
                all_movies.append({
                    "排名": rank,
                    "电影名称": title,
                    "评分": rating,
                    "评价人数": people,
                    "导演": director,
                    "年份": year
                })
            time.sleep(1) # 礼貌爬取
        except Exception as e:
            print(f"爬取出错（start = {start}）：{e}")
            continue
    return all_movies

#============================数据清洗==============================
def clean_data(df):
    df["评价人数"] = df["评价人数"].str.replace(',','').fillna('0').astype(int) #str.replace字符串重写 把‘,’改成''
                #fillna 填充0 astype把文字转换成整数
    df["评分"] = pd.to_numeric(df["评分"],errors='coerce').fillna(0).astype(float) #to_numeric转换成数字 errors='coerce'遇到异常转成空值
    df['年份'] = pd.to_numeric(df['年份'], errors='coerce').fillna(0).astype(int)
    ## df.dropna(subset = ['导演'], inplace=True) #删除导演为空的
    ## df.reset_index(inplace=True, drop=True) #重新排序 把删掉的那些整理
    return df
# pd.to_numeric 是 pandas专门转数字的 评价人数是因为带逗号要先清理

#====================存储========================
def save_to_csv(df,path):
    df.to_csv(path, index=False, encoding='utf-8')
    print(f"csv 已保存{path}")

def save_to_sqlite(df,db_path,table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"sqlite 已保存{db_path}(表：{table_name})")

#=================可视化报告===================
def plot_rating_distribution(df,save_path):
    plt.figure(figsize=(8,5))
    plt.hist(df["评分"],bins = 20,edgecolor = 'black',alpha = 0.7,color = 'skyblue') #hist画直方图 edgecolor边框颜色
    plt.title('豆瓣Top250电影评分分布')
    plt.xlabel('评分')
    plt.ylabel('电影数量')
    plt.grid(axis='y', linestyle='--', alpha=0.7) #plt.grid网格线 axis='y'只显示y轴的横线
    plt.savefig(save_path)
    plt.close()
    print(f"评分分布图: {save_path}")

def plot_top_directors(df,save_path,n = 10):
    director_counts = df['导演'].value_counts().head(n)
    plt.figure(figsize=(8,5))
    director_counts.plot(kind='barh',color = 'orange')
    plt.title(f'作品数量最多的前{n}位导演')
    plt.xlabel('电影数量')
    plt.ylabel('导演')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"导演频次图: {save_path}")

def plot_rating_pie(df, save_path):
    def rating_level(score):
        if score >= 9.0:
            return 'S级 (≥9.0)'
        elif score >= 8.5:
            return 'A级 (8.5-8.9)'
        elif score >= 8.0:
            return 'B级 (8.0-8.4)'
        else:
            return 'C级 (<8.0)'
    df_copy = df.copy() #拷贝一份不影响原表
    df_copy['等级'] = df_copy['评分'].apply(rating_level) #拷贝的等级通过评分 apply专门遍历通过（）里面的方式
    level_counts = df_copy['等级'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(level_counts, labels=level_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('电影评分等级占比')
    plt.axis('equal')
    plt.savefig(save_path)
    plt.close()
    print(f"评分等级饼图: {save_path}")

def generate_report(df,report_path):
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("豆瓣Top250电影分析报告\n")
        f.write("=" * 50 + "\n")
        f.write(f"总电影数: {len(df)}\n")
        f.write(f"平均评分: {df['评分'].mean():.2f}\n")
        f.write(f"最高评分: {df['评分'].max()}\n")
        f.write(f"最低评分: {df['评分'].min()}\n")
        f.write(f"总评价人数: {df['评价人数'].sum():,}\n")
        f.write(f"最早电影年份: {int(df['年份'].min()) if df['年份'].min() > 0 else '未知'}\n")
        f.write(f"最近电影年份: {int(df['年份'].max())}\n")
        f.write("\n评分前5名:\n")
        top5 = df.nlargest(5, '评分')[['排名', '电影名称', '评分', '评价人数']]  # nlargest 取最大最多的n条数据 按评分从高到底排序只要后面四列
        for _, row in top5.iterrows():  # iterrows 一行行遍历（但是第一个是索引所以要用一个占位符代替）
            f.write(f"{row['排名']}. {row['电影名称']} ({row['评分']}) - {row['评价人数']}人评价\n")
        f.write("\n评分后5名:\n")
        bottom5 = df.nsmallest(5, '评分')[['排名', '电影名称', '评分', '评价人数']]  # 从低到高排序 取分数最低的
        for _, row in bottom5.iterrows():
            f.write(f"  {row['排名']}. {row['电影名称']} ({row['评分']}) - {row['评价人数']}人评价\n")
    print(f"分析报告: {report_path}")

#================================主流程============================
def main():
    print("=== 豆瓣电影Top250数据采集与分析工具 ===\n")
    raw_csv = os.path.join(OUTPUT_DIR,"douban_raw.csv")
    if os.path.exists(raw_csv):
        print("发现已保存的原始数据，直接读取...")
        df = pd.read_csv(raw_csv)
    else:
        print("开始爬取豆瓣Top250...")
        movies = fetch_movies()
        if not movies:
            print("爬取失败，请检查网络。")
            return
        df = pd.DataFrame(movies)
        df.to_csv(raw_csv, index=False, encoding="utf-8-sig")
        print(f"原始数据已保存: {raw_csv}")

    print("\n正在清洗数据...")
    df_clean = clean_data(df)

    cleaned_csv = os.path.join(OUTPUT_DIR, "douban_cleaned.csv") #os.path.join拼接路径
    save_to_csv(df_clean, cleaned_csv)
    db_path = os.path.join(OUTPUT_DIR, "douban.db")
    save_to_sqlite(df_clean, db_path, "top250")

    plot_rating_distribution(df_clean, os.path.join(OUTPUT_DIR, "rating_hist.png"))
    plot_top_directors(df_clean, os.path.join(OUTPUT_DIR, "director_top10.png"), n=10)
    plot_rating_pie(df_clean, os.path.join(OUTPUT_DIR, "rating_pie.png"))

    generate_report(df_clean, os.path.join(OUTPUT_DIR, "report.txt"))

    print("\n🎉 项目完成！所有结果保存在 output 文件夹。")


if __name__ == "__main__":
    main()

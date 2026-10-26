import requests #专门做网络请求的

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/91.0.4472.124 Safari/537.36"
} # 伪装成谷歌浏览器
r = requests.get(url, headers=headers) #aders=headers 带上自己假的身份证
print(r.status_code) # 发送网络请求
print(r.text[:500])

from bs4 import BeautifulSoup #解析网页加工美化

soup = BeautifulSoup(r.text,'html.parser') #"html.parser"整理乱的 女仆

items = soup.find_all("div",class_="item") #只找div 找item标签
# 更准确：找 <div class="item">
# 豆瓣每个电影信息在 <div class="item"> 内
t = []
for item in items:
    title = item.find("span", class_="title").text
    rating = item.find("span", class_="rating_num").text
    star_div = item.find("div",class_="star")
    if star_div:
        people_span = star_div.find_all("span")[-1]
        people = people_span.replace('人评价', "").strip()
    else:
        people = "未知"
    t.append((title,rating,people))

for idx,(title,rating,people) in enumerate(t,1):
    print(f"{idx}. {title} | {rating} | {people}人评价")


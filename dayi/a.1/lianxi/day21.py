
import requests
import json
from datetime import datetime
def tq(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            print(f"请求失败，状态码：{resp.status_code}")
            return None
        data = resp.json()
        current = data.get("current_condition", [{}])[0]
        nearest = data.get("nearest_area", [{}])[0]
        city_name = nearest.get("areaName", [{}])[0].get("value", "未知")
        temp = current.get("temp_C", "N/A")
        weather = current.get("weatherDesc", [{}])[0].get("value", "N/A")
        humidity = current.get("humidity", "N/A")
        wind = current.get("windspeedKmph", "N/A")
        return {
            "city": city_name,
            "temp": temp,
            "weather": weather,
            "humidity": humidity,
            "wind": wind,
            "raw": data,
        }
    except requests.exceptions.RequestException as e:
        print(f"网络错误：{e}")
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"数据解析错误：{e}")

def display_weather(info):
    """打印天气信息"""
    print(f"城市：{info['city']}")
    print(f"温度：{info['temp']}°C")
    print(f"天气：{info['weather']}")
    print(f"湿度：{info['humidity']}%")
    print(f"风速：{info['wind']} km/h")
def save(city,info):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"[{timestamp}|{city}->{info['temp']}°C, {info['weather']}\n]"
    with open(f"weather_history.txt", "a", encoding="utf-8") as f:
        f.write(record)
def show_history():
    try:
        with open("weather_history.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("暂无历史记录")
        else:
            print("历史")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("无记录")
def main():
    print("欢迎使用命令行天气查询工具")
    print("输入城市名称（拼音或中文）查询天气")
    print("输入 history 查看历史记录，输入 q 退出")
    while True:
        city = input("请输入城市名称：（支持拼音）").strip()
        if city.lower() == "q":
            print("再见！")
            break
        elif city.lower() == "history":
            show_history()
            continue
        elif city == "":
            print("城市名不能为空")
            continue
        print(f"正在查询 {city} 的天气...")
        info = tq(city)
        if info:
            display_weather(info)
            save(city, info)
if __name__ == "__main__":
    main()
















# import numpy as np
# a = np.array([1,2,3])
# b = np.array([1,2],[3,4])
#
# c = np.arange(5)
# d = np.arange(1,10,4)
#
# e = np.linspace(0,1,5)
#
# zeros = np.zeros((2,3))
# ones = np.ones((3,2))
#
# rarr = np.random.rand(2,3)
# raint = np.random.randint(1,5,size=(2,3))



















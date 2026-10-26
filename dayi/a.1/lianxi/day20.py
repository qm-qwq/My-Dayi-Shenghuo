# import requests
# city = "guangdong"
# url = f"https://wttr.in/{city}?format=j1"
# response = requests.get(url)
# data = response.json()
#
#
# import json
# with open("weather.json","w",encoding="utf-8") as f:
#     json.dump(data,f,ensure_ascii=False,indent=2)




city = input("请输入城市名称：（支持拼音）")
import requests #re这个是给网路发请求的
import json #这个是处理json格式的
url = f"https://wttr.in/{city}?format=j1"
try:
    resp = requests.get(url,timeout=10)
    if resp.status_code != 200:
        print(f"请求失败，状态码：{resp.status_code}")
    else:
        data = resp.json()
        current = data.get("current_condition",[{}])[0]
        nearest = data.get("nearest_area",[{}])[0]
        city_name = nearest.get("areaName",[{}])[0].get("value","未知")
        temp = current.get("temp_C", "N/A")
        weather_desc = current.get("weatherDesc", [{}])[0].get("value", "N/A")
        humidity = current.get("humidity", "N/A")
        wind = current.get("windspeedKmph", "N/A")
        print(f"城市：{city_name}")
        print(f"温度：{temp}°C")
        print(f"天气：{weather_desc}")
        print(f"湿度：{humidity}%")
        print(f"风速：{wind} km/h")

        filename = f"weather_{city_name}.json"
        with open('weather.json', 'w',encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
            print(f"完整天气数据已保存到 {filename}")
except requests.exceptions.RequestException as e:
    print(e)
except (KeyError,IndexError,json.JSONDecodeError) as e:
    print(e)




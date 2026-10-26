print("这是 MBI（测你是偏重还是偏瘦）")

H = float(input("请输入身高 (米) "))
Z = float(input("请输入体重 (kg) "))

MBI = H/Z**2
if MBI <18.5:
    print("太瘦了 杂鱼~❤️")
elif 18.5 < MBI < 24:
    print("体重正常 Ciallo～(∠・ω< )⌒★")
elif 24 < MBI < 28:
    print("有点胖了喵 =￣ω￣=")
else :
    print("你觉得自己胖吗 ε=ε=ε=┏(゜ロ゜;)┛")
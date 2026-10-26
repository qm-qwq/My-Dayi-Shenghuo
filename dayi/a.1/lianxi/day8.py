

# ff = open(r"D:\python\a.txt", "a")
# ff.write("qaddabendan")
# ff = open(r"D:\python\a.txt", "r")
# print(c)

fff = open(r"D:\python\a.txt", "w")
fff.write("\n亲爱的杂鱼 \n亲爱的大笨蛋 \n亲爱的大坏蛋")
fff.close()


a = input("请输入要补充的")
with open(r"D:\python\a.txt", "a") as f:
    b = f.write(a)
    print(f"{b}")

ff = open(r"D:\python\a.txt", "r")
c = ff.readlines()
print(c)


for m,n in enumerate(c,1):
    print(f"{m}: {n}")
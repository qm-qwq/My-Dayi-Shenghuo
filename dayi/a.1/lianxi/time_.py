# 导入time标准库
from datetime import datetime  # 用来打印当前时间

# 第一次打印当前时间
print("第一次时间：", datetime.now())

# 等待3秒
time.sleep(3)

# 第二次打印当前时间
print("第二次时间：", datetime.now())

print("第一次时间：", time.ctime())
time.sleep(3)
print("第二次时间：", time.ctime())
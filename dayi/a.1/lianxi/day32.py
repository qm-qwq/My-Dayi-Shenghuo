# import pyautogui #控制鼠标 键盘 截屏 点击 输入文字
#
#
# pyautogui.FAILSAFE = True #（默认开启）   fail 故障 safe保护
# pyautogui.PAUSE = 0.5 #添加短暂延迟 便于手动干预 帕斯-停


# width, height = pyautogui.size() #获取屏幕尺寸
# print(width, height)
#
# x,y = pyautogui.position() #当前鼠标位置
# print(x,y)
#
# print(pyautogui.onScreen(100,100)) #Screen 屏幕
#
# pyautogui.moveTo(100,200,duration = 1)  # 移动鼠标到 （x,y,时间（秒））
# pyautogui.moveRel(50,0,duration = 0.5) #从当前鼠标位置相对移动 （右，下）带负号就是左上
#
# #点击
# pyautogui.click()  #当前位置点击
# pyautogui.click(200,300)  #移动坐标位置点击
# pyautogui.doubleClick() #douoble 两次  就是双击
# pyautogui.rightClick() #右键
# pyautogui.middleClick() #中建 middle 中间
#
# #拖拽
# pyautogui.drag(100,0,duration = 0.5) #向右拖拽100像素
# pyautogui.dragTo(500,500,duration = 1) #拖拽到指定坐标
#
# #输入文本（不支持中文）
# pyautogui.write("Hello World",interval = 0.1)
# #按下单个键
# pyautogui.press('enter') # press 按压
# pyautogui.press('up') #向上的键
# #组合键
# pyautogui.hotkey('ctrl','c') #hot 热的 key 键 热键组合键
#
# #截屏
# im = pyautogui.screenshot() #screen 屏幕 shot 拍摄
# im.save(r'D:\python\test.png')
# #在当前屏幕寻找图片（返回坐标 点击）
# location = pyautogui.locateOnScreen(r'D:\python\桌面壁纸.png') #locate 定位 在 屏幕
# if location:
#     center = pyautogui.center(location)
#     pyautogui.click(center)






# import time
# import pyautogui
# pyautogui.hotkey('winleft', 'r')
# pyautogui.write("notepad",interval=0.1)
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(2)
# pyautogui.press('shift')
# time.sleep(1)
# pyautogui.write('Hello from pyautogui!',interval=0.2)
# time.sleep(2)
# pyautogui.hotkey('ctrl','s',interval=1)
# time.sleep(1)
# pyautogui.write('auto.txt',interval=0.1)
# time.sleep(1)
# pyautogui.hotkey('Alt','F4',interval=1)
# print("结束")














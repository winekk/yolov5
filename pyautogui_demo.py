import pyautogui

# 获取屏幕分辨率大小
width,height = pyautogui.size()
print(f"宽{width},高{height}")

# 获取当前鼠标的位置
x,y = pyautogui.position()
print(x,y)

# """
# 检查XY坐标是否在屏幕上
# 如果它们位于屏幕的边界内 返回为True;否则 返回Flase
# param: 两个证书参数(int)或两个证书的单个元组或列表
# """
# isScreen = pyautogui.onScreen(x,y)
# print(isScreen)

# 鼠标运动
# 传递坐标后 光标移到该为止 (绝对位置)
# pyautogui.moveTo(X,Y)
"""
如果希望鼠标主键移动到新位置 需要在函数中
传入第三个参数 应采取的持续时间(秒) 默认为0.1S
这里示例花费2S
"""
# pyautogui.moveTo(100,200,2)
# # 相对位置移动
# pyautogui.move(0,-100,2)

# """
# 移动到100,200的位置
# 点击鼠标左键 拖动鼠标至1,1的屏幕像素点的绝对位置
# 花费耗时两秒
# pyatuogui.drag()  相对位置
# """
# pyautogui.moveTo(1000,500,2)
# pyautogui.dragTo(500,1,button='left',duration=2)


# # """
# # 鼠标点击事件
# # 获取屏幕上像素点位置进行点击
# # duration: 持续时间(3s)
# # clicks: 点击次数(双击两下)
# # interval: 间隔(0.1s)
# # """
# pyautogui.click(500,500,button='left',duration=3,clicks=2,interval=0.1)


"""
鼠标滚轮滚动
1000为向下滚动
-1000为向上滚动
"""
pyautogui.scroll(1000)
pyautogui.scroll(-1000)
pyautogui.scroll(500,x=x,y=y)
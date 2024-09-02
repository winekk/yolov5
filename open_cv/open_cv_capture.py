import cv2
import pyautogui
"""
根据file_path读取image 数据
imshow() -> 显示图片
waitKey() -> 等待键盘输入
"""
def get_xy(img_model_path):
    template = cv2.imread("./open_cv/template/py.png", 0)
    img = cv2.imread("./open_cv/pic/all.png", 0)
    # 读取模板的宽度 和 高度
    height, width = template.shape
    # 找到最佳匹配位置
    res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 左上角的坐标为
    upper_left = min_loc
    # 右下角坐标为
    lower_right = (upper_left[0]+width,upper_left[1] + height)
    avg = ((int(upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))

    return avg,min_loc

def auto_click(var_avg):
    pyautogui.click(var_avg[0],var_avg[1],button="left",clicks=10,interval=1)

def run(img_model_path,name):
    avg,min_loc = get_xy(img_model_path)
    pyautogui.moveTo(avg[0],avg[1])
    # pyautogui.moveTo(min_loc[0],min_loc[1])
    # auto_click(avg)

run("..",'')
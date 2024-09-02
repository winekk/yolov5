
import torch

"""
param1 本文件夹下面的测试图片
param2 解析模型为yolov5s
param3 如果为本地的数据源则填写local数据
"""
# Model
model = torch.hub.load("./","yolov5s",source="local")

#%%
# Images
img = "./data/images/zidane.jpg"

# Inference
results = model(img)

# Result
results.show()
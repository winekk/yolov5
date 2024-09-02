import torch
import gradio as gr
model = torch.hub.load("./", model="custom",
                       path="runs/train/exp/weights/best.pt", source="local")


title = "基于Gradio的yolov5检测项目"
desc = "这是一个基于Gradio的检测项目 目前正在学习中"
"""
构造gr绘图
inputs 传入
outputs 传出
fn 预测结果 可以用默认表达式来表达
入参为img
lambda img: model(img).render()[0]
.lauch() -> 启动
"""

"""
    这个image 其实是 gr.image()
 gr.Interface(inputs=[gr.image()], outputs=[gr.image()], title=title,
            description=desc, fn=lambda img: model(img).render()[0]).launch()
 gr.Interface(inputs=["image"], outputs=["image"], title=title,
              description=desc, fn=lambda img: model(img).render()[0]).launch()
"""

# 这个是绑定关系 其实inputs 和 outputs 是和fn(既function做绑定的关系
# 组件会自动的识别到 然后根据你新增的conf 和 iou  调整model的数据的大小
# live 实时更改 不用submit
def det_image(img,conf,iou):
    model.conf = conf
    model.iou = iou
    return model(img).render()[0]

base_conf,base_iou = 0.25,0.45

gr.Interface(inputs=[gr.Image(),gr.Slider(minimum=0,maximum=1,value=base_conf),gr.Slider(minimum=0,maximum=1,value=base_iou)], outputs=[gr.Image()], title=title,
             description=desc, fn=det_image,live=True).launch()

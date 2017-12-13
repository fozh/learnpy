#!/usr/local/bin/python3
from PIL import Image

im = Image.open('wm.gif')
#讲图片转化为8位像素模式
im.convert('P')
#颜色直方图
print(im.histogram())
import numpy as np  
import cv2 
import matplotlib.pyplot as plt
# 1.20 图像拆分通道 (Numpy切片)
img1 = cv2.imread("Lenna.png", flags=1)  # flags=1 读取彩色图像(BGR)

# 获取 B 通道
bImg = img1.copy()  # 获取 BGR
bImg[:, :, 1] = 0  # G=0
bImg[:, :, 2] = 0  # R=0

# 获取 G 通道
gImg = img1.copy()  # 获取 BGR
gImg[:, :, 0] = 0  # B=0
gImg[:, :, 2] = 0  # R=0

# 获取 R 通道
rImg = img1.copy()  # 获取 BGR
rImg[:, :, 0] = 0  # B=0
rImg[:, :, 1] = 0  # G=0

# 消除 B 通道
grImg = img1.copy()  # 获取 BGR
grImg[:, :, 0] = 0  # B=0

plt.subplot(221), plt.title("1. B channel"), plt.axis('off')
bImg = cv2.cvtColor(bImg, cv2.COLOR_BGR2RGB)  # 图片格式转换：BGR(OpenCV) -> RGB(PyQt5)
plt.imshow(bImg)  # matplotlib 显示 channel B
plt.subplot(222), plt.title("2. G channel"), plt.axis('off')
gImg = cv2.cvtColor(gImg, cv2.COLOR_BGR2RGB)
plt.imshow(gImg)  # matplotlib 显示 channel G
plt.subplot(223), plt.title("3. R channel"), plt.axis('off')
rImg = cv2.cvtColor(rImg, cv2.COLOR_BGR2RGB)
plt.imshow(rImg)  # matplotlib 显示 channel R
plt.subplot(224), plt.title("4. GR channel"), plt.axis('off')
grImg = cv2.cvtColor(grImg, cv2.COLOR_BGR2RGB)
plt.imshow(grImg)  # matplotlib 显示 channel GR
plt.show()

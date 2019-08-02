import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
 
lena = mpimg.imread('test.png') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
# lena.shape #(512, 512, 3)

backImage = np.array([0.0, 0.0, 0.0, 0.0])
# 取出图片宽度
c = len(lena[0])
# 取出图片高度
k = len(lena)

dataList = np.zeros(c, np.float16) 

print('图片宽度: ' + str(c) + 'px 图片高度: ' + str(k) + 'px')

for key1 in range(0, c):
  for value2 in range(0, k):
    value = lena[value2][key1]
    # print((value == backImage).all())
    # print(backImage)
    # break
    if (value != backImage).all():
      # print(key1, value2 / k)
      dataList[key1] = 1 - (value2 / k)
      break

print(dataList)
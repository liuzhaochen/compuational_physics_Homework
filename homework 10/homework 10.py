# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 22:13:49 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D 



t1=time.clock()
maxIter = 3000 #迭代次数
delta = 1 #循环中间隔
colorinterpolation = 50 #颜色图的颜色设置
colourMap = plt.cm.jet

X, Y = np.meshgrid(np.arange(0, 10.1,0.1), np.arange(0, 10.1,0.1)) #X,Y为网格
V= np.zeros((101, 101)) #设置一个101X101矩阵
V.fill(5) #将矩阵中所有值填充为5
V[41:62,41:62]=1  # 中心正方形区域的电势为1
V[:1,:]=0 #最上端电势为0
V[100:,:]=0 #最下端电势为0
V[:,:1]=0 #最左端电势为0
V[:,100:]=0 #最右端电势为0
for iteration in range(0, maxIter):
    for i in range(1, 101-1, delta):
        for j in range(1, 101-1, delta):
            V[i, j] = 0.25 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])
            V[41:62,41:62]=1 #保持中间电势为1
#等值线
C = plt.contour(X, Y, V, 10, colors = 'black', linewidth = 0.5)  # 等值线的设置
plt.clabel(C, inline = True, fontsize = 10) #画等值线
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Isogram of Potenial')
plt.show()
#电势分布
plt.contourf(X, Y, V, colorinterpolation, cmap=colourMap) # 电势颜色图
plt.colorbar() # 颜色图例
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Distribation of Potenial')
plt.show()

fig = plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,V,rstride=1, cstride=1,cmap='rainbow')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('V')

t2=time.clock() #计算计算耗时
print `t2-t1`
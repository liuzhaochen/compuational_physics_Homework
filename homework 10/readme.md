# Homework 10
# Electric Potentials and Fields: Laplace's Equation
## 物基二班 刘兆晨 2015302540110
## Problem 5.1
- 原题：
- Solve for the potential in the prism geometry in Figure 5.4
  即计算二维正方形区域的电势分布，中心有个电势恒为1的正方形区域，而最外层的正方形边界的电势为0。
## Laplace 方程
- 二维无源电场的分布由二维拉普拉斯方程决定，即![](http://latex.codecogs.com/gif.latex?\frac{{\partial}^2V}{{\partial}x^2}+\frac{{\partial}^2V}{{\partial}y^2}=0).
- 而对应的离散化后的递推公式即为Jacobi method：![](http://latex.codecogs.com/gif.latex?T_{i,j}=\frac{1}{4}(T_{i+1,j}+T_{i-1,j}+T_{i,j+1}+T_{i,i+1}))
## 计算代码
- 因为在之前的作业中使用的都是python内置的list方法，而这个方法在我们计算中，对于100x100的矩阵，多次迭代中(3000次)，由于list的数据结构，使得计算效率低下，故在这次作业中学习了numpy的array方法，以及使用numpy的meshgrid函数生成网格，从而画出等值线与电势大小分布。
## 计算结果
- 等值线：
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2010/isogram.png)
- 电势分布图：
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2010/distribution.png)
- 三维分布图：
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2010/3d.png)
## 源代码：
  [源代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2010/homework%2010.py)
```python
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
```

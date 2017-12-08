# Homework 09
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


# Homework 03
# Population Growth Problems
## Problem 01
- 原题:
- ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2003/problem1.6.png)
- 在人口增长的模型中，aN对应新生人口，-bN^2则对应死亡人数。
- ![](http://latex.codecogs.com/gif.latex?\\frac{dN}{dt}\=aN-bN^2)
- 当N的变化率为零时，人口达到平衡,即：![](http://latex.codecogs.com/gif.latex?\\frac{dN}{dt}\=0)
- 可见![](http://latex.codecogs.com/gif.latex?N=\frac{a}{b})
- 由Elur method 可得，递推关系是![](http://latex.codecogs.com/gif.latex?\{N}(t+\triangle{t})=aN\triangle{t}-bN^2\triangle{t}+N(t))
- 在我们的计算中，取![](http://latex.codecogs.com/gif.latex?\\traingle{t}=0.0002)
## 情况一，b等于零
- 当b等于零时，通过直接解方程可知N按指数增长
- 计算结果如图：
- ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2003/Population%20Growth%20%20%20N(0)%3D0.png)
- N=0,a=3,b=0
## 当N(0)较小时
- 当N(0)=10时，选择参数a=10,b=3
- 此时计算结果如图：
- ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2003/Population%20Growth%20%20%20N(0)%3D10.png)
- 可见N开始减小，直到平衡后等于10/3
## 当N(0)较大时
- 当N(0)等于100时，选择参数a=10,b=0.01
- 此时计算结果为：
- ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2003/Population%20Growth%20%20%20N(0)%3D100.png)
- 可见，N的平衡数值为1000

- [源代码](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2003/chapter1.py)

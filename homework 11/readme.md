# Homework 11
# Waves:The Ideal Case
## 物基二班 刘兆晨 2015302540110 
## Problem 6.4
- 原题：
- Study the propagation of wavepackets with other shapes. For example,a guitar string that is plucked has an initial  profile like that shown in Figure6.4. Calculate how this excitation splits and moves with time.
## 波动方程
- 波动方程即为： ![](http://latex.codecogs.com/gif.latex?\frac{{\partial}^2y}{\partial{t}^2}=c^2\frac{{\partial}^2y}{\partial{x}^2})
- 离散化后，![](http://latex.codecogs.com/gif.latex?y(i,n+1)=2[1-r^2]y(i,n)-y(i,n-1)+r^2[y(i+1,n)+y(i-1,n)])
   其中，i代表坐标位置，n为时间，即![](http://latex.codecogs.com/gif.latex?x=i{\Delta}x{\quad}t=n{\Delta}t)  
   而![](http://latex.codecogs.com/gif.latex?r=c{\Delta}t/{\Delta}x)
- 而在计算中，我们固定两端点不动
## 不同形状波包的传播
- 高斯型波包
   即，初始时![](http://latex.codecogs.com/gif.latex?y(x)=exp[-1000(x-x_0)^2)  
   
   初始时:  
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/gauss_i.png)  
   传播的动图：  
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/gauss.gif)
- Maxwell分布型波包
   即，初始时![](http://latex.codecogs.com/gif.latex?y(x)=100x^2e^{-100(x)})
   
   初始，时：  
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/maxwell_i.png)
   传播时的动图：  
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/maxwell.gif)
- x^2突起型波包  
   即，初始时在x=0.15处突起一个x^2分布的波包
   
   初始形状：  
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/x%5E2_i.png)
   传播时：  
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/x%5E2.gif)
- 直线拉起型
   在0.3处，拉起一个幅度为0.5的直线型尖峰：
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/0.3_straight.gif)
- 正弦型波包
   即，初始时![](http://latex.codecogs.com/gif.latex?y(x)=sin(4{\pi}x))
   传播时：  
   ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2011/sin.gif)
 ## 讨论
   可以看到，在上面的计算中，只有高斯型波包劈裂成两个波包向相反方向传播，而其余情况中并没有出现劈裂，都是随时间向右传播，然后在最右端反弹。而正弦波则是驻波，不随时间传播。
   源代码：
   [源代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2011/Homework11.py)

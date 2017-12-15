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
   


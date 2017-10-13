# Homework 04
# Realistic Projectile Motion
## 物基二班 刘兆晨 2015302540110
## Problem 2.7
- 原题：
- ![]()
### 无阻力时的抛物运动
- 在无阻力的抛物运动中，对应的运动方程为：  

  ![](http://latex.codecogs.com/gif.latex?\frac{d^2x}{dt^2}=0\quad\frac{d^y}{dt^2}=-g)
- 将方程降阶后可得到：  

  ![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x\quad\frac{dv_x}{dt}=0)
  ![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y\quad\frac{dv_y}{dt}=-g)
### 考虑空气阻力后
- 在考虑真实情况中，在大气中的运动顶存在空气阻力。
- 诚然，空气阻力的精确描述十分复杂，但是对于抛物运动的炮弹而言，一个较好的近似是平方正比的空气阻力：  
 ![](http://latex.codecogs.com/gif.latex?F_{drag}=-B_2v^2) 该力与速度方向相反
- 故，水平与竖直方向的阻力为：  
 ![](http://latex.codecogs.com/gif.latex?F_{drag,x}=F_{drag}cos(\theta)=-B_2vv_x)  
 ![](http://latex.codecogs.com/gif.latex?F_{drag,y}=F_{drag}sin(\theta)=-B_2vv_y)
- 则，对应的关于![](http://latex.codecogs.com/gif.latex?v_x)与![](http://latex.codecogs.com/gif.latex?v_y)的方程应该加上对应的项。
### 由于海报造成空气密度不同而对于空气阻力的修正
- 空气阻力中，系数![](http://latex.codecogs.com/gif.latex?B_2)是正比与空气密度的。
- 故在考虑到随海拔增加，空气密度相应减小，因此要考虑到对空气密度的修正。
- 在等温模型中，空气密度：  
 ![](http://latex.codecogs.com/gif.latex?\rho={\rho}_0{exp(-\frac{y}{y_0})}\quad{y_0=\frac{K_BT}{mg}=1.0\times10^4})
 
 
 

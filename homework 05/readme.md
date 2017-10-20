
# Homework 05
# Throwing a Baseball:The Effects of Spin
## 物基二班 刘兆晨 2015302540110
## Problem 2.19
- 原题：
- ![]()
### 运动方程
- 由[作业4](https://github.com/liuzhaochen/compuational_physics_N2015302540110/tree/master/homework%2004)我们知道，一个受到空气阻力作业的小球的运动方程应该是：  
![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x\quad\frac{dv_x}{dt}=-{\frac{B_2}{m}}vv_x)  

  ![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y\quad\frac{dv_y}{dt}=-g-{\frac{B_2}{m}}vv_y)  
  ![](http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=v_z\quad\frac{dv_z}{dt}=-{\frac{B_2}{m}}vv_z)  
- 由于棒球表面的不规则性，使得阻力系数会根据速度的变化而变化，一个有效的经验公式是：![](http://latex.codecogs.com/gif.latex?
- 而在棒球运动中，棒球速度远比作业4中的物体小，故z方向与y方向受到的空气阻力足够小，以至于我们可以忽略不计。
### 自传效应
- 由于棒球运动中，棒球作为球体的旋转带来的影响会造成球在运动方向上的偏转。不能将球看作质点处理。必须考虑到Magnus效应。
- 考虑自旋Magnus效应，小球受到一个![](http://latex.codecogs.com/gif.latex?F_M=S_0\vec{\omega}\times\vec{v})
- 对于棒球，![](http://latex.codecogs.com/gif.latex?S_0/m\approx=4.1\times{10^{-4}})
### 考虑自旋后的运动方程
- 考虑Magnus后：  
![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x\quad\frac{dv_x}{dt}=-{\frac{B_2}{m}}vv_x)  

  ![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y\quad\frac{dv_y}{dt}=-g)  
  ![](http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=v_z\quad\frac{dv_z}{dt}=-S_0/m\vec{\omega}\times\vec{v}) 






# Homework 05
# Throwing a Baseball:The Effects of Spin
## 物基二班 刘兆晨 2015302540110
## Problem 2.19
- 原题：
- Model the effect of backspin on the range of a batted ball. Assume an anguler velocity of 2000 rpm.
### 运动方程
- 由[作业4](https://github.com/liuzhaochen/compuational_physics_N2015302540110/tree/master/homework%2004)我们知道，一个受到空气阻力作业的小球的运动方程应该是：  
![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x\quad\frac{dv_x}{dt}=-{\frac{B_2}{m}}vv_x)  

  ![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y\quad\frac{dv_y}{dt}=-g-{\frac{B_2}{m}}vv_y)  
  ![](http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=v_z\quad\frac{dv_z}{dt}=-{\frac{B_2}{m}}vv_z)  
- 由于棒球表面的不规则性，使得阻力系数会根据速度的变化而变化，一个有效的经验公式是：![](http://latex.codecogs.com/gif.latex?\frac{B_2}{m}=0.0039+\frac{0.0058}{1+exp[\frac{v-v_d}{\triangle}]}\quad)![](http://latex.codecogs.com/gif.latex?{v_d=35m\s,\triagnle=5m\s})
- 而在棒球运动中，棒球速度远比作业4中的物体小，故z方向与y方向受到的空气阻力足够小，以至于我们可以忽略不计。
### 自传效应
- 由于棒球运动中，棒球作为球体的旋转带来的影响会造成球在运动方向上的偏转。不能将球看作质点处理。必须考虑到Magnus效应。
- 考虑自旋Magnus效应，小球受到一个![](http://latex.codecogs.com/gif.latex?F_M=S_0\vec{\omega}\times\vec{v})
- 对于棒球，![](http://latex.codecogs.com/gif.latex?S_0/m\approx=4.1\times{10^{-4}})
### 考虑自旋后的运动方程
- 考虑Magnus后：  
![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x\quad\frac{dv_x}{dt}=-{\frac{B_2}{m}}vv_x)  

  ![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y\quad\frac{dv_y}{dt}=-g)  
  ![](http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=v_z\quad\frac{dv_z}{dt}=-\frac{S_0}{m}\vec{\omega}\times\vec{v}) 
### 递推公式
- 这样的微分方程组依旧可以用Eulr Mehod计算
- 对应的递推公式为：  
  ![](http://latex.codecogs.com/gif.latex?x_{i+1}=x_i+v_x{\triangle}t{\quad}v_{x,i+1}=v_{x,i}-{\frac{B_2}{m}}vv_x{\triangle}t)  
  ![](http://latex.codecogs.com/gif.latex?y_{i+1}=y_i+v_y{\triangle}t{\quad}v_{y,i+1}=v_{y,i}-g{\triangle}t)  
  ![](http://latex.codecogs.com/gif.latex?z_{i+1}=z_i+v_z{\triangle}t{\quad}v_{z,i+1}=v_{z,i}-\frac{S_0}{m}{\omega}v_{x}{\triangle}t)
### 计算
- 在计算Batted ball时，我们的初速度设置为30m/s，而角速度是2000rpm
#### 45°出射
- 三维图像：  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2005/angle_45%2Cw_2000rpm.png)
 - Z轴偏转距离与x的关系：  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2005/zDEFLECTION_angle_45%2Cw_2000rpm.png)
#### 30°出射
- 三维图像：  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2005/angle_30%2Cw_2000rpm.png)
- Z轴偏转距离与x的关系:  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2005/zDEFLECTION_angle_30%2Cw_2000rpm.png)
#### 60°出射
- 三维图像：  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2005/angle_60%2Cw_2000rpm.png)
- Z轴偏转距离与x的关系:  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2005/zDEFLECTION_angle_60%2Cw_2000rpm.png)
#### Z方向偏转
- Z方向的最大偏转距离与出射角度有关，给出具体曲线：
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2005/deflection.png)
- [源代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2005/homework05.py)





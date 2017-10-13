# Homework 04
# Realistic Projectile Motion
## 物基二班 刘兆晨 2015302540110
## Problem 2.7
- 原题：
- ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/problem2.7.png)
### 无阻力时的抛物运动
- 在无阻力的抛物运动中，对应的运动方程为：  

  ![](http://latex.codecogs.com/gif.latex?\frac{d^2x}{dt^2}=0\quad\frac{d^2y}{dt^2}=-g)
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
### 由于海拔高度造成空气密度不同而对于空气阻力系数的修正
- 空气阻力中，系数![](http://latex.codecogs.com/gif.latex?B_2)是正比与空气密度的。
- 故在考虑到随海拔增加，空气密度相应减小，因此要考虑到对空气密度的修正。
- 在等温模型中，空气密度：  
 ![](http://latex.codecogs.com/gif.latex?\rho={\rho}_0{exp(-\frac{y}{y_0})}\quad{y_0=\frac{K_BT}{mg}=1.0\times10^4m})  
- 但是，等温模型过于粗糙。因为我们知道，随着海拔的增加，温度必然会降低。
- 绝热近似模型会是一个更好的近似。这时密度![](http://latex.codecogs.com/gif.latex?\rho={\rho_0}(1-\frac{ay}{T_0})^{\alpha})  
 其中，![](http://latex.codecogs.com/gif.latex?a=6.5\times10^{-3}\{K/m})而![](http://latex.codecogs.com/gif.latex?\alpha=2.5)
- 虽然这两种对阻力系数的修正是不同的，但是对于我们的方程，我们只需要将![](http://latex.codecogs.com/gif.latex?B_2)替换为![](http://latex.codecogs.com/gif.latex?B_2\frac{\rho}{\rho_0})
### 地面温度变化对阻力系数的影响
- 再考虑到空气密度对空气阻力的修正之后，我们进一步考虑由于地面温度变化造成对阻力系数的影响。
- 此时应该将![](http://latex.codecogs.com/gif.latex?B_2)替换为![](http://latex.codecogs.com/gif.latex?B^{ref}_2(\frac{T_0}{T_{ref}})^\alpha)
- ![](http://latex.codecogs.com/gif.latex?T_0)是海平面温度。
- 这里T=300K是参考温度，在我们的问题考虑中，遵循书上的标定![](http://latex.codecogs.com/gif.latex?\frac{B^{ref}_2}{m}=4\times10^{-5}m^{-1})
### Eulr Method 递推关系
#### 绝热模型的递推公式：
- ![](http://latex.codecogs.com/gif.latex?x_{i+1}=x_i+v_{x,i}{\triangle}t)
- ![](http://latex.codecogs.com/gif.latex?y_{i+1}=y_i+v_{y,i}{\triangle}t)
- ![](http://latex.codecogs.com/gif.latex?v_{x,i+1}=v_{x,i}-{\frac{B^{ref}_2}{m}(\frac{T_0}{T_{ref}})^\alpha}{(1-\frac{ay}{T_0})^{\alpha}}vv_{x,i}{\triangle}t)
- ![](http://latex.codecogs.com/gif.latex?v_{y,i+1}=v_{y,i}-g{\triangle}t-{\frac{B^{ref}_2}{m}(\frac{T_0}{T_{ref}})^\alpha}{(1-\frac{ay}{T_0})^{\alpha}}vv_{y,i}{\triangle}t)
#### 等温模型的递推公式：
- ![](http://latex.codecogs.com/gif.latex?x_{i+1}=x_i+v_{x,i}{\triangle}t)
- ![](http://latex.codecogs.com/gif.latex?y_{i+1}=y_i+v_{y,i}{\triangle}t)
- ![](http://latex.codecogs.com/gif.latex?v_{x,i+1}=v_{x,i}-{\frac{B^{ref}_2}{m}(\frac{T_0}{T_{ref}})^\alpha}{exp(-\frac{y}{y_0})}vv_{x,i}{\triangle}t)
- ![](http://latex.codecogs.com/gif.latex?v_{y,i+1}=v_{y,i}-g{\triangle}t-{\frac{B^{ref}_2}{m}(\frac{T_0}{T_{ref}})^\alpha}{exp(-\frac{y}{y_0})}vv_{y,i}{\triangle}t)
### 计算结果： 45°出射，切地面温度不同的情况
- 温度273K时：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/45degree_T%3D273k.png)
- 温度283K时：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/45degree_T%3D283k.png)
- 温度293K时：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/45degree_T%3D293k.png)
- 温度303K时: ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/45degree_T%3D303k.png)
- 温度313K时: ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/45degree_T%3D313k.png)
### 计算结果： 293K温度下，不同出射角度的对比
- 45°与60°: ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/45degree_60degree_T%3D293k.png)
- 45°与30°: ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2004/45degree_30degree_T%3D293k.png)
### 源代码
- [源代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2004/homework04.py)
### 结论
- 从上述图片可以看出，在格外考虑到地面温度对阻力的影响时，等温模型下的抛物运动总比绝热模型远。
- 而温度越低，最大距离越远。
### Pygame的尝试
- 尝试使用计算抛物线的结果，将X，Y轴数据接入pygame中直接进行坐标定位。
- 的确成功让图片按照计算的抛物线运动。
- 但是由于代码设计原因，没有达成调整出射角度的想法。
- [pygame 尝试 源代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2004/try.py)


 
 
 
 

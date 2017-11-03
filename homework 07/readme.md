# Homework 07
# Routes to Chaos: Period Doubling
## 物基二班 刘兆晨 2015302540110
## Problem 3.20
- 原题：
- Calculate the bifuraction diagram for the pendulum in the vicinity of FD=1.35 to 1.5. Make a magnified plot of the diagram(as compared to Figure 3.11) and obtain an estimate of the Feigenbaum parameter.
## Bifuraction Diagram  
- 我们知道，对于一个摆长为l的非线性单摆，在存在线性耗散像与周期性驱动力下，对应的动力学方程为![](http://latex.codecogs.com/gif.latex?\frac{d^2\theta}{dt^2}=-\frac{g}{l}sin{\theta}-q\frac{d\theta}{dt}+F_Dsin{\Omega_Dt})其中![](http://latex.codecogs.com/gif.latex?q)为耗散系数，![](http://latex.codecogs.com/gif.latex?F_D)为驱动力幅度，![](http://latex.codecogs.com/gif.latex?\Omega_D)为驱动力周期。  
  而在这样的简单模型中，随着驱动力幅度的改变仍可以出现混沌现象，而在驱动力振幅在某些范围内时，系统的运动周期扔和驱动力周期有简单关系。例如，在FD=1.35   时，系统周期是驱动力周期的1倍，而1.44时为2倍。  
  
- 为了判断什么时候会出现混沌现象，我们需要引入Bifuraction Diagram。即将![](http://latex.codecogs.com/gif.latex?\theta)作为![](http://latex.codecogs.com/gif.latex?F_D)画出。这里的![](http://latex.codecogs.com/gif.latex?\theta)是指满足![](http://latex.codecogs.com/gif.latex?{\Omega_D}t=2n\pi)的点，n为整数。
## 参数选取
- 在下面的计算中，我们选取初始角度为0.01，而耗散系数为0.5，驱动力周期![](http://latex.codecogs.com/gif.latex?\Omega_D=\frac{2}{3})计算步长![](http://latex.codecogs.com/gif.latex?{\triangle}t=0.01)
- 而由于我们的计算步长总是有限的，所以![](http://latex.codecogs.com/gif.latex?{\Omega_D}t=2n\pi)肯定无法严格满足。故我们用不等式![](http://latex.codecogs.com/gif.latex?|t-\frac{2n\pi}{\Omega_D}|<{\triangle}t)来作为限制条件选择去点。
## 计算结果
- Bifurcation计算结果如下：
- [](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2007/bifurcation.png)
- 而我们按照FD=1.2，计算出![](http://latex.codecogs.com/gif.latex?\theta)与![](http://latex.codecogs.com/gif.latex?\omega)的图为：
- [](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2007/omega_theta_fd%3D1.2.png)
### 分析
    这里计算的两个图都有问题，第一张图曲线走势没有问题，但是曲线整体偏下，且在1.5处有误。  
    而第二张图，有一部分是正确的，但是不知道为什么多出一块。。。。
    代码给出来：![Bifurcation图](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2007/homework%2007.py)
               ![Poincare section](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2007/homework07_2.py)

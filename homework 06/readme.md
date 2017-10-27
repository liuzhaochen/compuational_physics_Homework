# Homework 06
# Chaos in the Driven Nonlinear Pendulum
## 物基二班 刘兆晨 2015302540110
## Problem 3.13
- 原题:
- Write a program to calculate and compare the behavior of two, nearly identical pendulums Use it to calculate the divergence of two nearby trajectories in the chaotic regime, as in Figure 3.7, and ae a qualitative estimate of the corresponding Lyapunov exponent from the slope of a plot of log(delta theta)as a function of t.
### 非线性摆的动力学方程
- 对于一个摆长为l的非线性单摆，在存在线性耗散像与周期性驱动力下，对应的动力学方程为![](http://latex.codecogs.com/gif.latex?\frac{d^2\theta}{dt^2}=-\frac{g}{l}sin{\theta}-q\frac{d\theta}{dt}+F_Dsin{\Omega_Dt})其中![](http://latex.codecogs.com/gif.latex?q)为耗散系数，![](http://latex.codecogs.com/gif.latex?F_D)为驱动力幅度，![](http://latex.codecogs.com/gif.latex?\Omega_D)为驱动力周期。
- 对于这样的二阶方程，我们可以选取降阶的方法去计算
- 即![](http://latex.codecogs.com/gif.latex?\frac{d\omega}{dt}=-\frac{g}{l}sin{\theta}-q\frac{d\theta}{dt}+F_Dsin{\Omega_Dt})  
  ![](http://latex.codecogs.com/gif.latex?\frac{d\theta}{dt}=\omega)
### Nearly Identical Pendulums
- 两个除初始角度有微小差别的且其余参数都相同的单摆，虽然初始角度有细微的差距但是![](http://latex.codecogs.com/gif.latex?{\triangle}\theta=|\theta_1-\theta_2|)随时间的变化却因为驱动力参数的不同有着很多不同的形式。
- 如果我们固定初始角度的差值，而改变初始角度，然后取平均结果，我们可以得到![](http://latex.codecogs.com/gif.latex?log({\triangle}\theta)\approx{{\lambda}t}),这个就是lyapunov exponent.
### Euler-Cromer Method
- 因为Euler方法在谐振子系统中的失效而引入了Euler-Cromer方法，修正后的递推关系如下：  
  ![](http://latex.codecogs.com/gif.latex?\omega_{i+1}=\omega_{i}-[\frac{g}{l}sin\omega_i+q\omega_i-F_Dsin\Omega_Dt_i]{\triangle}t)  
  ![](http://latex.codecogs.com/gif.latex?\theta_{i+1}=\theta_i+\omega_{i+1}{\triangle}t)
### 参数设置
- 在计算中，我们取l=9.8,g=9.8,q=0.5,![](http://latex.codecogs.com/gif.latex?\Omega_D)为2/3,![](http://latex.codecogs.com/gif.latex?F_D)为可调参数，而初始角速度为零。而演化步长为0.0004s
### 计算结果
- 计算结果如下图，我们在y轴使用了对数坐标。 
- 图中曲线突然直线下降的原因在于，再这个位置![](http://latex.codecogs.com/gif.latex?{\triangle}\theta)等于0，而我们选取的对数坐标对于为值为负无穷大，故出现了这样的现象。  

  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/fd%3D0.5.png)![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/fd%3D0.8.png)
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/fd%3D1.0.png)![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/fd%3D1.2.png)  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/fd%3D1.5.png)![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/fd%3D2.png)  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/FD%3D3.png)
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/fd%3D4.png)  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/FD%3D5.png)![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2006/FD%3D6.png)
### 讨论
- 我们可以从上面的计算图看出，当![](http://latex.codecogs.com/gif.latex?F_D)小于1.0时，![](http://latex.codecogs.com/gif.latex?{\triangle}\theta)是减函数。可以看到![](http://latex.codecogs.com/gif.latex?F_D)等于1.0处是一个转折点。大于1.0如1.2，1.5，3时，![](http://latex.codecogs.com/gif.latex?{\triangle}\theta)的趋势是随时间增大。再对比![](http://latex.codecogs.com/gif.latex?F_D)等于4，5，6的计算结果我们可以看到，![](http://latex.codecogs.com/gif.latex?{\triangle}\theta)的增长趋势也在随着![](http://latex.codecogs.com/gif.latex?F_D)的变化而周期性变化。

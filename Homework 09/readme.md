# Homework 09
# The Solar System
## 物基二班 刘兆晨 2015302540110
## Problem 4.14
- 原题：
- Simulate the orbits of Earth and Moon in the solar system by writing a program that accurate ly tracks the motions of both as they move about the Sun. Be careful about(1)the different time scales present in this problem,and(2)the correct initial velocities(i.e.,set the initial velocity of Moon taking into account the motion of Earth around whitch it orbits)
## The Solar System
- 在处理地球与月球在太阳系中的运动时，由于月球对地球引力相对太阳对地球引力较小，所以可以近似忽略掉月球对地球的影响，而在计算月球轨道时，必须考虑到地球与太阳的同时作用，此时才能正确得到月球在太阳系中的运动规律。而在考虑到太阳引力对月球的影响之后，月球相对地球轨道并不是以回旋的形式前进，而是反复穿过地球轨道，这个结果可以通过下面的计算得到。
## 运动方程
- 地球运动方程：  
  ![](http://latex.codecogs.com/gif.latex?\frac{d^2x}{dt^2}=-\frac{GM_{s}x}{r^3})  
  ![](http://latex.codecogs.com/gif.latex?\frac{d^2y}{dt^2}=-\frac{GM_{s}y}{r^3})  
  其中：![](http://latex.codecogs.com/gif.latex?r=\sqrt{x^2+y^2})
- 月球运动方程：  
  ![](http://latex.codecogs.com/gif.latex?\frac{d^2x_m}{dt^2}=-\frac{GM_{E}(x_m-x)}{R^3}-\frac{GM_{s}x_m}{r^3_m})  
  ![](http://latex.codecogs.com/gif.latex?\frac{d^2y_m}{dt^2}=-\frac{GM_{E}(y_m-y}}{R^3)-\frac{GM_{s}y_m}{r^3_m})  
  其中：![](http://latex.codecogs.com/gif.latex?R=\sqrt{(x_m-x)^2+(y_m-y)^2})  
          ![](http://latex.codecogs.com/gif.latex?r_m=\sqrt{(x_m)^2+(y_m)^2})
- 由于使用自然坐标系在计算行星运动中时，行星运动尺度的巨大性导致其十分不方便，因此引入天文单位：
  即1AU等于太阳与地球间距离的平均单位，而使用年作为时间单位时，可见![](http://latex.codecogs.com/gif.latex?GM_s=4{\pi}^2{AU}^3}/{{yr}^2)
  而![](http://latex.codecogs.com/gif.latex?\frac{M_E}{M_s}\approx{3\times{10^{-6}}})
## 初始条件
  因为在我们的计算中使用了天文单位制，所以我们的初始条件选取为：
- 地球：
  坐标：x=1,y=0; 速度：![](http://latex.codecogs.com/gif.latex?v_x=0\quadv_y=2\pi)
- 月球：
  坐标：x=1+0.00275,y=0; 速度：![](http://latex.codecogs.com/gif.latex?2\pi+2\pi\sqrt{\frac{1}{0.00275}\frac{M_E}{M_s}})
## 计算结果：
- 轨迹图：
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Homework%2009/Figure_1.png)
- 放大后的轨迹：
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Homework%2009/Figure_1-1.png)  
  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Homework%2009/Figure_1-2.png)
  可见，月球轨道(蓝色)在运动中，多次往复穿过地球轨道(红色)，可见，我们定性分析中，对月球轨道与地球轨道的关系的判断是正确的。
  
  [计算原代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/Homework%2009/homework9.py)

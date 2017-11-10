# Homework 08
# The Billiard Problem
## 物基二班 刘兆晨 2015302540110
## Problem 3.31
- 原题：
- Study the behavior for other types of tables. One interesting possibility is a square table with a circular interior wall located either in the center, or slightly off-center.Another possibility is an elliptical table.
## The Billiard Problem
- 当一个硬球在无摩擦的平面内运动时，当球碰到平面边界（可以是矩形，也可以是椭圆）时，会和边界发生碰撞，我们要求碰撞是弹性碰撞，那么球会反弹回去。在一般对称性较低的台面上，会经常看到混沌现象。我们现在研究球在椭圆内的情况。
## 椭球方程
- 这里我们讨论中心在坐标原点的椭球，即![](http://latex.codecogs.com/gif.latex?\frac{x^2}{a^2}+\frac{y^2}{b^2}=1)  
  这里我们选取a=4,b=2
- 为了让球在边界处弹性碰撞，我们需要知道椭圆的法向量![](http://latex.codecogs.com/gif.latex?\vec{n})而碰撞对速度造成的影响为：  我们
![](http://latex.codecogs.com/gif.latex?{\vec{v^'}}_{\bot}=-(\vec{v}\cdot\vec{n})\vec{n}\quad)  ![](http://latex.codecogs.com/gif.latex?{\vec{v^'}}_{\shortparallel}={\vec{v^}}_{\shortparallel}=\vec{v}-{\vec{v^}}_{\bot})
- 即 ![](http://latex.codecogs.com/gif.latex?{\vec{v^'}}={\vec{v}}-2(\vec{v}\cdot\vec{n})\vec{n})
- 由椭圆方程可知，椭圆的单位法向量即为![](http://latex.codecogs.com/gif.latex?{\vec{n}}=\frac{(\frac{2x}{a^2},\frac{2y^2}{b^2})}{\sqrt{\frac{4x^2}{a^4}+\frac{4y^2}{b^4}}})
- 由此即可计算出碰撞后的速度。
## 计算结果与讨论
### 初始位置在原点，不同方向的结果
- 10°时：
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0%2C0angle10.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0%2C0angle10.png)  
- 15°时：
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0%2C0angle15.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0%2C0angle15.png)
- 30°时：
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0%2C0angle30.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0%2C0angle30.png)
- 40°时：
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0%2C0angle40.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0%2C0angle40.png)
- 60°时：
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0%2C0angle60.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0%2C0angle60.png)
### 初始方向固定为与x轴夹角30°，而初始位置不同时：
- x=0.001,y=0:
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0.001%2C0angle30.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0.001%2C0angle30.png)
- x=0.01,y=0.01:
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0.01%2C0.01angle30.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0.01%2C0.01angle30.png)
- x=0.1,y=0.1:
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D0.1%2C0.1angle30.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D0.1%2C0.1angle30.png)
- x=1,y=1:
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D1%2C1angle30.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D1%2C1angle30.png)
- x=2,y=0:
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D2%2C0angle30.png)  ![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D2%2C0angle30.png)
### x=3,y=0.5,角度为60°时：
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/x%2Cy%3D3%2C0.5angle60.png)
![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/homework%2009/phase_space_x%2Cy%3D3%2C0.5angle60.png)
### 结论
从上面的计算结果我们可以看到，在椭圆的情况下，由于椭圆是对称性非常高的图像，在这个边界线之下，混沌现象并没有出现（至少在我们的计算中）。而计算结果也具有高度的对程序
源代码：[代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/homework%2009/homework%2008.py)



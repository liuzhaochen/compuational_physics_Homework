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
- 为了让球在边界处弹性碰撞，我们需要知道椭圆的法向量![](http://latex.codecogs.com/gif.latex?\vec{n})而碰撞对速度造成的影响为：  
![](http://latex.codecogs.com/gif.latex?{\vec{v^'}}_{\bot}=-(\vec{v}\cdot\vec{n})\vec{n}\quad)  ![](http://latex.codecogs.com/gif.latex?{\vec{v^'}}_{\shortparallel}={\vec{v^}}_{\shortparallel}=\vec{v}-{\vec{v^}}_{\bot})
- 即 ![](http://latex.codecogs.com/gif.latex?{\vec{v^'}={\vec{v}}-2(\vec{v}\cdot\vec{n})\vec{n})
- 由椭圆方程可知，椭圆的单位法向量即为![](http://latex.codecogs.com/gif.latex?{\vec{n}}=\frac{(\frac{2x}{a^2},\frac{2y^2}{b^2})}{\sqrt{\frac{4x^2}{a^4}+\frac{4y^2}{b^4}}})
- 由此即可计算出碰撞后的速度。
## 计算结果与讨论
### 初始位置在原点，不同方向的结果

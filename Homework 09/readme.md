# Homework 09
# The Solar System
## 物基二班 刘兆晨 2015302540110
## Problem 4.14
- 原题：
- Simulate the orbits of Earth and Moon in the solar system by writing a program that accurate ly tracks the motions of both as they move about the Sun. Be careful about(1)the different time scales present in this problem,and(2)the correct initial velocities(i.e.,set the initial velocity of Moon taking into account the motion of Earth around whitch it orbits)
## The Solar System
- 在处理地球与月球在太阳系中的运动时，由于月球对地球引力相对太阳对地球引力较小，所以可以近似忽略掉月球对地球的影响，而在计算月球轨道时，必须考虑到地球与太阳的同时作用，此时才能正确得到月球在太阳系中的运动规律。而在考虑到太阳引力对月球的影响之后，月球相对地球轨道并不是以回旋的形式前进，而是反复穿过地球轨道，这个结果可以通过下面的计算得到。

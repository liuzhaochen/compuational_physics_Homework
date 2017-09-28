# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:01:06 2017

@author: liuzc
"""

import  numpy as np
import matplotlib.pyplot as plt
import math
N=10 #初始值
c=[]
T=np.arange(0,1000,0.0002)
t=0
a=3
b=0
while t<999.9998:
    t=t+0.0002
    c.append(N)
    N=a*N*0.0002-b*N*N*0.0002+N
x1=np.linspace(0,10)
y1=10*math.e**(a*x1)    
plt.axis([0,5,0,1200])
plt.title('Population growth   N(0)=10 a=3 b=0')
plt.ylabel('Population')
plt.xlabel('Time')
plt.plot(T,c)
plt.plot(x1,y1,'--')
plt.show()


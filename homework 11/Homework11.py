# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:27:04 2017

@author: liuzc
"""


import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import animation

fig,ax=plt.subplots()
t1=time.clock()
c=300
dt=2
dx=0.001
r=1


X=1

X=np.arange(0,X,dx)
T=2000

Y= np.zeros((T,len(X)))
#初始波形
for i in range(0,len(X),1):

            Y[0][i]=100*(i*dx)**2*np.exp(-100*((i*dx)**2))
            Y[1][i]=100*(i*dx)**2*np.exp(-100*((i*dx)**2))
   
#计算
for j in range(1,T-1,1):
    for i in range(0,len(X)-1,1):
        Y[j+1][i]=2*(1-r**2)*Y[j][i]-Y[j-1][i]+r**2*(Y[j][i+1]+Y[j][i-1])
        Y[j][0]=0
        Y[j][len(X)-1]=0
    

#for i in range(10,T,10):
    #plt.plot(X,Y[i],label='T:'+`dt*i`)
   # plt.legend(loc='up')
    #plt.ylim(-1,1)
    
    #plt.pause(0.01)

fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = X
    y = Y[i]
    #plt.title(`i`+'s')
    line.set_data(x, y)
    return line,
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=T, interval=8, blit=True)
plt.show()  
#anim.save('line.gif', dpi=80)
t2=time.clock() #计算计算耗时
print `t2-t1`
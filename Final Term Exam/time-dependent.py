# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:55:10 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

import time
t1=time.clock()
dx=0.0005
dt=5*10**(-7)
X=np.arange(0,1,dx)

T=0.7*10**(-3)#演化总长

V=np.zeros((1,len(X)),dtype=complex)#势能
psi=np.zeros((int(T/dt)+2,len(X)),dtype=complex)
Psi=np.zeros((len(X),len(X)),dtype=complex)
PP=np.zeros((len(X),len(X)),dtype=complex)
B=np.arange(0,len(X),1,dtype=complex)
lembda=2*dx**2/dt

V[0][1200:1300]=10**5#x>0.6处，一个很高的势垒

psi[0]=np.exp(-10**3*(X-0.4)**2-100000j*X)  #k=10**5
t1=time.clock()

t=0



#初始两个矩阵
for i in range(2,len(X)-1):
        Psi[0][0]=1
        Psi[0][1]=2j*lembda-2
        Psi[i-1][i-2]=1
        Psi[i-1][i-1]=2j*lembda-2-2*dx**2*V[0][i-1]
        Psi[i-1][i]=1
        Psi[len(X)-2][len(X)-3]=1
        Psi[len(X)-2][len(X)-2]=2j*lembda-2-2*dx**2*V[0][len(X)-2]
        Psi[len(X)-2][len(X)-1]=1
        Psi[len(X)-1][len(X)-2]=1
        Psi[len(X)-1][len(X)-1]=2j*lembda-2-2*dx**2*V[0][len(X)-2]
for i in range(1,len(X)-2):
        PP[0][0]=-1
        PP[0][1]=2j*lembda+2
        PP[i-1][i-2]=-1
        PP[i-1][i-1]=2j*lembda+2+2*dx**2*V[0][i-1]
        PP[i-1][i]=-1
        PP[len(X)-2][len(X)-3]=-1
        PP[len(X)-2][len(X)-2]=2j*lembda+2+2*dx**2*V[0][len(X)-2]
        PP[len(X)-2][len(X)-1]=-1
        PP[len(X)-1][len(X)-2]=-1
        PP[len(X)-1][len(X)-1]=2j*lembda+2+2*dx**2*V[0][len(X)-2]

j=0

#计算
while t<T:

    B=np.dot(PP,psi[j].T)
    x = np.linalg.solve(Psi,B)
    a=np.shape(x)
    if a>2:
        x=x.T
    psi[j+1]=x
    t+=dt
    #print `np.int(t*100/T)`   
    j+=1 
    t3=time.clock() 
    print `t3-t1`
#动图
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)
def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = X

    y = np.abs(psi[i])**2
    #plt.title(`i*dt`+'s')
    line.set_data(x,y)
    return line,
anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=int(T/dt), interval=10,blit=True)    
plt.show()  

t2=time.clock() 
print `t2-t1`   
    


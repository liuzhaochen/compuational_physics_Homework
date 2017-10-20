# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:45:19 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax=Axes3D(fig)
t_1=time.clock()
w=2000*math.pi*2/60 # angular velocity of bell
g=9.8
dt=0.002
S_0_m=4.1*10**(-4)
Zd=[]
class shell:
    def setvalue(self, m,n):
        self.m=m
        self.n=n
        self.Xn=[]
        self.Yn=[]
        self.Zn=[]
    
    def caculate(self):
        x=0.0
        y=0.0
        z=0.0
        v=30.0 #initial velocity
        B2_m_ref=0.0039+0.0058/(1+math.exp((v-35)/5))   #referencec B/m
        vx=v*math.cos(self.m)
        vy=v*math.sin(self.m)
        vz=0
        t=0.0
        while y>=0:
            self.Xn.append(x)
            self.Yn.append(y)
            self.Zn.append(z)
            t=t+0.002
            v=math.sqrt(vx**2+vy**2+vz**2)
            a_x_drag=B2_m_ref*v*vx
        #((1-a*y/T_0)**alpha is caused by the dependence of the density on altitude
            x=vx*dt+x
            y=y+vy*dt
            z=z+vz*dt
            vx=vx-a_x_drag*dt
            vy=vy-g*dt
            vz=vz-S_0_m*vx*w*dt
    def plot(self):
        plt.xlim(0,100)
        plt.ylim(-15,0)
        ax.plot(self.Xn,self.Zn,self.Yn,label='angle'+'='+'60degree')
        plt.legend(loc='upper right')
        ax.set_xlabel('X')
        ax.set_ylabel('Z')
        ax.set_zlabel('y')
        plt.show()

        
    def xd(self):
        lenth=len(self.Zn)
        plt.plot(self.Xn,self.Zn,label='Deflection distance of z:'+`self.Zn[lenth-1]`+'m')
        plt.xlabel('X(m)')
        plt.ylabel('Z(m)')
        plt.legend(loc='lower right')
        plt.plot(m,self.Zn[lenth-1])
        plt.show()
    def zd(self):
        lenth=len(self.Zn)
        Zd.append(self.Zn[lenth-1])
        

def pltzd():
    plt.plot(z,Zd)
    plt.title('function of maxium deflection distance of z ')
    plt.xlabel('inital ganle')
    plt.ylabel('deflection distance of Z')    

c=shell()
c.setvalue(math.pi/4,2)
c.caculate()
c.plot()
c.xd()

z=np.arange(0,1.57,0.01)
for m in z:
    
    d=shell()
    d.setvalue(m,1)
    d.caculate()
    d.zd()
pltzd()
plt.show()

t_2=time.clock()
print 'Caculation time:'+`t_2-t_1`




        
        
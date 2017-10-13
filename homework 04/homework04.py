# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:45:19 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time
t_1=time.clock()


T_0=273.0 #temperature of sea level
T=300.0 #reference temperature
g=9.8
a=6.5*(10**(-3))
B2_m_ref=4*(10**(-5))  #referencec B/m
alpha=2.5
B2_m=B2_m_ref*((T_0/T)**alpha) #B/m when y=0
dt=0.002

class shell:
    def setvalue(self, m,n):
        self.m=m
        self.n=n
        self.Xn=[]
        self.Yn=[]
    
    def caculate(self):
        x=0.0
        y=0.0
        v=700.0 #initial velocity
        vx=v*math.cos(self.m)
        vy=v*math.sin(self.m)
        t=0.0
        while t<999.998:
            self.Xn.append(x)
            self.Yn.append(y)
            t=t+0.002
            v=math.sqrt(vx**2+vy**2)
            a_x_drag=B2_m*v*vx*((1-a*y/T_0)**alpha) 
        #((1-a*y/T_0)**alpha is caused by the dependence of the density on altitude
            a_y_drag=B2_m*v*vy*((1-a*y/T_0)**alpha)
            x=vx*dt+x
            y=y+vy*dt
            vx=vx-a_x_drag*dt
            vy=vy-g*dt-a_y_drag*dt
    def plot(self):
        plt.axis([0,60000,0,10000])
        plt.plot(self.Xn,self.Yn,label='angle'+'='+`self.m`+'  adiabatic model  '+'T='+`T_0`+'K')
        plt.legend(loc='upper right')
        plt.xlabel('X(m)')
        plt.ylabel('Y(m)')

y_0=10**4
class isothermal:   #对应等温模型
    def setvalue2(self, m,n):
        self.m=m
        self.n=n
        self.Xn=[]
        self.Yn=[]
    def caculate2(self):
        x=0.0
        y=0.0
        v=700.0
        vx=v*math.cos(self.m)
        vy=v*math.sin(self.m)
        t=0.0
        while t<999.998:
            self.Xn.append(x)
            self.Yn.append(y)
            t=t+0.002
            v=math.sqrt(vx**2+vy**2)
            a_x_drag=B2_m*v*vx*(math.exp(-y/y_0))
            a_y_drag=B2_m*v*vy*(math.exp(-y/y_0))
            x=vx*dt+x
            y=y+vy*dt
            vx=vx-a_x_drag*dt
            vy=vy-g*dt-a_y_drag*dt
    def plot2(self):
        plt.axis([0,60000,0,10000])
        plt.plot(self.Xn,self.Yn,label='angle'+'='+`self.m`+'  isothermal model')
        plt.legend(loc='upper right')
        plt.xlabel('X(m)')
        plt.ylabel('Y(m)')
c1=isothermal()
c1.setvalue2(math.pi/4,1)
c1.caculate2()
c2=shell()
c2.setvalue(math.pi/4,1)
c2.caculate()
c2.plot()
c1.plot2()
plt.show()
t_2=time.clock()
print 'Caculation time:'+`t_2-t_1`




        
        
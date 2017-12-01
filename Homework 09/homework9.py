# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:10:17 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time

dt=0.001
Dt=dt
t_1=time.clock()
M=3*10**(-6)
class cl:
    def setvalue(self,earthV,moonV):
        self.EX=[1,]
        self.EY=[0,]
        self.MX=[1+0.00257,]
        self.MY=[0,]
        
        self.Evx=[0,]
        self.Evy=[earthV,]
        
        self.Mvx=[0.0,]
        self.Mvy=[moonV,]
        
        self.M=M

    def calculate(self):
        t=0
        i=0
        while t<1:
            #Earth
            x_i=self.EX[i]
            y_i=self.EY[i]
            v_xi=self.Evx[i]
            v_yi=self.Evy[i]
            
            r_i=math.sqrt(x_i**2+y_i**2)
            v_xj=v_xi-4*(math.pi*math.pi)*x_i*dt/(r_i*r_i*r_i)
            v_yj=v_yi-4*(math.pi*math.pi)*y_i*dt/(r_i*r_i*r_i)
            x_j=x_i+v_xj*dt
            y_j=y_i+v_yj*dt
            self.EX.append(x_j)
            self.EY.append(y_j)
            self.Evx.append(v_xj)
            self.Evy.append(v_yj)
            #Moon
            X_i=self.MX[i]
            Y_i=self.MY[i]
            v_Xi=self.Mvx[i]
            v_Yi=self.Mvy[i]
            R_i=np.sqrt((X_i-x_i)*(X_i-x_i)+(Y_i-y_i)*(Y_i-y_i))
            l_i=np.sqrt((X_i)*(X_i)+(Y_i)*(Y_i))
            #这个计算是在地球坐标系里面
            v_Xj=v_Xi-4*(math.pi*math.pi)*(X_i-x_i)*self.M*Dt/(R_i**3)-4*(math.pi*math.pi)*X_i*Dt/(l_i*l_i*l_i)
            v_Yj=v_Yi-4*(math.pi*math.pi)*(Y_i-y_i)*self.M*Dt/(R_i**3)-4*(math.pi*math.pi)*Y_i*Dt/(l_i*l_i*l_i)
            X_j=X_i+(v_Xj)*Dt
            Y_j=Y_i+(v_Yj)*Dt
            self.MX.append(X_j)
            self.MY.append(Y_j)
            self.Mvx.append(v_Xj)
            self.Mvy.append(v_Yj)
            i=i+1
            t=t+dt
    def plot(self):
        plt.figure(figsize=(100,100)) 
        plt.xlabel('X/AU')
        plt.ylabel('Y/AU')
        plt.plot(self.EX,self.EY,color="red",linewidth=1.0,label='Orbits of Earth')
        plt.plot(self.MX,self.MY,color='blue',linewidth=1.0,label='Orbits of Moon')
        plt.legend(loc='upper left')
        plt.xlim(-2.5,2.5)
        plt.ylim(-1.5,1.5)
        plt.title('The Orbits of Earth and Moon')


a=cl()
a.setvalue(2*math.pi,2*math.pi*np.sqrt(M/0.00257)+2*math.pi)
a.calculate()
a.plot()
t_2=time.clock()
print `2*math.pi*np.sqrt(M/0.00257)`

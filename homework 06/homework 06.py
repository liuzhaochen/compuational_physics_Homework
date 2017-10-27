# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:02:50 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time

dt=0.0004
t_1=time.clock()
class cal:

    def setvalue(self,b,q,f,n):
        self.n=n
        self.__dict__['b%d'%self.n]=b
        self.__dict__['q%d'%self.n]=q
        self.__dict__['f%d'%self.n]=f
        self.__dict__['w%d'%self.n]=[0,]
        self.__dict__['theta%d'%self.n]=[self.__dict__['b%d'%n],]
    def calculate(self):

        self.T=[0,]

        t=0
        i=0
        while t<150-dt:
            w_i=self.__dict__['w%d'%self.n][i]
            theta_i=self.__dict__['theta%d'%self.n][i]
            w_j=w_i-(math.sin(theta_i)+self.__dict__['q%d'%self.n]*w_i-self.__dict__['f%d'%self.n]*math.sin((2.0/3.0)*t))*dt
            theta_j=theta_i+w_j*dt
            self.__dict__['w%d'%self.n].append(w_j)
            self.__dict__['theta%d'%self.n].append(theta_j)
            t=t+dt
            i=i+1
            self.T.append(t)
        
        

    def plot(self):
        plt.plot(self.__dict__['theta%d'%self.n],self.__dict__['w%d'%self.n],label="theta_inital="+`self.__dict__['b%d'%self.n]`+" ")
        plt.xlabel=('theta')
        plt.ylabel=("omega")
        plt.xlim(-3.14,3.14)
        plt.ylim(-4,4)
        plt.show()
    def w(self):
        return self.__dict__['theta%d'%self.n]
class diver():
    def divervalue(self,b,q,f,d): #b角度的初始值 q衰减系数 f驱动力系数 #d两角度的插值
        self.b=b
        self.q=q
        self.f=f
        self.d=d
    def diverplot(self):
        a1=cal()
        a1.setvalue(self.b,self.q,self.f,1)
        a2=cal()
        a2.setvalue(self.b+self.d,self.q,self.f,2)
        a1.calculate()
        a2.calculate()
        T=np.arange(0,150,dt)
        W=(np.array(a2.w()-np.array(a1.w())))
        #把W里面的数改为绝对值
        for i in range(len(W)):
            if W[i]<0:
                W[i]=-W[i]
        plt.xlim(0,150)
        plt.ylim(10**(-17),100)
        plt.xlabel('time(s)')
        plt.ylabel('delta theta')
        self.Y=10**(-3)*math.e**(-0.3*np.array(T))
        plt.plot(T,self.Y,label="lamdba=-0.3")
        plt.semilogy(T,W,label="delta theta="+`self.d`+'   FD='+`self.f`)
        plt.legend(loc='donwer right')


        

a=diver()
a.divervalue(0.1,0.5,6,0.001)
a.diverplot()
t_2=time.clock()
print `t_2-t_1`
        

        



        


        
            
        

        
     
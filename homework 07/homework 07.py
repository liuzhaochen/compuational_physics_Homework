# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 10:34:33 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time
from progressbar import ProgressBar

dt=0.04
t_1=time.clock()
class cal:
    def setvalue(self,b,q): #b初始角度 

        self.b=b
        self.q=q
        self.omega=[0,]
        self.theta=[self.b,]
        self.FD=[]
        self.theta_f=[]
    def calculate(self):
        #self.T=[0,]
        pbar = ProgressBar().start()
        f=np.arange(1.35,1.5,0.001)
        j=0
        n=range(200,401)
        for self.f in f:
            i=0
            t=0
            
            while t<400*3*math.pi:
                w_i=self.omega[i]
                theta_i=self.theta[i]
                w_j=w_i-(math.sin(theta_i)+self.q*w_i-self.f*math.sin((2.0/3.0)*t))*dt
                theta_j=theta_i+w_j*dt
                self.omega.append(w_j)
                self.theta.append(theta_j)
                t=t+dt
                i=i+1
                #self.T.append(t)
                if t>300*3*math.pi:
                    for m in n:
                        if t>3*m*math.pi-dt/2:
                            if t<3*m*math.pi+dt/2:
                                self.theta_f.append(math.fmod(theta_j,math.pi))
                                self.FD.append(self.f)

                            
            pbar.update(j + 1)
        
            
                
                 
            #length=len(self.theta)
            #self.theta_f.append(self.theta[length-1])
            self.omega=[0,]
            self.theta=[self.b,]
        pbar.finish()
    def plot(self):
        plt.xlabel('FD')
        plt.ylabel('theta')
        plt.scatter(self.FD,self.theta_f,color="red",s=0.2)
        plt.show()
        #print self.theta_f
  


a=cal()
a.setvalue(1,0.5)
a.calculate()
a.plot()
    
    


t2=time.clock()

print `t2-t_1`
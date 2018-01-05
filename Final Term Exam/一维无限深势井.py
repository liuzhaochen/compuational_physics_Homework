# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:48:09 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt

import time
t1=time.clock()
dx=0.001
X=np.arange(0,2,0.001)
Psi=np.zeros((1,len(X)))



def calculate():
    Psi[0][1]=dx
    E=4.9398
    dE=0.00001
    DE=0.001
    j=0
    while E>0:
        
        for i in np.arange(1,len(X)-1,1):
            Psi[0][i+1]=2*Psi[0][i]-Psi[0][i-1]-2*dx**2*(E)*Psi[0][i]
        if np.abs(Psi[0][len(X)-1])<10**(-4):
            plt.plot(X,Psi[0],label='level n=2')
            plt.title('E='+`round(E,6)`)
            plt.legend(loc='upper right')
            plt.xlabel('x')
            plt.ylabel('Psi')
            plt.show()
            break
            
        if np.abs(Psi[0][len(X)-1])>10**(-2):

            E=E+DE
        if Psi[0][len(X)-1]<0 and Psi[0][len(X)-1]<-10**(-2):
            
            E=E-DE
        if np.abs(Psi[0][len(X)-1])<10**(-2) and np.abs(Psi[0][len(X)-1])>10**(-4):
            #dE=0.001
            if Psi[0][len(X)-1]>0:
                E=E+dE
            if Psi[0][len(X)-1]<0:
                E=E-dE
        print `j`
        j=j+1
        print 'E:'+`E`
        print 'PSI:'+`Psi[0][len(X)-1]`
calculate()











t2=time.clock() #计算计算耗时
print `t2-t1`
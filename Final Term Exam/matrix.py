# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:45:13 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import eign
import time
t1=time.clock()
dx=0.01
X=np.arange(0,10,dx)
Psi=np.zeros((1,len(X)))

H=np.zeros((len(X),len(X)))
for i in np.arange(1,len(X)-1,1):
    x_i=(i-500)*dx
    V_i=0.5*x_i**2 #lennard-jones  10,1  x=0.5 to x=10
    H[i][i]=2.0/(2*dx**2)+V_i
    H[i+1][i]=-1.0/(2*dx**2)
    H[i-1][i]=-1.0/(2*dx**2)
    
    H[0][0]=2.0/(2*dx**2)
    H[1][0]=-1.0/(2*dx**2)
    H[len(X)-2][len(X)-1]=-1.0/(2*dx**2)
    H[len(X)-1][len(X)-1]=2.0/(2*dx**2)+0.5*(500*dx)**2

n=np.arange(0,10,1)
eign.Eigs(H,len(n),0.0001)  
plt.plot(n,eign.Eign,label='numerical solution')
plt.plot(n,(n+0.5),label='theorical solution')
plt.legend(loc='upper left')
plt.show()
plt.plot(n,np.abs(eign.Eign-(n+0.5))/(n+0.5),label='relative error')
plt.legend(loc='upper left')


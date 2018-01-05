# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:55:10 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import time
t1=time.clock()
dx=0.01
X=np.arange(0,10,dx)
##初始试探波函数
psi=np.zeros((1,len(X)))
#psi[0]=np.exp(-(X-1)**2)
for i in range(200,600):
    psi[0][i]=np.random.uniform(0,1)   

#积分
#def inte(f,N):
    #s=0
    #for k in range(N):
        #s +=dx*f(k)
    #return s


dpsi=0.1


#哈密顿量
Ha=np.zeros((len(X),len(X)))
for i in np.arange(1,len(X)-1,1):
    x_i=(i-500)*dx
    V_i=16*0.5*x_i**2 #lennard-jones  10,1  x=0.5 to x=10
    Ha[i][i]=2.0/(2*dx**2)+V_i
    Ha[i+1][i]=-1.0/(2*dx**2)
    Ha[i-1][i]=-1.0/(2*dx**2)
    
    Ha[0][0]=2.0/(2*dx**2)
    Ha[1][0]=-1.0/(2*dx**2)
    Ha[len(X)-2][len(X)-1]=-1.0/(2*dx**2)
    Ha[len(X)-1][len(X)-1]=2.0/(2*dx**2)+16*0.5*(500*dx)**2

#H平均值
def H(z):
    return np.dot(psi[0],np.dot(Ha,psi[0]))
#概率分布
def n(z):
    P=psi[0]*psi[0]
    return P[z]
    
    
    
j=1.0
p=0
while j<10**5:
    
    E=H(1)
    Normal=np.dot(psi[0],psi[0])
    E_N=E/Normal#归一化
    k=np.int(np.random.uniform(0,len(X)-1))
    m=np.random.uniform(0,1)
    if m>0.5:
        psi[0][k]+=dpsi
        
    if m<0.5:
        psi[0][k]-=dpsi
        
    
    e=H(1)
    normal=np.dot(psi[0],psi[0])
    e_n=e/normal#改变之后的能量
    if e_n<E_N:
        None
        print 'yes'
        p+=1
    if e_n>E_N:
        if m>0.5:
            psi[0][k]-=dpsi
            
        if m<0.5:
            psi[0][k]+=dpsi
        print 'no'
    j+=1
    print j/10**3
    print 'E/N:'+`E_N`+'   e/n'+`e_n`+'   delta:'+`p`
plt.plot(X,psi[0])
t2=time.clock() #计算计算耗时
print `t2-t1`   
    
   
    

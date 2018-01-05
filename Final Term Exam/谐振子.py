# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:17:43 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt

import time
t1=time.clock()
dx=0.001
X=np.arange(0,8,0.001)  #坐标
Psi=np.zeros((2,len(X)))

e=[]
l=[0,1,2,3,4,5]
psi=np.zeros((10,len(X)))
##matching method
def calculate():
    Psi[0][1]=dx
    Psi[1][len(X)-2]=dx
    
    
    

    E=0.5#初始能量
    for n in l:
        Psi[0][0]=0
        Psi[1][len(X)-1]=0
        if (n % 2) == 1: 
           Psi[0][1]=-dx   
        if (n % 2) == 0: 
           Psi[0][1]=dx 
        #根据奇偶性，确定断点导数正负
        
        j=0#j为计算次数
        f=[]
        DDE=0.4
        dE=0.01
        z=5
        
        while j>=0:  
            x=np.sqrt(E/2.0)
            x=np.int(x/dx)
            for i in np.arange(1,len(X)-1,1):
                Psi[0][i+1]=2*Psi[0][i]-Psi[0][i-1]-2*dx**2*(E-2*(dx*(i-len(X)/2))**2)*Psi[0][i]
                Psi[1][len(X)-i-2]=2*Psi[1][len(X)-i-1]-Psi[1][len(X)-i]-2*dx**2*(E-2*(dx*(len(X)-i-1-len(X)/2))**2)*Psi[1][len(X)-i-1]
                
                #判断满足条件与否
            
            # F为判定标准
            F=(Psi[0][x-1]-Psi[1][x-1])/Psi[0][x]
            f.append(F)
            print `F`
            print 'E'+`E`
            if n>=4:
                z=10
            if np.abs(F)<10**(-z):
                e.append(E)
                for m in np.arange(0,x,1):
                    psi[n][m]=Psi[0][m]
                for m in np.arange(x,len(X)-1):
                    psi[n][m]=Psi[1][m]
                break
            
            if j>1:
                if f[j]*f[j-1]<0:
                    dE=-dE/10
                    print 'ssssssssssssssssssssssssssss'
            E=E+dE
            j=j+1

        E=E+DDE
        print 'newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
        f
calculate()
plt.xlim(0,6)
plt.plot(l,e,marker='.',label='numerical analysis')
plt.plot(X,2*X+1,label='theory energy')
plt.legend(loc="upper left")
plt.xlabel('n')
plt.ylabel('energy')
plt.show()

for m in l:
    #plt.ylim(-6,6)
    plt.plot(X,psi[m],label='level'+`m`)
    plt.legend(loc='upper right')
    plt.show()







t2=time.clock() #计算计算耗时
print `t2-t1`
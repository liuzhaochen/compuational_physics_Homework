# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:30:42 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time
fig = plt.figure()
class ball:
    def setvalue(self,initial_x,initial_y,initial_angle,initial_speed):
        self.x=initial_x
        self.y=initial_y
        self.angle=initial_angle
        self.theta=np.deg2rad(initial_angle)
        self.speed=initial_speed
        self.X=[self.x,]
        self.Y=[self.y,]
        self.VX=[np.cos(self.theta)*self.speed,]
    def curve(self):
        #椭圆
        m=np.linspace(-5,5,num=1000)
        a=4
        b=2
        y=b*np.cos(m)
        x=a*np.sin(m)
        plt.plot(x,y)

    
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        t=0
        #椭圆方程

        vx=np.cos(self.theta)*self.speed
        vy=np.sin(self.theta)*self.speed
        
        X=self.x
        Y=self.y
        while t<150:
            dt=0.0003
            ddt=dt/1000
            t+=dt
            X=vx*dt+X
            Y=vy*dt+Y
            self.X.append(X)
            self.Y.append(Y)
            self.VX.append(vx)
            if Y>0:
                XX=X/a
                
                if Y>b*np.sin(np.arccos(XX)):
                    normal=4*X*X/(a*a*a*a)+4*Y*Y/(b*b*b*b)
                    zx=8*(vx*X/(a*a)+Y*vy/(b*b))*X/(a*a*normal)
                    zy=8*(vx*X/(a*a)+Y*vy/(b*b))*Y/(b*b*normal)
                    
                    vx=vx-zx
                    vy=vy-zy
                    X=vx*ddt+X
                    Y=vy*ddt+Y
                    self.X.append(X)
                    self.Y.append(Y) 
                    self.VX.append(vx)
                    #print `vx`
                    
                    
                    
            if Y<0 :
                XX=X/a
                if Y<-b*np.sin(np.arccos(XX)):
                    #print 'Y:'+`Y`
                    #print `-b*np.sin(np.arccos(X/a))`                    
                    normal=4*X*X/(a*a*a*a)+4*Y*Y/(b*b*b*b)
                    zx=8*(vx*X/(a*a)+Y*vy/(b*b))*X/(a*a*normal)
                    zy=8*(vx*X/(a*a)+Y*vy/(b*b))*Y/(b*b*normal)
                    vx=vx-zx
                    vy=vy-zy
                    X=vx*ddt+X
                    Y=vy*ddt+Y
                    self.X.append(X)
                    self.Y.append(Y)
                    self.VX.append(vx)
            if Y==0:

                if X>0:
                    if X>a:
                        normal=4*X*X/(a*a*a*a)+4*Y*Y/(b*b*b*b)
                        zx=8*(vx*X/(a*a)+Y*vy/(b*b))*X/(a*a*normal)
                        zy=8*(vx*X/(a*a)+Y*vy/(b*b))*Y/(b*b*normal)
                        vx=vx-zx
                        vy=vy-zy
                        X=vx*ddt+X
                        Y=vy*ddt+Y
                        self.X.append(X)
                        self.Y.append(Y)
                        self.VX.append(vx)
                if X<0:
                    if X<-a:
                        normal=4*X*X/(a*a*a*a)+4*Y*Y/(b*b*b*b)
                        zx=8*(vx*X/(a*a)+Y*vy/(b*b))*X/(a*a*normal)
                        zy=8*(vx*X/(a*a)+Y*vy/(b*b))*Y/(b*b*normal)
                        vx=vx-zx
                        vy=vy-zy
                        X=vx*ddt+X
                        Y=vy*ddt+Y
                        self.X.append(X)
                        self.Y.append(Y)
                        self.VX.append(vx)                        


        plt.plot(self.X,self.Y,linewidth=0.5) 
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('initial x:'+`self.x`+'  initial y:'+`self.y`+' initial angle:'+`self.angle`)
        #plt.savefig('x,y='+`self.x`+','+`self.y`+'angle'+`self.angle`+'.png', format='jpg', dpi=300)
        #plt.clf()
        plt.show()
        plt.scatter(self.X,self.VX,s=0.1)
        plt.xlabel('X')
        plt.ylabel('Vx')
        plt.title('initial x:'+`self.x`+'  initial y:'+`self.y`+' initial angle:'+`self.angle`)
        #plt.savefig('phase_space_x,y='+`self.x`+','+`self.y`+'angle'+`self.angle`+'.png', format='jpg', dpi=300)
        #plt.clf()
        plt.show()
        
        
a=ball()
a.setvalue(-3.5,0,20,2)
a.curve()





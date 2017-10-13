# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:21:22 2017

@author: liuzc
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import pygame as py
import sys
from pygame.locals import QUIT
from pygame.locals import KEYUP
from pygame.locals import KEYDOWN
import time



#主程序
py.init()
screen = py.display.set_mode((800,600))
py.display.set_caption("Throwing")
font=py.font.Font(None,18)

space=py.image.load(r"F:\ProgramData\compution physics\ss\background.jpg").convert_alpha()
class shell:
    def setvalue(self, m,n):
        self.m=m
        self.n=n
        self.Xn=[]
        self.Yn=[]
    

    def a(self):
        i=0
        mm=self.m
        x=0.0
        y=0.0
        v=100.0
        vx=v*math.cos(mm)
        vy=v*math.sin(mm)
        
        while True:
            
            for event in py.event.get():
                if event.type == QUIT:
                    sys.exit()
                    py.quit()
                if event.type == KEYUP:
                    mm=mm+0.05
                if event.type == KEYDOWN:
                    mm=mm-0.05
            T_0=293.0 #temperature of sea level
            T=300.0 #reference temperature
            g=9.8
            a=6.5*(10**(-3))
            B2_m_ref=4*(10**(-5))  #referencec B/m
            alpha=2.5
            B2_m=B2_m_ref*((T_0/T)**alpha) #B/m when y=0
            dt=0.002



            
            self.Xn.append(x)
            self.Yn.append(y)

            v=math.sqrt(vx**2+vy**2)
            a_x_drag=B2_m*v*vx*((1-a*y/T_0)**alpha) 
        #((1-a*y/T_0)**alpha is caused by the dependence of the density on altitude
            a_y_drag=B2_m*v*vy*((1-a*y/T_0)**alpha)
            x=vx*dt+x
            y=y+vy*dt
            vx=vx-a_x_drag*dt
            vy=vy-g*dt-a_y_drag*dt
            py.display.update()
            screen.blit(space, (0,0))
            
            
            
            
            shell=py.image.load(r"F:\ProgramData\compution physics\ss\shell.png").convert_alpha()
            screen.blit(shell, (self.Xn[i],600-self.Yn[i]))
            py.display.update()
            print `mm`


            i=i+1
    def plot(self):
        plt.axis([0,800,0,600])
        plt.plot(self.Xn,self.Yn)
        plt.show()


c=shell()
c.setvalue(math.pi/4,1)
c.a()
c.plot()


       



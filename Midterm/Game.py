# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:04:04 2017

@author: liuzc
"""
background_image='F:\ProgramData\compution physics\pygame\Background.jpg'
shell_image='F:\ProgramData\compution physics\pygame\shell.png'
caon_image='F:\ProgramData\compution physics\pygame\caon.png'
ufo_image='F:\ProgramData\compution physics\pygame\ufo.jpg'


import pygame 
from pygame.locals import *
from gameobjects.vector2 import Vector2
from sys import exit
import math
import time
import random

pygame.init()
screen=pygame.display.set_mode((1114,752),0,32)
#title of game
pygame.display.set_caption("GO!KILL QB IN UFO")
#背景图片
background=pygame.image.load(background_image).convert()
shell_img=pygame.image.load(shell_image).convert_alpha()
caon=pygame.image.load(caon_image).convert_alpha()
ufo=pygame.image.load(ufo_image).convert_alpha()
#缩放
caon=pygame.transform.scale(caon,(200,136))
shell_img=pygame.transform.scale(shell_img,(60,40))
ufo=pygame.transform.scale(ufo,(100,42))


clock = pygame.time.Clock()
time_passed = clock.tick(60)
timeP = time_passed / 1000.0

shell_pos=Vector2(10,400) #initial position
shell_theta=0 #initial angle
g=1 #g
G=Vector2(0,g)
shell_speed=10 #initial speed
start_time = time.clock() 

#记录时间
def TIME():  
    over_time = time.clock()  
    used_time = over_time - start_time  
    global time_sec, time_min, time_hour  
    time_sec = int(used_time % 60)  
    time_min = int((used_time // 60) % 60)  
    time_hour = int((used_time // 60) // 60)     
#字体
score_font = pygame.font.SysFont('tahoma.ttf', 40)  
time_font = pygame.font.SysFont('tahoma.ttf', 40) 
score_word= pygame.font.SysFont('tahoma.ttf', 40)  
time_word= pygame.font.SysFont('tahoma.ttf', 40) 
angle=pygame.font.SysFont('tahoma.ttf', 40) 
speed=pygame.font.SysFont('tahoma.ttf', 40) 
life=pygame.font.SysFont('tahoma.ttf', 40) 
#起始分数
score = 0
yy=400
#
l=10
class shell():
    def __init__(self):
        self.screen=screen
        self.x=[]
        self.y=[]
        self.moving=None
        self.shell_pos=Vector2(220,400)

    def life(self):
        global l
        l=l-1
        if l<0:
            self.Restart()
                
    
    def start_move(self,theta,speed):
        self.moving=True
        self.theta=theta
        self.speed=speed
        
        self.velocity=Vector2(math.cos(self.theta),-math.sin(self.theta))*self.speed
        self.screen.blit(shell_img,self.shell_pos)
        self.life()

            
        
    def stop_move(self):
        self.moving=False
        self.shell_pos=Vector2(220,400)
        global yy
        yy=random.uniform(40,442)
        #停止运动，重置位置



    def move(self):

        
        if self.moving==True:
            
            self.velocity+=G*timeP
            self.shell_pos+=self.velocity*timeP
            self.R=math.atan(self.velocity.y/self.velocity.x)
            self.screen.blit(shell_img,self.shell_pos)
            print `self.shell_pos`
        if self.moving==False:
            
            None
    def score(self):
        global score
        global yy
        if self.shell_pos.x>750:
            if self.shell_pos.y>yy:
                if self.shell_pos.y<yy+42:
                    
                    if self.speed<10:
                        score+=1
                    
                    if self.speed>10 and self.speed<20:
                        score+=5
                    if self.speed>20 and self.speed<30:
                        score+=10
                    if self.speed>40 and self.speed<50:
                        score+=20
                    if self.speed>50:
                        score+=30
                    self.stop_move()
        if self.shell_pos.x>1114:
            self.stop_move()
        if self.shell_pos.y<0:
            self.stop_move()
        if self.shell_pos.y>752:
            self.stop_move()

    def Restart(self):
        global score 
        global l
        self.stop_move()
        score=0
        l=10


            

        


                       

class main():
    def __init__(self):
        
        self.Shell=shell()
        self.angle=shell_theta
        self.speed=shell_speed
    #画图
    def draw(self):
        global yy
        screen.blit(background,(0,0))
        screen.blit(caon,(20,400))
        screen.blit(ufo,(850,yy))
        #分数
        global score
        score_surface = score_font.render('{0}'.format(score), True, (0, 0, 0))
        screen.blit(score_surface,(700, 100))
        score_word=score_font.render('Score',True, (0,0,0))
        screen.blit(score_word,(700,50))
        #时间
        TIME()  
        time_surface = time_font.render('{0:0>2}:{1:0>2}:{2:0>2}'.format(time_hour, time_min, time_sec), True, (0, 0, 0))
        screen.blit(time_surface,(700, 200)) 
        time_word=score_font.render('Time',True, (0,0,0))
        screen.blit(time_word,(700,150))
        
        #角度
        angle_surface=angle.render('{0}'.format(math.degrees(self.angle)),True,(0,0,0))
        screen.blit(angle_surface,(900,100))
        angle_word=angle.render('Angle',True,(0,0,0))
        screen.blit(angle_word,(900,50))
        #速度
        speed_surface=speed.render('{0}'.format(int(self.speed)),True,(0,0,0))
        screen.blit(speed_surface,(900,200))
        speed_word=speed.render('Speed',True,(0,0,0))
        screen.blit(speed_word,(900,150))
        # life time
        global l
        life_surface=life.render('{0}'.format(l),True,(0,0,0))
        screen.blit(life_surface,(100,100))
        life_word=life.render('Life Remaining',True,(0,0,0))
        screen.blit(life_word,(100,50))
    def run(self):
        
        while True:
            self.draw()
            

            for event in pygame.event.get():

                if event.type==QUIT:
                    exit()
                
                if event.type==KEYDOWN:
                    if event.key==K_UP:
                        
                        self.angle=self.angle+0.03
                        print 'a'
                        print `self.angle`
                    if event.key==K_DOWN:
                        self.angle=self.angle-0.03
                    if event.key==K_LEFT:
                        self.speed=self.speed-2
                    if event.key==K_RIGHT:
                        self.speed=self.speed+2
                    if event.key==K_SPACE:
                        self.Shell.start_move(self.angle,self.speed)
                    if event.key==K_a:
                        self.Shell.stop_move()
                    if event.key==K_s:
                        self.Shell.Restart()    
                if event.type==KEYUP:
                    if event.key==K_SPACE:
                        #self.Shell.move()
                        None
                        
            self.Shell.move()
            self.Shell.score()
            pygame.display.update()
app=main()
app.run()

            
        
        

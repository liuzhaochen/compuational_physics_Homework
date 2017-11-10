# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:54:02 2017

@author: liuzc
"""

background_image='F:\ProgramData\compution physics\pygame\sushiplate.jpg'
mouse_image='F:\ProgramData\compution physics\pygame\shell.png'
import pygame 
from pygame.locals import *
from gameobjects.vector2 import Vector2
from sys import exit
import math


pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("a")
background=pygame.image.load(background_image).convert()
sprite=pygame.image.load(mouse_image).convert_alpha()#convert把图像转换为surface对象

clock = pygame.time.Clock()
 
sprite_pos = Vector2(100, 400)   # 初始位置
sprite_speed = 300.     # 每秒前进的像素数（速度）
sprite_rotation = 60.      # 初始角度
sprite_rotation_speed = 360. # 每秒转动的角度数（转速）
g=Vector2(0,500000)
speed=500
while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    pressed_keys = pygame.key.get_pressed()
 
    rotation_direction = 0.
    movement_direction = 0.
    screen.blit(background, (0,0))
    # 更改角度
    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    roted_sprite=pygame.transform.rotate(sprite,sprite_rotation)
    w,h=roted_sprite.get_size()
    sprite_draw_pos=Vector2(sprite_pos.x-w/2,sprite_pos.y-h/2)
    screen.blit(roted_sprite,sprite_draw_pos)
    
    time_passed=clock.tick()
    timeP=time_passed/1000.0
    
    sprite_rotation=sprite_rotation+rotation_direction*sprite_rotation_speed*timeP
    
    
    vdirection_x=math.cos(sprite_rotation*math.pi/180)
    vdirection_y=math.sin(sprite_rotation*math.pi/180)
    
    e_v=Vector2(vdirection_x,-vdirection_y)
    
    V=e_v*speed+g*timeP
    
    sprite_pos=sprite_pos+V*timeP
    pygame.display.update()

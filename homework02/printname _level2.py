# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:53:46 2017

@author: liuzc
"""

import os
import sched,time
import sys

l=('  #   ',
   '  #   ',
   '  #   ',
   '  #   ',
   '  #   ')
i=('# ',
   '  ',
   '# ',
   '# ',
   '# ')
u=(' #   #  ',
   ' #   #  ',
   ' #   #  ',
   ' #   #  ',
   '  ###   ')
z=('   ##### ',
   '      #  ',
   '     #   ',
   '    #    ',
   '   ##### ')
h=(' #     ',
   ' #     ',
   ' ####  ',
   ' #  #  ',
   ' #  #  ')
a=('  ###  ',
   ' # #   ',
   '#   #  ',
   ' #  ## ',
   '  ##  #')
o=('  ###   ',
   ' #   #  ',
   '#     # ',
   ' #   #  ',
   '  ##    ')
c=('     ### ',
   '    #    ',
   '   #     ',
   '    #    ',
   '     ### ')
e=('  ###   ',
   ' #   #  ',
   '#####   ',
   ' #      ',
   '  ###   ')
n=('##### ',
   '#   # ',
   '#   # ',
   '#   # ',
   '#   # ')
m=(l,i,u,z,h,a,o,c,h,e,n)
def mm():
    y=0
    while y<=4 :
        x=0
        while x<=10:
            print m[x][y],  #加逗号不会换行  
            x=x+1
        print     #用一个空格来换行
        y=y+1
    

t=0
tt=0
while True:
    os.system('cls')  #用os.system('cls')来清屏
    #while循环用于打出空格行
    while True:
        print ''
        tt=tt+1
        if tt>t:    #tt>t控制了空格行的个数
            tt=0
            break
    t = t+1
    mm()
    if t>10:      #t=11的时候从头来
        t=0
    time.sleep(0.5)
    
    
    
    


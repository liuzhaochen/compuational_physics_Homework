# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:53:46 2017

@author: liuzc
"""

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
#打印每个字母的第一行后，换行再打第二行，直到结束
y=0
while y<=4 : 
    x=0
    while x<=10:
        print m[x][y],  #加逗号不会换行  
        x=x+1
    print     #用一个空格来换行
    y=y+1


# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:20:20 2017

@author: liuzc
"""

import scipy as sp  
import scipy.sparse.linalg  
import scipy.io as sio   
import numpy as np  
from numpy import *
import time  
import os  


def Eigs(X,m,tolerance):  
        k=m
        A=X#后面的A表示在matlab中名字  
        timeCheckin=time.clock()  
        #tol=0表示使用原先的计算精度  
        vals, vecs = sp.sparse.linalg.eigs(A, k,tol=tolerance,which="SM")  
        print("first"+`k`+" eigenvalues cost %s seconds" % (time.clock()-timeCheckin))  
        print("first"+`k`+"eigenvalues are %s" % vals)  
        global Eign,Vec
        Vec=vecs.T
        Eign=vals
        #nRow,nCol=A.get_shape()  
        for i in range(0,k):  
                print("error of lamda is %s " % (np.linalg.norm(A.dot(vecs[:,i])-vals[i]*vecs[:,i])))  
        #for i in range(0,k):  
                #v=np.random.rand(nCol)  
                ##v must be normalization  
                #v=v/np.linalg.norm(v)  
                #print("random error is %s " % (np.linalg.norm(A.dot(v)-vals[i]*v)))  
        print 'Eign='+`Eign`

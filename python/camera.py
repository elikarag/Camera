# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:33:04 2015

@author: Elissaios
"""

import numpy as np
import math

#folder = 'c:\Users\Elissaios\Box Sync\Projects\fMRI\analysis1'
folder = r"c:\Users\Elissaios\Box Sync\Projects\fMRI\analysis1";

path = folder + r"\camera.txt";
camera_1d = np.loadtxt(path);

P = len(camera_1d)
#dim=camera_1d.shape

#matplotlib

myArr = np.asarray(camera_1d)

#dim=myArr.shape
sq = int(math.sqrt(P))

my2d = myArr.reshape(sq,sq)
my2d = np.rot90(my2d,3)
my2dBW = my2d.copy()
my2dBW[my2dBW>0.1] = 1
my2dBW[my2dBW<=0.1] = 0
plt.imshow(my2d)
#plt.imshow(my2dBW,'gray')

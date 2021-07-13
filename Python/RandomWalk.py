# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:28:02 2021

@author: minhv
"""

import pandas as pd
import numpy as np
from scipy import stats
import math
from matplotlib import pyplot as plt

eps = np.random.normal(size=(100,1))
rw = np.zeros((100,1))

rw[0] = 0.8 + eps[0]
for i in range(1,100,1):
    rw[i] = 0.8 + 1*rw[i-1] + eps[i]
    

plt.plot(rw)

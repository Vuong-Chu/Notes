# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:42:00 2021

@author: minhv
"""

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, range(1000)))
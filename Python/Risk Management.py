# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:12:58 2021

@author: minhv
"""

import pandas as pd
import numpy as np
from scipy import stats
import math
from matplotlib import pyplot as plt

##1.1##
if __name__ == "__main__":
    sp500 = pd.read_csv("1.1.csv",index_col=0)
    sp500_removed = sp500.loc[(sp500.shift(-1)!=sp500).loc[:,"Close"]]
    daily_log_return = sp500_removed.iloc[1:,:].copy() #When we wanna copy instead of replacing values in the old data
    daily_log_return["Close"] = np.log(sp500_removed.loc[:,"Close"].iloc[1:].values/sp500_removed.loc[:,"Close"].iloc[:-1].values).tolist()
    mean_return = daily_log_return.mean().values[0]
    variance_return = daily_log_return.var().values[0]
    skewness_return = daily_log_return.skew().values[0]
    kurtosis_return = daily_log_return.kurtosis().values[0]
    
    index = pd.to_datetime(daily_log_return.index)
    fig,plt1 = plt.subplots()
    plt1.set_xlabel("Time")
    plt1.plot(index,daily_log_return["Close"], color="blue")
    plt1.set_ylabel("Return",color="blue")
    plt2 = plt1.twinx()
    plt2.plot(index,sp500_removed.iloc[1:,:],color ="red")
    plt2.set_ylabel("Price",color="red")
    plt.show()
    #length = np.size(daily_log_return)
    #normal_random = np.random.normal(mean_return,math.sqrt(variance_return),size = length)
    _,bins,_= plt.hist(daily_log_return, 20, density=1, alpha=0.5)
    fit_line = stats.norm.pdf(bins,mean_return,math.sqrt(variance_return))
    plt.plot(bins,fit_line, color="orange")
    
    

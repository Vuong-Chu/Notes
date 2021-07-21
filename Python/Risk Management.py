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
    daily_log_return = sp500_removed[1:].copy() #When we wanna copy instead of replacing values in the old data
    daily_log_return["Close"] = np.log(sp500_removed.iloc[1:].values/sp500_removed.iloc[:-1].values)
    daily_log_return.rename(columns={"Close":"Return"},inplace=True)
    mean_return = daily_log_return.mean().values[0]
    variance_return = daily_log_return.var().values[0]
    skewness_return = daily_log_return.skew().values[0]
    kurtosis_return = daily_log_return.kurtosis().values[0]
    
    index = pd.to_datetime(daily_log_return.index)
    fig,plt1 = plt.subplots(figsize=(25,10))
    plt1.set_xlabel("Time")
    plt1.plot(index,daily_log_return["Return"], color="blue")
    plt1.set_ylabel("Return",color="blue")
    plt2 = plt1.twinx()
    plt2.plot(index,sp500_removed.iloc[1:,:],color ="red")
    plt2.set_ylabel("Price",color="red")
    plt.show()
    #length = np.size(daily_log_return)
    #normal_random = np.random.normal(mean_return,math.sqrt(variance_return),size = length)
    plt.figure(figsize=(15,10))
    _,bins,_= plt.hist(daily_log_return, 50, density=1, alpha=0.5)
    fit_line = stats.norm.pdf(bins,mean_return,math.sqrt(variance_return))
    plt.plot(bins,fit_line, color="orange")
    plt.show()
    
    autocorrelation_100 = np.zeros((100,1))
    #in Pandas, calculations will match between indexes.
    for i in range(1,101,1):
        autocorrelation_100[i-1],_ = stats.pearsonr(daily_log_return.iloc[i:]["Return"].values, daily_log_return.iloc[:-i]["Return"].values)
    
    plt.figure(figsize=(25,10))
    plt.plot(range(1,101),autocorrelation_100)
    plt.show()
    
    sq_autocorrelation_100 = np.zeros((100,1))
    
    for i in range(1,101,1):
        sq_autocorrelation_100[i-1],_ = stats.pearsonr(daily_log_return.iloc[i:]["Return"].values**2, daily_log_return.iloc[:-i]["Return"].values**2)
    
    plt.figure(figsize=(25,10))
    plt.plot(range(1,101),sq_autocorrelation_100)
    plt.show()
    
    
    sigma_sq = daily_log_return.copy()
    sigma_sq.iloc[0,:] = variance_return
    return_sq = daily_log_return.copy()
    return_sq["Return"] = return_sq["Return"]**2
    sigma_sq.rename(columns={"Return":"Sigma_squared"},inplace=True)
    size = return_sq.shape[0]
    for i in range(1,size):
        sigma_sq.iloc[i,:]["Sigma_squared"] = 0.94*sigma_sq.iloc[i-1,:]["Sigma_squared"] + 0.06*return_sq.iloc[i-1,:]["Return"]
    
    sigma = sigma_sq.copy()
    sigma.rename(columns={"Sigma_squared":"Sigma"},inplace=True)
    sigma["Sigma"] = sigma_sq["Sigma_squared"]**(1/2)
    
    plt.figure(figsize=(25,10))
    plt.plot(index,sigma)
    plt.title("Conditional Standard Deviation")
    plt.show()
    zt = pd.DataFrame(daily_log_return["Return"]/sigma["Sigma"],index = sigma.index, columns={"zt"})
    mean_zt = zt.mean()[0]
    skew_zt = zt.skew()[0]
    kurtosis_zt = zt.kurtosis()[0]
    
    daily_return = sp500_removed.iloc[1:,:].copy()
    daily_return.rename(columns={"Close":"Daily_Return"},inplace=True)
    daily_return["Daily_Return"] = np.log(sp500_removed.iloc[1:].values/sp500_removed.iloc[:-1].values)
    mean_daily = daily_return.mean()[0]
    std_daily = daily_return.std()[0]
    skew_daily = daily_return.skew()[0]
    kurtosis_daily = daily_return.kurtosis()[0]
    
    daily_return = sp500_removed.iloc[1:,:].copy()
    daily_return.rename(columns={"Close":"Daily_Return"},inplace=True)
    daily_return["Daily_Return"] = np.log(sp500_removed.iloc[1:].values/sp500_removed.iloc[:-1].values)
    mean_daily = daily_return.mean()[0]
    std_daily = daily_return.std()[0]
    skew_daily = daily_return.skew()[0]
    kurtosis_daily = daily_return.kurtosis()[0]
    
    day5_return = sp500_removed.iloc[5:,:].copy()
    day5_return.rename(columns={"Close":"5Day_Return"},inplace=True)
    day5_return["5Day_Return"] = np.log(sp500_removed.iloc[5:].values/sp500_removed.iloc[:-5].values)
    mean_day5 = day5_return.mean()[0]
    std_day5 = day5_return.std()[0]
    skew_day5 = day5_return.skew()[0]
    kurtosis_day5 = day5_return.kurtosis()[0]
    
    day10_return = sp500_removed.iloc[10:,:].copy()
    day10_return.rename(columns={"Close":"10Day_Return"},inplace=True)
    day10_return["10Day_Return"] = np.log(sp500_removed.iloc[10:].values/sp500_removed.iloc[:-10].values)
    mean_day10 = day10_return.mean()[0]
    std_day10 = day10_return.std()[0]
    skew_day10 = day10_return.skew()[0]
    kurtosis_day10 = day10_return.kurtosis()[0]
    
    day15_return = sp500_removed.iloc[15:,:].copy()
    day15_return.rename(columns={"Close":"15Day_Return"},inplace=True)
    day15_return["15Day_Return"] = np.log(sp500_removed.iloc[15:].values/sp500_removed.iloc[:-15].values)
    mean_day15 = day15_return.mean()[0]
    std_day15 = day15_return.std()[0]
    skew_day15 = day15_return.skew()[0]
    kurtosis_day15 = day15_return.kurtosis()[0]
    

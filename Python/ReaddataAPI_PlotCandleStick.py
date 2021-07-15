# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:33:23 2021

@author: minhv
"""

import pandas_datareader as pdr
import datetime
import plotly.graph_objs as go
from plotly.offline import plot

end_date = datetime.datetime.now().date()
timechange = datetime.timedelta(days=250)
start_date = end_date - timechange
data = pdr.get_data_yahoo(["AAPL"],start=start_date,end=end_date)


fig = go.Figure(data = [go.Candlestick(x=data.index,
                        open=data.iloc[:,4],
                        high=data.iloc[:,2],
                        low=data.iloc[:,3],
                        close=data.iloc[:,1])])
plot(fig,auto_open=True)

from matplotlib import pyplot as plt
import mpl_finance as mpf
from matplotlib.pylab import date2num
import pandas as pd
import matplotlib as mp
import matplotlib.dates as dates
import datetime
import numpy as np
#%matplotli inline
def main():
    quotes = []
    stock = pd.read_csv('E:/PyCharm/workspace/BS/trade/csv_file/output.csv',parse_dates=[7], encoding="ANSI")

    stock['CP']=stock['CP'].apply(lambda x: x.replace(",","")).astype("float64")#利用lambda去除数据中的逗号，并用astype将object转换为float
    stock['HP']=stock['HP'].apply(lambda x: x.replace(",","")).astype("float64")
    stock['LP']=stock['LP'].apply(lambda x: x.replace(",","")).astype("float64")
    stock['OP']=stock['OP'].apply(lambda x: x.replace(",","")).astype("float64")
    stock['TV']=stock['TV'].apply(lambda x: x.replace(",","")).astype("float64")
    stock['turnover']=stock['turnover'].apply(lambda x: x.replace(",","")).astype("float64")

    stock['date']=pd.to_datetime(stock['date'], format='%Y%m%d')#将date转换为datetime


    stock.set_index(stock['date'], inplace=True)#将转换后的date设置成检索
    # stock["CP"].plot()
    # stock["HP"].plot()
    plt.plot(stock["OP"],label='op')
    plt.plot(stock["HP"], label='hp')
    plt.legend()#图例
    plt.xticks(rotation=30)# 设置日期刻度旋转的角度
    plt.xlabel("datetime")
    plt.show()
if __name__ == '__main__':
    main()
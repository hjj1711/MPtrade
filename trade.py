# import pandas
#import matplotlib
# import mpl_finance
# import matplotlib.pyplot as plt

#matplotlib.style.use('ggplot')
#matplotlib.style.use('dark_background')

# def stockPricePlot(ticker):
# 	# Step 1. Load Data
# 	history = pandas.read_csv('E:/PyCharm/workspace/BS/trade/csv_file/output.csv', parse_dates=True, index_col=7)


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

    #stock.info()
    # stock.set_index(stock['date'], inplace=True)
    # sdate_change_format = str(stock['date'][0:4]) + '-' + str(stock['date'][4:6]) + '-' + str(stock['date'][6:])
    # sdate_num = date2num(datetime.datetime.strptime(sdate_change_format, '%Y-%m-%d'))
    # sdate_plt = sdate_num
    # stock.set_index(sdate_plt, inplace=True)
    #stock['date']=stock['date'].astype("datetime64")

    # stock.set_index("date", inplace=True)
    # stock.index = pd.DatetimeIndex(stock.index)

    stock['date']=pd.to_datetime(stock['date'], format='%Y%m%d')#将date转换为datetime

    #stock['date'] = stock['date'].apply(lambda x: dates.date2num(x) * 1440)

    stock.set_index(stock['date'], inplace=True)#将转换后的date设置成检索
    #print(stock.isnull())
    # print(stock)
    # print(stock.info())
    # print(stock.head())
    # print(stock.columns)

    # stock["CP"].plot(grid=True,)
    # stock["HP"].plot()
    #plt.show()

    # mp.style.use('ggplot')
    # fig, (ax1,ax2)=plt.subplots(1,2,figsize=(12,4))
    # stock.stock["CP"].plot(kind='barh',ax=ax1)
    # ax1.set_xlabel('cp')
    # stock.stock["HP"].plot(kind='barh', ax=ax2)
    # ax2.set_xlabel('cp')
    # fig.tight_layout()

    # for row in range(70):
    #     if row == 0:
    #         sdate = str(stock.loc[row,stock['date']])   # 注意：loc返回数值，iloc返回dataframe
    #         sdate_change_format = sdate[0:4] + '-' + sdate[4:6] + '-' + sdate[6:]
    #         sdate_num = date2num(datetime.datetime.strptime(sdate_change_format, '%Y-%m-%d'))  # 日期需要特定形式，这里进行转换
    #         sdate_plt = sdate_num
    #     else:
    #         sdate_plt = sdate_num + row

        # sopen = stock.loc[row, 'OP']
        # shigh = stock.loc[row, 'HP']
        # slow = stock.loc[row, 'LP']
        # sclose = stock.loc[row, 'CP']
    sdate_plt=stock['date']
    sopen = stock['OP']
    shigh =stock['HP']
    slow = stock['LP']
    sclose = stock['CP']
    datas = (sdate_plt, sopen, shigh, slow, sclose)  # 按照 candlestick_ohlc 要求的数据结构准备数据
    quotes.append(datas)

    fig, ax = plt.subplots(facecolor=(0, 0.3, 0.5), figsize=(12, 8))
    fig.subplots_adjust(bottom=0.1)
    ax.xaxis_date()
    plt.xticks(rotation=45)  # 日期显示的旋转角度
    plt.title('600000')
    plt.xlabel('time')
    plt.ylabel('price')
    mpf.candlestick_ohlc(ax, quotes, width=0.7, colorup='r', colordown='green')  # 上涨为红色K线，下跌为绿色，K线宽度为0.7
    plt.grid(True)
    plt.show()

    # stock = pd.read_csv("E:/PyCharm/workspace/BS/trade/csv_file/output.csv",nrows=28,parse_dates=[7], index_col=7, encoding="ANSI")
    # stock["CP"].plot(grid=True)
    #
    # stock["HP"].plot()
if __name__ == '__main__':
    main()
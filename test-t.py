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

    CP=stock['CP'].apply(lambda x: x.replace(",","")).astype("float64")#利用lambda去除数据中的逗号，并用astype将object转换为float
    HP=stock['HP'].apply(lambda x: x.replace(",","")).astype("float64")
    LP=stock['LP'].apply(lambda x: x.replace(",","")).astype("float64")
    OP=stock['OP'].apply(lambda x: x.replace(",","")).astype("float64")
    TV=stock['TV'].apply(lambda x: x.replace(",","")).astype("float64")
    turnover=stock['turnover'].apply(lambda x: x.replace(",","")).astype("float64")


    stock['date']=pd.to_datetime(stock['date'], format='%Y%m%d')#将date转换为datetime
    stock.set_index(stock['date'], inplace=True)
    date = stock['date'].apply(lambda x: dates.date2num(x) * 1440)

    #stock.set_index(stock['date'], inplace=True)#将转换后的date设置成检索

    for row in range(70):

        sdate = stock.loc[row,date]   # 注意：loc返回数值，iloc返回dataframe

        sopen = stock.loc[row,OP]
        shigh = stock.loc[row,HP]
        slow = stock.loc[row,LP]
        sclose = stock.loc[row,CP]
    datas = (sdate, sopen, shigh, slow, sclose)  # 按照 candlestick_ohlc 要求的数据结构准备数据
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
if __name__ == '__main__':
    main()
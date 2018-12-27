import csv
from datetime import datetime
from matplotlib import pyplot as plt

def get_data(filename,title):
    with open(filename) as f:
        reader=csv.reader(f)
        header_row=next(reader)
        dates,highs,lows=[],[],[]
        #阅读器已将第一行列头数据读取，下面的每一行都为数据
        for row in reader:
            try:
                date=datetime.strptime(row[0],'%Y-%m-%d')
                high=int(row[1])
                low=int(row[3])
            except :
                print(row[0],'missing date')
            else:
                dates.append(date)#日期
                highs.append(high)#最高温
                lows.append(low)#最低温
        
    #键值 列名
    #for index,column_header in enumerate(header_row):
    #    print(index,column_header) 
    #输出指定数据
    #print(highs)
    #print(lows)
    #print(dates)
    
    fig=plt.figure(dpi=128,figsize=(10,6))
    #alpha透明度
    #日期和最高温
    plt.plot(dates,highs,c='red',alpha=0.5)
    #日期和最低温
    plt.plot(dates,lows,c='blue',alpha=0.5)
    #给气温范围着色，此方法接受一个x值两个y值
    plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)
    #设置标题
    plt.title(title,fontsize=24)
    plt.xlabel("",fontsize=16)
    #绘制斜的日期标签
    fig.autofmt_xdate()
    plt.ylabel("Temperatures(F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()


#filename='csvFile/sitka_weather_07-2014.csv'
#title='Daily high temperatures,July 2014'
#filename='csvFile/sitka_weather_2014.csv'
filename='csvFile/death_valley_2014.csv'
title='Daily high and low death valley-2014'
get_data(filename,title)
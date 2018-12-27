import matplotlib.pyplot as plt
from randomwalk import RandomWalk

while True:
    rw=RandomWalk(90000)
    rw.fill_walk()
    #绘制所有的点
    plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,cmap=plt.cm.Blues,s=15,edgecolor='none')
    #绘制起点
    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    #绘制终点
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100,edgecolor='none')
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running=input("Mark another walk?(y/n):")
    if keep_running=="n":
        break


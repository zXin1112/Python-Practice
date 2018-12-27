import matplotlib.pyplot as plt
#折线图
#画图的数据源，若只添加y轴的值则默认y轴的值从0开始
input_values=[1,2,3,4,5]#x轴坐标
squares=[1,4,9,16,25]#y轴坐标
#画图,线的宽度
plt.plot(input_values,squares,linewidth=5)
#添加标题，横纵轴标题
plt.title("square Number",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
#显示
plt.show()
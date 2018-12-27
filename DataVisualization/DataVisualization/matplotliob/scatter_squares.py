import matplotlib.pyplot as plt
#散点图
#设置画面大小，12相当于1200 5.5相当于550 宽1200高550
plt.figure(figsize=(12, 5.5))
#数据源
#x_values=[1,2,3,4,5]
#y_values=[1,4,9,16,25]
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
#s为点的尺寸,c为点的颜色 也可指定rgb
#plt.scatter(x_values,y_values,c='red',s=40)
#颜色映射 c设置为y值列表，cmap使用那个颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=40)
#添加标题，横纵轴标题
plt.title("square Number",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
#设置每个坐标轴的取值范围 X轴 y轴
plt.axis([0,1100,0,1100000])
#保存图片，路径 将空白区域裁减掉
plt.savefig('test.png',bbox_inches='tight')
plt.show()
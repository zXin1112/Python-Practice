#range(value1,value2)从指定的第一个数开始，到第二个数结束，所以不包括第二个数
for value in range(1,5):
    print(value)
#以range为参数创建列表
number=list(range(1,6))
print(number)

#指定自定义的步长，例如range(1,11,2)从1不断加2到11
for value in range(1,11,2):
    print(value)


#将1-10的平方放入队列中
squres=[]
for value in range(1,11):
    squres.append(value**2)
    print(squres)
#99乘法表
num=list(range(1,10))
num.sort(reverse=True)
for value1 in num: 
    string=''
    for value2 in range(value1,10):       
        string+=str(value1)+"*"+str(value2)+"="+str(value1*value2)+" "
    print(string)

#简单的统计计算
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
squres=[value**2 for value in range(1,11)]
print(squres)

#切片 处理列表部分元素
players=['charles','martina','michael','florence','eli']
print(players[0:3])#输出列表0-3
print(players[1:4])#输出列表1-4
print(players[:4])#第一个索引省略则从列表头部开始
print(players[3:])#同理从3到末尾
print(players[-3:])#从倒数第三个到末尾

#列表的复制
#使用此方法是将players的值给players_copy，所以对players或者players_copy进行更改，两者互不影响
players_copy=players[:]
print(players)
print(players_copy)
#这种方式是两个变量指向同一列表，所以对任意一个更改，都会影响
_players=players
players[0]='aaaa'
print(_players)
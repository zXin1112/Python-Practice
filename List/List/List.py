#列表
bicycles=['trek','cannondale','aedline','specialized']
print(bicycles)

#访问列表元素
print(bicycles[0].title())
#当指定索引为-1时，返回列表中最后一个元素
print(bicycles[-1])

#修改、添加和删除元素
#修改
print(bicycles[0])
bicycles[0]='ducati'
print(bicycles[0])
#添加
print(bicycles)
bicycles.append('trek')
print(bicycles)
#插入
bicycles.insert(1,'honda')
print(bicycles)
#删除
del bicycles[1]
print(bicycles)
bicycles_pop=bicycles.pop()#弹出，可弹出任意索引的值，默认最后一个值
print(bicycles_pop)
print(bicycles)
#根据值删除元素
bicycles.remove('aedline')
print(bicycles)
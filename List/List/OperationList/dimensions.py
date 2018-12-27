#元组 很像列表，但不同的是元组使用圆括号，元素不能修改
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#元组不可更改但可重新定义
dimensions=(330,550)
for dimension in dimensions:
    print(dimension)
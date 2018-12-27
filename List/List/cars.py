#排序
cars=['bmw','audi','toyota','subaru']
print(cars)
#永久排序（改变元素位置）
cars.sort()#默认升序
print(cars)
cars.sort(reverse=True)#降序
print(cars)

#临时排序
cars=['bmw','audi','toyota','subaru']
print(sorted(cars))
print(cars)
print(sorted(cars,reverse=True))

#反转
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#长度
print(len(cars))
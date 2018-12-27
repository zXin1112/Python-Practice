cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#检查是否相等时会考虑大小写
print('bmw' == 'bmw')
print('bmw' == 'Bmw')

#检查多个条件
print('bmw' == 'bmw' and 5 > 9)#and 同时成立
print('bmw' == 'bmw' or 5 > 9)#or 有一个成立

#特定值是否在列表中
print('bmw' in cars)

#if-else语句
age = 17
if age > 18:
    print(True)
else:
    print(False)

#if-elif-else
age = 12
if age < 4:
    print('$0')
elif age < 18:
    print('$5')
else:
    print('$10')

age = 12
if age < 4:
    print('$0')
elif age < 18:
    print('$5')
elif age <= 65:
    print("$10")
elif age >= 65:
    print('$5')

#判断列表是否为空
age=[]
if age:
    print(age[0])
else:
    print('null')
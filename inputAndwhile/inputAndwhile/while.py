#while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+=1
#break
while True:
    city = input("tell me something:")
    if city == '.':
        break
    print(city)

#counting
temp = 0
while temp < 10:
    temp+=1
    if temp % 2 == 0:
        continue
    print(temp)

#while循环处理字典
#删除包含特定值的所有列表元素
pets=['dog','cat','dog','cat','goldfish','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
    print(pets)
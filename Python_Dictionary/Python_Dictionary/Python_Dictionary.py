#字典是一系列的键值对
alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#字典-添加
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#字典-修改
alien_0['color']='yellow'
print(alien_0)

#字典-删除
del alien_0['color']
print(alien_0)

#字典-遍历
for key,value in alien_0.items():
    print(key+":"+str(value))

#遍历所有的键
for key in alien_0.keys():
    print(key)

#遍历所有的值
for value in alien_0.values():
    print(value)


#字典列表-在列表中嵌套字典
alines=[]
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

alines.append(alien_0)
alines.append(alien_1)
alines.append(alien_2)

for alien in alines:
    print(alien)

#在字典中存储列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
    }
for topping in pizza['toppings']:
    print(topping)


#字典中存储字典
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    }
for username,user_info in users.items():
    print("username"+username)
    fullname=user_info['first']+" "+user_info['last']
    location=user_info['location']
    print("\tfullname:"+fullname)
    print("\tlocation:"+location)
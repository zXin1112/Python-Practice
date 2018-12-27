#函数
def greet_user():
    print("hello")

greet_user()

#向函数传递信息
def greet_user(username):
    print("hello,"+username)

greet_user("zzz")

#关键字实参 传递函数的实参与形参名称对应，防止混淆
def sayhello(name,sex):
    print("hi,my name is "+name)
    print("my gender is "+sex)
sayhello(name="xx",sex="cc")

#为参数指定默认值
def sayhello(name,sex="male"):
    print("hi,my name is "+name)
    print("my gender is "+sex)
sayhello(name="zz")
sayhello("zz")

#返回值
def get_fullname(first,last,middle=""):
    fullname=first+" "+middle+" "+last if middle else first+" "+last#python的三元表达式 为真时的结果 if 判断条件 else 为假时的结果
    return fullname.title()
musician=get_fullname('jimi','hendrix')
print(musician)
musician=get_fullname('jimi','hendrix',"lee")
print(musician)

#返回一个字典
def build_person(first,last):
    person={'first':first,'last':last}
    return person
musician=build_person('jimi','hendrix')
print(musician)

#传递列表
def geet_username(names):
    for name in names:
        print(name.title())
geet_username(['hannah','ty','margot'])

#在函数中修改列表
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()

        print(current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#禁止函数修改列表 在上面的例子中，传递实参时使用切片创建列表副本，可实现不改变原列表
unprinted_designs=['iphone case','robot pendant','dodecahedron']
print_models(unprinted_designs[:],completed_models)
print(unprinted_designs)

#传递任意数量的实参
def make_pizza(*toopings):
    print(toopings)
make_pizza('pepperoni')
make_pizza('green peppers','extra cheese')

#传递任意数量的关键字实参
def build_person(first,last,**user_Info):
    porfile={}
    porfile['first_name']=first
    porfile['last_name']=last
    for key,value in user_Info.items():
        porfile[key]=value
    return porfile

user_info=build_person('albert','einstein',location='princeton',field='physics')
print(user_info)

#导入模块 
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','extra cheese')

#导入模块中指定函数，多个函数用逗号分隔,使用*可将所有函数导入
from pizza import make_pizza,add
make_pizza(12,'mushrooms','extra cheese')
print(str(add(2,5)))

#用as为导入模块，函数指定别名
import pizza as p
from pizza import add as a

print(str(p.add(3,5)))
print(str(a(2,6)))
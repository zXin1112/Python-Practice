import dog
from cat import cat

#访问属性
mydog=dog.dog('willie',6)
print("My dog's name is "+mydog.name.title()+".")
print("My dog is "+str(mydog.age)+" years old")
#调用方法
mydog.sit()
#更改属性的值
mydog.age=20
print("My dog is "+str(mydog.age)+" years old")

#继承，cat继承dog 子类继承父类所有属性方法，子类也可以添加新的属性方法
mycat=cat('paris',2)
mycat.rool_over()
mycat.printsex()#输出添加的方法
mycat.sit()#调用重写父类的方法
print(str(mycat.t.t))#实例用作属性

#Python标准库 以模块collections中OrderedDict类为例
from collections import OrderedDict

favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarsh']='c'
favorite_languages['puil']='python'

for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title())

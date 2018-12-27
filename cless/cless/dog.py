class dog():
    """模拟小狗类"""
    def __init__(self, name,age):#生成实例时自动调用，self存放属性方法
       self.name = name
       self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def rool_over(self):
        print(self.name.title() + " rolled over!")



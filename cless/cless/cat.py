from dog import dog
class cat(dog):
    """cat继承dog"""

    def __init__(self, name, age):
        """初始化父类的属性"""
        super().__init__(name, age)
        self.sex="male"#添加一个属性
        self.t=test()
    def printsex(self):
        print(self.sex)
    def sit(self):
        #super().sit()父类的方法
        print("the cat "+self.name.title() + " is now sitting.")
class test():
    """实例用作属性"""
    def __init__(self, t=10):
        self.t=t

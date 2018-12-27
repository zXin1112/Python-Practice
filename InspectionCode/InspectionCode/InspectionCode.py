# 测试代码 类和函数的测试同理
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):#继承此类
    def test_first_last_name(self):
        formatted=get_formatted_name('janis','joplin')
        self.assertEqual(formatted,'Janis Joplin')
    def test_first_middle_last_name(self):
        formatted=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted,'Wolfgang Amadeus Mozart')#断言方法 测试两者是否相等

unittest.main()#测试所有test开头的函数

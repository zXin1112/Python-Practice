#用户输入 input() 程序暂停等待用户输入的文本
message=input('tell me something,and i will repeat it back to you:')
print(message)

#使用int（）将用户输入的字符转为数字
age=input("how old are you?")
age=int(age)
if age>=18:
    print(True)
else:
    print(False)

name="ada lovelace"
#首字母大写
print(name.title())
#所有字母大写
print(name.upper())
#所有字母小写
print(name.lower())

#拼接字符串
first="ada"
last_name="lovelace"
full_name=first+" "+last_name
print(full_name)
print("hello, "+full_name.title()+"!")
message="hello, "+full_name.title()+"!"
print(message)

#制表符
print("\tPython")
#换行符
print("Languages:\nPython\nC\nJavaScript")

#删除空白
favorite_language="python "
print(favorite_language)
print(favorite_language.rstrip())#删除右边的空白，同理还存在删除左边的空白lstrip()



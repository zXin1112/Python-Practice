#文件
#读取整个个文件 with会在合适的时候自动将打开的文件关闭 在win系统中使用/由于Python认为是转义符所以可能失败，故在引号之前加r保证字符原义输出
filename='pi_digits.txt'
#with open(filename) as file_object:
#    contents=(file_object.read()).rstrip()
#    print(contents)

##逐行读取
#with open(filename) as file_object:
#    for line in file_object:
#        print(line.rstrip())

#将文件内容存到列表中
with open(filename) as file_object:
    lines=file_object.readlines()
print(lines)
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
#显示前十位
print(pi_string[:10]+"……")

#写入文件 其中，open的参数 w写入、r读取、a附加、r+读写，默认只读
filename='programming.txt'
#写入
with open(filename,'w') as file_wirite:
    file_wirite.write("hello world!\n")
    file_wirite.write("hello world!\n")
#读取
with open(filename) as file_read:
   print( file_read.read())

#附加到文件 写入后原内容保持不变
with open(filename,'a') as file_attach:
    file_attach.write("aaaaa\n")
    file_attach.write("bbbbb\n")
with open(filename) as file_read:
   print( file_read.read())
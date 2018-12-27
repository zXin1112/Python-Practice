#异常
#try方可能存在异常的代码，except放代码异常时执行的代码，else放在try中的代码执行成功后执行的代码
#first = int(input("the first_number:"))
#second = int(input("the second_number:"))
#try:
#    answer = first / second
#except :
#    print("error")
#else:
#    print(answer)

#统计文件单词数目 split()创建单词列表
def count_words(filename):
    try:
        with open(filename,'r',encoding='UTF-8') as file_re:#指定编码格式 默认gbk
            words = file_re.read()
    except :
        print('erroe')
    else:
        print("the file " + filename + " has about " + str(len(words.split())) + " worlds")


filenames = ['219-0.txt','98-0.txt','pg7296.txt']
for filename in filenames:
    count_words(filename)


#存储数据
import json#导入模块
numbers = [1,2,3,4,5,6,7,8,9]
filename = 'numbers.json'
with open(filename,'w') as f_obj:#打开文件
    json.dump(numbers,f_obj)#写入指定文件
with open(filename,'r') as f_r:
    number = json.load(f_r)#读取数据
print(number)


#接受用户输入的用户名
filename = 'user_name.json' 
username=[]
try:
    with open(filename) as file_r:
        username=json.load(file_r)
except :
    pass#先读取文件中的数据

while True:
    try:
        with open(filename,'w') as file_w:
            username.append(input("what's your name?"))#追加
            if(username[-1] == 'q'): #按q时退出输入
                username.pop()
                json.dump(username,file_w)
                break
            
    except :
        print("error")
    else:
        print("OK")

#输出输入的用户，包括之前的用户
try:
    with open(filename) as file_r_:
        usernames=json.load(file_r_)
except :
    print('error')
else:
    for uname in usernames:
        print(uname)
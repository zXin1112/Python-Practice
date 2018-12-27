import requests
import pygal
from pygal.style import LightenStyle as LS , LightColorizedStyle as LCS

url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
print("status_code:",r.status_code)#请求的状态码
response_dict=r.json()#将请求的内容转成Python字典
print(response_dict.keys())#请求到的键
print("Total repostitories:",response_dict["total_count"])#共有多少个仓库 

repo_dicts=response_dict['items']#仓库信息
print("Repositories returned:",len(repo_dicts))#有多少个仓库信息

#repo_dict=repo_dicts[0]#获取第一个仓库
#print("\nKeys:",len(repo_dict))#第一个仓库有多少信息
#for key in sorted(repo_dict.keys()):
#    print(key)#遍历打印键
for repo_dict in repo_dicts:    #打印所有仓库信息
    print("\nSelected information about first repository:")
    print('Name:',repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Created:',repo_dict['created_at'])
    print('updated:',repo_dict['updated_at'])
    print('Description:',repo_dict['description'])

names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict={
        "value":repo_dict['stargazers_count'],
        "label":str(repo_dict['description']),#此处有特殊字符，易引发错误，故将其强转string
        'xlink':repo_dict['html_url']#添加单击链接
        }
    plot_dicts.append(plot_dict)#设置自定义工具信息
#设置自定义工具信息
#plot_dicts = [
#{'value':16101, 'label': 'Description of httpie.'},
#{'value':15028, 'label': 'Description of django.'},
#{'value':14798, 'label': 'Description of flask.'}
#]

my_style=LS('#333366',base_style=LCS)

my_config=pygal.Config()#设置类对象
my_config.x_label_rotation=45#标签倾斜
my_config.show_legend=False#不显示图例
my_config.title_font_size=24#标题大小
my_config.label_font_size=14#标签大小
my_config.major_label_font_size=18
my_config.truncate_label=15#标签名缩短至15个字符
my_config.show_y_guides=False#隐藏水平线
my_config.width=1000#设定大小

#chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)#添加样式 标签绕x轴旋转45 隐藏图例
chart=pygal.Bar(my_config,style=my_style)#添加设置  添加样式
chart.title="M0st-Starred Python Projects on Github"
chart.x_labels=names

chart.add('',plot_dicts)#添加自定义工具信息
chart.render_to_file('Python_repos.svg')

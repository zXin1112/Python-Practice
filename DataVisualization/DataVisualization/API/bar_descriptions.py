import pygal
from pygal.style import LightenStyle as LS , LightColorizedStyle as LCS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django','flask']
plot_dicts = [
{'value':16101, 'label': 'Description of httpie.'},
{'value':15028, 'label': 'Description of django.'},
{'value':14798, 'label': 'Description of flask.'}
]
#添加自定义工具提示
chart.add('',plot_dicts)#接受一个字符串一个列表

chart.render_to_file('bar_descriptions.svg')
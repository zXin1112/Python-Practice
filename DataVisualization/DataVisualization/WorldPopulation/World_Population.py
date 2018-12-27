import json
from countries import get_country_code
import pygal.maps.world

def get_world_map(year):
    """"获取地图"""
    filename='WorldPopulation/population-data.json'
    with open(filename) as f:#读取文件
        pop_data=json.load(f)
    cc_populations={}#存放两个字母的国别码和对应的人数
    #获取指定年份所有国家的人口数
    for pop_dict in pop_data:
        if pop_dict["Year_"+year.strip()]:
            country_name=pop_dict['Country']#城市名
            population=int(float(pop_dict["Year_"+year.strip()]))#有些小数无法转换为int 故这样处理
            code=get_country_code(country_name)#根据城市名获取两个字母的国别名
            if code:
                cc_populations[code]=population
            #print(country_name+':'+str(population))
    print(cc_populations)
   
    #以人口数量分类
    cc_pops_1,cc_pops_2,cc_pops_3={},{},{}
    for cc,pop in cc_populations.items():
        if pop<10000000:
            cc_pops_1[cc]=pop
        elif pop<1000000000:
            cc_pops_2[cc]=pop
        else:
            cc_pops_3[cc]=pop
    print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

    worldmap_chart=pygal.maps.world.World()#世界地图
    worldmap_chart.title='World Population in {0} ,by Country'.format(year)  #标题
    #添加三种类别的数据
    worldmap_chart.add('0-10m',cc_pops_1)
    worldmap_chart.add('10m-1bn', cc_pops_2)
    worldmap_chart.add('>1bn', cc_pops_3)
    #生成文件和名
    worldmap_chart.render_to_file( worldmap_chart.title+'.svg')


try:
    Year=int(input('Year(1960<Year<2017):'))
except :
    print('Error')
else:
    if Year<2017 and Year>1960:
        get_world_map(str(Year))



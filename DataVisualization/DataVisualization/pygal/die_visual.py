from die import Die
import pygal
#直方图

def get_svg(die1,die2,filename):
    
    #获取数据
    results = []
    for roll_num in range(1000):
        result = die1.roll() + die2.roll()
        results.append(result)

    #分析数据
    frequencies = []
    max_result = die1.num_sides + die2.num_sides
    for value in range(2,max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    #数据可视化
    hist = pygal.Bar()
    hist.title = "Results of rolling one D6 1000 times"
    hist.x_labels = [i for i in range(2,max_result+1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add('D{0}+D{1}'.format(die1.num_sides,die2.num_sides),frequencies)
    hist.render_to_file(filename.strip()+'.svg')


##扔两个相同面数骰子得到的数据
#die1 = Die()
#die2 = Die()
#filename=input('FileName:')
#get_svg(die1,die2,filename)

#扔两个不同面数骰子得到的数据
die1 = Die()
die2 = Die(10)
filename=input('FileName:')
get_svg(die1,die2,filename)

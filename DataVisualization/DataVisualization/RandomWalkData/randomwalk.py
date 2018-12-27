from random import choice

class RandomWalk():
    """生成随机漫步数据"""
    def __init__(self, num_points=5000):
       self.num_points=num_points
       #初始位置
       self.x_values=[0]
       self.y_values=[0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values)<self.num_points:
            #生成xy轴坐标
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance
            #不能原地踏步
            if x_step==0 and y_step==0:
                continue
            #去坐标列表的最后一个加上要移动的值
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            #添加到坐标集合中
            self.x_values.append(next_x)
            self.y_values.append(next_y)
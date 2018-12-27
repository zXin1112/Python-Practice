class Setting():
    """设置类，游戏中的设置参数"""
    def __init__(self):
        #窗口大小
        self.screen_width = 1200
        self.screen_height = 800
        #窗口背景色
        self.screen_color = (230,230,230)
         #子弹颜色
        self.bullet_color = 60,60,60
        #飞船移动速度
        self.ship_speed_factor = 1.5
         #子弹移动速度
        self.bullet_speed_factor = 2
        #外星人向左右移动速度
        self.alien_speed_factor = 1
         #外星人向下移动速度
        self.fleet_drop_speed = 10
        #1右移 -1左移
        self.fleet_direction = 1

        #子弹宽高
        self.bullet_with = 10
        self.bullet_height = 15
      
        #子弹数量
        self.bullet_allowed = 3
        #飞机数量
        self.ship_limit = 3

        #加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale=1.5

        #外星人分数
        self.alien_points=5000

    def initialize_dynamic_settings(self):
        """初始化随游戏的进行而变化的设置"""
        self.ship_speed_factor = 1.5#飞船移动速度
        self.bullet_speed_factor = 3#子弹移动速度
        self.alien_speed_factor = 1#飞船移动速度

        #外星人左右移动的方向
        self.fleet_direction = 1
    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale



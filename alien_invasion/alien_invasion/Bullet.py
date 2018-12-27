import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """飞船发射的子弹"""
    def __init__(self,ai_settings,screen,ship):
       super().__init__()#继承父类
       self.screen=screen#窗口对象
       self.rect=pygame.Rect(0,0,ai_settings.bullet_with,ai_settings.bullet_height)#创建一个矩形，位置0,0
       self.rect.centerx=ship.rect.centerx#飞船的横坐标
       self.rect.top=ship.rect.top#飞船顶部
       self.y=float(self.rect.y)#y轴位置
       self.color=ai_settings.bullet_color#子弹颜色
       self.speed_factor=ai_settings.bullet_speed_factor#子弹速度

    def update(self):
        """向上移动子弹"""
        self.y-=self.speed_factor#由于原点在左上角（0,0）右下角为（窗口宽度，高度）子弹初始位置的y轴为最大值，只能递减接近原点
        self.rect.y=self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)

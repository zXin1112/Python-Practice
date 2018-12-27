import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """飞船相关"""
    def __init__(self,screen,ai_settings):
        super().__init__()
        self.screen = screen#窗口对象
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')#加载图像
        self.rect = self.image.get_rect()#获取飞船图片的rect对象
        self.screen_rect = self. screen.get_rect()#获取窗口的rect对象

        #将飞船放于屏幕底部中央 设定位置
        self.rect.centerx = self.screen_rect.centerx#飞船图片元素居中
        self.rect.bottom = self.screen_rect.bottom#在屏幕底部

        #飞船是否移动
        self.moving_right = False
        self.moving_left = False

        #飞船移动速度
        self.center = self.ai_settings.ship_speed_factor

    def update(self):
        """更新飞船位置"""
        #if self.moving_right and self.rect.centerx < self.screen_rect.width:
        #    self.moving_right+=1
        #当飞船位置靠近最左或最右时，不再移动
        self.rect.centerx = self.rect.centerx + self.center + 1 if self.moving_right and self.rect.centerx < self.screen_rect.width else self.rect.centerx           
        self.rect.centerx = self.rect.centerx - self.center if self.moving_left and self.rect.centerx > 0 else  self.rect.centerx

    def blitem(self):
        """绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx



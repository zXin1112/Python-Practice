import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """外星人"""
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen#窗口对象
        self.ai_settings=ai_settings#设置参数
        self.image=pygame.image.load('images/alien.bmp')#加载图像
        self.rect=self.image.get_rect()#获取外星人的rect对象
        #位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #外星人的精确位置
        self.x=float(self.rect.x)

    def blitme(self): 
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True


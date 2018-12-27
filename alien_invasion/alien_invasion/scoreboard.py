#coding=utf-8
from pygame.sprite import Group
from ship import Ship
import pygame.font
class Scoreboard():
    """得分信息"""
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen#显示窗口对象
        self.screen_rect = screen.get_rect()#显示窗口的rect对象
        self.ai_settings = ai_settings
        self.stats = stats
        #设置字体颜色
        self.txt_color = (30,30,30)
        self.font = pygame.font.SysFont("arial",48)

        self.prep_score()#分数
        self.prep_high_score()#最高分
        self.prep_level()#等级
        self.prep_ship()

    def prep_score(self):
        """将得分渲染成一幅图像"""
      
        rounded_score = int(round(self.stats.score,-1))#将值园整到最近的10 的整数倍

        score_str = "Current score: {:,}".format(rounded_score)#其中的：，为千分位分隔符
        #score_str=str(self.stats.score)#将得分转换为字符串
        self.score_image = self.font.render(score_str,True,self.txt_color,self.ai_settings.screen_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分和最高分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转换为渲染图像"""
        #获取最高分
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "Highest score: {:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str,True,self.txt_color,self.ai_settings.screen_color)
        #将最高分放到屏幕上方的中间
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级渲染成图像"""
        self.level_image = self.font.render("grade: " + str(self.stats.level),True,self.txt_color,self.ai_settings.screen_color)
        #将等级放到得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        """还剩下多少飞船"""
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.screen,self.ai_settings)
            ship.rect.centerx=self.screen_rect.centerx-ship.rect.width+ship_number*ship.rect.width#在最高分的后面
            ship.rect.y=self.score_rect.height
            self.ships.add(ship)
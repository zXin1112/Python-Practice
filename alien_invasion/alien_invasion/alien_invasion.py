#coding=utf-8

import sys
import pygame
from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from Alien import Alien
from GameStats import GameStats
from Button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()#模块初始化
    ai_settings = Setting()#设置属性
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#窗口尺寸 此处创建了一个屏幕对象
    ship = Ship(screen,ai_settings)#飞船
    bullets = Group()#创建子弹编组
    aliens = Group()
    alien = Alien(ai_settings,screen)
    pygame.display.set_caption("Alien Invasion")#窗口标题
    gf.create_fleet(ai_settings,screen,ship,aliens)#游戏初始化时创建一组外星人
    stats = GameStats(ai_settings)#统计信息
    play_Button = Button(ai_settings,screen,"play")#按键
    sb=Scoreboard(ai_settings,screen,stats)

    #主循环
    while True:
        #监视键盘鼠标事件
        gf.check_events(ai_settings,aliens,screen,ship,bullets,stats,play_Button,sb)
        if stats.game_action:
            #更新飞船位置
            ship.update()
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)
            #刷新子弹
            gf.update_bullet(ai_settings,screen,ship,stats,aliens,bullets,sb)   
            #更新窗口动画
        gf.update_screen(ai_settings,screen,ship,stats,aliens,bullets,play_Button,sb)
         
run_game()
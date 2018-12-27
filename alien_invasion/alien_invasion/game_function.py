#coding=utf-8
import sys
import pygame
from Bullet import Bullet
from Alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats,play_Button,aliens,sb):
    """按键响应"""
     #按下的是方向键右
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
     #按下的是方向键左
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    #按下的是空格
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
     #按下q
    elif event.key == pygame.K_q:
        sys.exit()#退出游戏
        #按下p
    elif event.key == pygame.K_p:
        start_game(ai_settings,screen,stats,play_Button,ship,aliens,bullets,sb)
    
def check_play_button(ai_settings,screen,stats,play_Button,ship,aliens,bullets,sb,mouse_x,mouse_y):
    """鼠标点击play按钮时的相应"""
    if play_Button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_action:
       start_game(ai_settings,screen,stats,play_Button,ship,aliens,bullets,sb)

def start_game(ai_settings,screen,stats,play_Button,ship,aliens,bullets,sb):
    """开始游戏"""
     #改变游戏是否开开始的标识为true
    stats.game_action = True
    #重置游戏
    stats.reset_stats()
    #清空外星人和子弹
    aliens.empty()
    bullets.empty()
    #创建一组外星人
    create_fleet(ai_settings,screen,ship,aliens)
    #创建飞船
    ship.center_ship()
    #隐藏光标
    pygame.mouse.set_visible(False)
    #重置速度
    ai_settings.initialize_dynamic_settings()
    #重新设置计分
    sb.prep_level()
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_ship()#显示剩余飞机数量

def fire_bullet(ai_settings,screen,ship,bullets):
    """发射子弹"""
    if len(bullets) < ai_settings.bullet_allowed:#如果子弹数量没有超过限制
        new_bullet = Bullet(ai_settings,screen,ship)#创建一个新子弹
        bullets.add(new_bullet)#添加到
def check_keyup_events(event,ship):
    """按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,aliens,screen,ship,bullets,stats,play_Button,sb):
    """按键响应事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#点击窗口关闭按钮
            sys.exit()#退出游戏
             #检测键盘有按键按下
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets,stats,play_Button,aliens,sb)               
            #检测键盘是否有按键松开
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            #检测是否有鼠标按下
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #获取鼠标点击的位置
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_Button,ship,aliens,bullets,sb,mouse_x,mouse_y)

def update_screen(ai_settings,screen,ship,stats,aliens,bullets,play_Button,sb):
    """更新动画"""
   
    screen.fill(ai_settings.screen_color)#为屏幕填充颜色,RGB
    
    #根据子弹的大小位置等信息绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    #绘制飞船
    ship.blitem()
    #自动根据编组内每个成员的rect绘制
    aliens.draw(screen)
    if not stats.game_action:
        play_Button.draw_button()
        #刷新分数
    sb.show_score()
    #让最近绘制的屏幕可见
    pygame.display.flip()#不断擦去旧屏幕，显示新屏幕，不断刷新，形成动画
def update_bullet(ai_settings,screen,ship,stats,aliens,bullets,sb):
    """刷新子弹"""
     #自动对编组中的每一个成员执行update
    bullets.update()
   
    #对消失的子弹进行删除
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,ship,stats,aliens,bullets,sb)

def check_bullet_alien_collisions(ai_settings,screen,ship,stats,aliens,bullets,sb):
    """外星人与子弹发生碰撞"""
     #检查外星人与子弹是否产生碰撞
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)#后面两个布尔值的意思是若发生碰撞则两个元素都删除，
    #若改为false，true则发生碰撞时子弹不消失，外星人消失
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats,sb)

    if len(aliens) == 0:#如果外星人全部消失则重新创建一组外星人
        bullets.empty()#清除子弹
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)
        stats.level+=1#消灭一组外星人 等级加一
        sb.prep_level()#刷新等级
        ai_settings.bullet_with+=0.5
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """更新外星人"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #如果外星人与飞船相撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
    #到屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """外星人与飞船相撞"""
    
    if stats.ships_left > 1:
        stats.ships_left-=1#飞船数减一
        aliens.empty()#外星人重置
        bullets.empty()#子弹重置
        create_fleet(ai_settings,screen,ship,aliens)#创建新的外星人
        ship.center_ship()#重置飞船位置
        stats.game_action = True
        sleep(0.1)#暂停0.1s
        sb.prep_ship()#更新当前飞机图标
    else :
        stats.game_action = False
        pygame.mouse.set_visible(True)

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行外星人数"""
    available_space_x = ai_settings.screen_width - (3 * alien_width)#减去一个外星人的位置
    number_aliens_x = int(available_space_x / (2 * alien_width))#能放多少个外星人
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,number_row):
    """创建一个外星人，并将它放到分组里"""
    alien = Alien(ai_settings,screen)#创建一个外星人
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number#位置，每个外星人之间间隔一个外星人的距离
    alien.rect.x = alien.x#设置位置，外星人的位置由rect中的值决定
    alien.rect.y =3* alien.rect.height + 2 * alien.rect.height * number_row
    aliens.add(alien)#添加到编组中
def get_number_rows(ai_settings,ship_height,alien_height):
    """计算可容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - 4* alien_height - ship_height
    #窗口高度减去外星人与最上面边距之间的距离，外星人与飞船之间的距离（外星人高度的三倍），飞船的高度
    number_rows = available_space_y / (2 * alien_height)#减后的距离除以外星人所占的高度（每行外星人之间有一行外星人高度的距离）
    return number_rows

def create_fleet(ai_settings,screen,ship,aliens):
    """创建一组外星人"""
    alien = Alien(ai_settings,screen)#生成外星人单个实例
    alien_width = alien.rect.width#外星人宽
    number_aliens_x = get_number_aliens_x(ai_settings,alien_width)#一行创建多少个外星人
    number_rows = int(get_number_rows(ai_settings,ship.rect.height,alien.rect.height))#创建多少行外星人

    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):#从0开始计数
            create_alien(ai_settings,screen,aliens,alien_number,number_row)#创建外星人
def check_fleet_edges(ai_settings,aliens):
    """外星人到达屏幕边缘做出的反应"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    """外星人向下移动，并改变移动方向"""
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed#向下移动
    ai_settings.fleet_direction *= -1#改变方向
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()#获取屏幕rect对象
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:#当外星人的底部大于或等于窗口的底部时，说明外星人撞到屏幕底部
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
            break

def check_high_score(stats,sb):
    """检查分数，获取最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
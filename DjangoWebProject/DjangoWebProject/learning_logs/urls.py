# -*- coding: utf-8 -*-
"""
定义learning_logs的URL模式
"""
from django.conf.urls import url

from . import views

urlpatterns=[
    #主页
    url(r'^$',views.index,name='index'),#第一个参数为正则表达式 匹配网址确定输入的网址指向的页面，第二个参数为调用指定视图 第三个参数为这个URL模式的名字
    #所有主题
    url(r'^topics/$',views.topics,name='topics'),
         #添加主题详细页
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #添加新主题
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    #添加主题对应的内容
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    #修改主题内容
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
    
]
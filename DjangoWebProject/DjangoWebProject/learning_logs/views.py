# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic,Entry
from  .forms import TopicForm,EntryForm


# Create your views here.
def index(request):
    """首页"""
    title1='记录你的学习内容'
    zhuce='注册'
    context1=' 一个用户以制作您自己的学习日志，并列出您正在学习的主题。'
    context2='每当您学习有关某个主题的新内容时，请输入一个条目，总结您所学到的内容。'
    context={
        'title1':title1,
             'zhuce':zhuce,
             'context1':context1,
             'context2':context2,
             }
    return render(request,'learning_logs/index.html',context)
@login_required#检查是否登录
def topics(request):
    """显示所有主题"""
    #topics=Topic.objects.order_by('date_added')#向数据库查询，按添加时间排序，将结果给topics
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')#查询当前登录的user的主题
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)#返回request对象和模板路径，还有上下文字典context

@login_required#检查是否登录
def topic(request,topic_id):##topic_id为获取的参数
    """显示主题中详细信息"""
    topic=Topic.objects.get(id=topic_id)
    if topic.owner!=request.user:
        raise  Http404
    entries=topic.entry_set.order_by("-date_added")
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required#检查是否登录
def new_topic(request):
    """用户添加新主题"""
    if request.method!='POST':#判断提交类型
        form=TopicForm()#不是post提交则返回空表单
    else:
        form=TopicForm(request.POST)#利用提交的数据创建对象
        if form.is_valid():#若数据可用
            new_topic=form.save(commit=False)#保存
            new_topic.owner=request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))#利用reverse获取URL链接 HttpResponseRedirect重定向到此链接
    context={'form':form}#返回空表单
    return render(request,'learning_logs/new_topic.html',context)#返回响应内容,跳转指定页面

@login_required#检查是否登录
def new_entry(request,topic_id):
    """用户添加主题对应的内容"""
    topic=Topic.objects.get(id=topic_id)

    if request.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)#保存不提交
            new_entry.topic=topic#添加主题对象
            new_entry.save()#保存
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context={'form':form,'topic':topic}
    return render(request,'learning_logs/new_entry.html',context)

@login_required#检查是否登录
def edit_entry(request,entry_id):
    """修改主题内容"""
    entry=Entry.objects.get(id=entry_id)#获取要修改的内容

    if request.method!='POST':
        form=EntryForm(instance=entry)#填充实例
    else:
        form=EntryForm(instance=entry,data=request.POST)#填充实例和要数据
        if form.is_valid():
            form.save()#保存
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[entry.topic.id]))
    context={'form':form,'entry':entry,'topic':entry.topic}
    return render(request,'learning_logs/edit_entry.html',context)

            

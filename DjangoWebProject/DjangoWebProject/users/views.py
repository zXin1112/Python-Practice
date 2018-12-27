from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method!='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()#保存注册的信息
            authenticate_user=authenticate(username=new_user.username,password=request.POST['password1'])#传递用户信息
            login(request,authenticate_user)#自动登录
            return HttpResponseRedirect(reverse('learning_logs:index'))#跳转主页
    context={'form':form,'title1':'注册'}
    return render(request,'users/register.html',context)
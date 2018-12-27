from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(max_length=200)#创建属性 文字
    date_added=models.DateTimeField(auto_now_add=True)#时间
    owner=models.ForeignKey(User)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic=models.ForeignKey(Topic)#下拉框
    text=models.TextField()#多行文本框
    date_added=models.DateTimeField(auto_now_add=True)#时间
    class Meta:#Django模型类的Meta是一个内部类，它用于定义一些Django模型类的行为特性
        verbose_name_plural='entries'#指定复数形式

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50]+'....'
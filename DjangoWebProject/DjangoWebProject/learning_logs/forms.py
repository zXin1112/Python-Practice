from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text']#此处的标签应与model指向的实体类对应
        labels={'text':''}#设置字段text的标签内容

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}#定义小部件

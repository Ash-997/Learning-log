from django import forms
from .models import Topic,Entry,User

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {"text":""}

class Entryform(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}


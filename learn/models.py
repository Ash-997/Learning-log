from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='topics')

    def __str__(self):
        return self.text
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='entries')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
     verbose_name_plural = 'entries'

    def _str_(self):

        return self.text[:50]+"..."

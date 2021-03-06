from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    path("", views.index, name="index"),
    path("ash", views.vccd, name="hhh"),
    path("topics", views.topics, name='topics'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic1'),
    path('new_topic', views.new_topic, name="new_topic"),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^deltopic/(?P<del_id>\d+)/$', views.del_top, name='deltopic'),
    url(r'^delent/(?P<delent_id>\d+)/(?P<topi_id>\d+)$', views.delent, name='del_ent'),
    #path('deltopic', views.del_top, name='deltopic'),
    # path("god",views.god,name = 'god')
]

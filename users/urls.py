from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login
from django.contrib.auth.views import auth_login

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout1, name='logout12'),
    path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^login/$', login, {'templates/login.html'}, name='login')
    path('register/', views.register, name='register')
]

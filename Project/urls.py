from django.contrib import admin
from django.urls import path, include
from MyApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",include('MyApp.urls')),
    path('home',home,name='home'),
    path('',home,name='home'),
    path('register',register,name='register'),
    path('success',success,name='success'),
    path('index',task,name='index'),
    path('pay',pay,name='pay'),
    path('form',form,name='form'),
    path('main',main,name='main'),
    path('add',add,name='add'),
    path('added',added,name='added'),
    path('show',show,name='show'),

]

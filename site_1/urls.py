from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    #127.0.0.1:8000/admin/ 과 같은 의미
    path('admin/', admin.site.urls),
    #127.0.0.1:8000/
    # path('', views.index), #views라는 파이썬 파일 안에 있는 index라는 함수를 연결해주고 싶다
    #127.0.0.1:8000/hello/
    path('hello/',views.hello, name='hello_main'),

    path('lotto/',views.index, name='index'),

    path('lotto/new/', views.post, name='new_lotto'),

    path('lotto/<int:lottokey>/detail/', views.detail, name='detail'),
]

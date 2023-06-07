from django.urls import path
from . import views




import os
urlpatterns = [
    path('test', views.test, name='test'),
    path('rsp', views.rsp, name='rsp'),
    path('test3', views.test3, name='test3'),
    path('test2', views.test2, name='test2'),
    path('middle', views.middle, name='middle'),
    path('game', views.game, name='game'),
    path('ib', views.ib, name='ib'),
    path('alice', views.alice, name='alice'),
    path('ow', views.ow, name='ow'),
    path('sling', views.sling, name='sling'),
    path('dino', views.dino, name='dino'),
    path('index', views.index, name='index'),


    path('execute_function/', views.execute_function, name='execute_function'),
    path('execute_function1/', views.execute_function1, name='execute_function1'),
    path('execute_function2/', views.execute_function2, name='execute_function2'),
    path('execute_function3/', views.execute_function3, name='execute_function3'),

]
from django.urls import path
from . import views # . --> this directory itself

urlpatterns = [
    path('home',views.home,name='Home'),
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('cam',views.camera,name='camera'),
    path('video',views.video,name='video'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('user',views.user,name='user'),
]


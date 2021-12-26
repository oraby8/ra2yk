from django.urls import path

from . import views




urlpatterns = [
    path('', views.index, name='index'),
     path('questions/<int:pk>/',views.questions,name='questions'),
     path('answer/<int:pk>/',views.answer,name='answer'),
     path('templates/',views.templates,name='templates')


     
    
]

#path('questions/<int:i>/answer/<int:pk>/',views.answer,name='answer')
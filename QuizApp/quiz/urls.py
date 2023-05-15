from . import views
from django.urls import path

urlpatterns = [
    path('',views.login,name='Quizlogin'),
    path('home/',views.index,name='Quizindex'),
    path('web/',views.web,name='Quizweb'),
    path('js/',views.js,name='Quizjs'),
]

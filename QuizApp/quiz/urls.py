from . import views
from django.urls import path

urlpatterns = [
    path('https://sensational-melomakarona-c4208d.netlify.app/',views.login,name='Quizlogin'),
    path('https://sensational-melomakarona-c4208d.netlify.app/home/',views.index,name='Quizindex'),
    path('https://sensational-melomakarona-c4208d.netlify.app/web/',views.web,name='Quizweb'),
    path('https://sensational-melomakarona-c4208d.netlify.app/js/',views.js,name='Quizjs'),
]

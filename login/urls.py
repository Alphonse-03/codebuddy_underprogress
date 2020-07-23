from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('',views.intro,name="intro"),
    path('register',views.register,name="register"),
    path('listoc',views.listoc,name="listoc"),
    path('cppquiz',views.cppquiz,name="cppquiz"),
    path('javaquiz',views.javaquiz,name="javaquiz"),
    path('cquiz',views.cquiz,name="cquiz"),
    path('javascriptquiz',views.javascriptquiz,name="javascriptquiz"),
    path('pythonquiz',views.pythonquiz,name="pythonquiz"),
    path('djangoquiz',views.djangoquiz,name="djangoquiz")
]
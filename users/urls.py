from django.urls import path,include
from django.contrib import admin
from django.views.generic import  ListView, DetailView 
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('',views.mainhome,name="home"),
    #path('index/',views.index,name="index"),
    path('signin/',auth_views.LoginView.as_view(template_name="signin.html"),name="signin"),
    path('signout/',auth_views.LogoutView.as_view(template_name="signout.html"),name="signout"), #if we dotn write this user defined logout then default admin logout page will be displayed
    path('signup/', views.signup,name="signup"), #these names are used in html ref
    #path('case/',CaseList.as_view(queryset=Case.objects.all().order_by("-date"),template_name='case_list.html')), #pylint error
    #path('check/', views.check, name="check"),
    #path('case/(?P<pk>\d+)',DetailView.as_view(model=Case,template_name='case_detail.html')) old version
   # path('case/<int:pk>/',DetailView.as_view(model=Case,template_name='case_detail.html'))
    path('case/',include('pop.urls')),
    path('mainhome/',views.mainhome,name="mainhome"),
    path('profile/',views.profile,name="profile")
]       
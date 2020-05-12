from django.urls import path
from django.contrib import admin
from .models import Case 
from . import views 
from .views import (
    CaseListView,
    CaseDetailView,
    CaseCreateView,
    CaseUpdateView,
    CaseDeleteView,
    CaseFoundView,
    CaseConfirmView,
    UnfoundlistView,
    FoundlistView,
    FoundbymelistView,
    CaseFinderCreateView,
    CaseFinderListView,
    CaseFinderDeleteView
)

urlpatterns = [
    #class-based views
    path('',CaseListView.as_view(),name='case'), #pylint error
    #path('case/(?P<pk>\d+)',DetailView.as_view(model=Case,template_name='case_detail.html')) old version
     path('case_finder_list',CaseFinderListView.as_view(),name='case_finder_list'),
    path('<int:pk>/',CaseDetailView.as_view(),name='case_detail'),
    path('<int:pk>/update/',CaseUpdateView.as_view(),name='case_update'),
     path('<int:pk>/found/',CaseFoundView.as_view(),name='case_found'),
      path('<int:pk>/confirm/',CaseConfirmView.as_view(),name='case_confirm'),
     path('<int:pk>/delete/',CaseDeleteView.as_view(),name='case_delete'), 
      path('<int:pk>/case_finder_delete/',CaseFinderDeleteView.as_view(),name='case_finder_delete'), 
    path('new_case/',CaseCreateView.as_view(),name='new_case'), #requires case_form.html
     path('found/',FoundlistView.as_view(),name='found'),
     path('casefinder/',CaseFinderCreateView.as_view(),name='casefinder'),
     path('foundbyme/',FoundbymelistView.as_view(),name='foundbyme'),
     path('unfound/',UnfoundlistView.as_view(),name='unfound'), #pylint error

]

# <app>/<model>_<viewtype>.html is looked up by class-based views
#queryset=Case.objects.all().order_by("-lost_date"),template_name='case_list.html'
#path('<int:pk>/',DetailView.as_view(model=Case,template_name='case_detail.html'))
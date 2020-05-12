from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Case #to import outside , write pop.models

class CaseListView(ListView):
    model = Case
    template_name = 'case.html' # <app>/<model>_<viewtype>.html is looked up by class-based views #actually this line is not required since html is already names as case_list.html 
    context_object_name = 'cases' #see y to use this line
    queryset=Case.objects.filter(found_status = False)
    #ordering = ["-lost_location" ]
    # if we write template_name= 'case.html' then there is no need to rename the case.html to case_list.html
class CaseFinderListView(ListView):
    model = Case
    template_name = 'casefinderlist.html' # <app>/<model>_<viewtype>.html is looked up by class-based views #actually this line is not required since html is already names as case_list.html 
    context_object_name = 'cases' #see y to use this line
    queryset=Case.objects.filter(confirmed_status = False)
class UnfoundlistView(ListView):
    model = Case
    template_name = 'case.html'
    def get_queryset(self):
       return Case.objects.filter(user= self.request.user, found_status = False)
    
class FoundlistView(ListView):
    model = Case
    template_name = 'case.html'
    def get_queryset(self):
       return Case.objects.filter(user= self.request.user, found_status = True)
class FoundbymelistView(ListView):
    model = Case
    template_name = 'case.html'
    def get_queryset(self):
       return Case.objects.filter(founder_id = self.request.user.id , found_status = True)

class CaseDetailView(DetailView):
    model = Case
     
class CaseCreateView(LoginRequiredMixin, CreateView):
    model = Case
    fields = ['pet_type', 'pet_breed','pet_name', 'lost_date', 'lost_location', 'pet_image', 'reward', 'user_contact_no', 'user_address']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class CaseFinderCreateView(LoginRequiredMixin, CreateView):
    model = Case
    fields = ['pet_type', 'citizen_name', 'citizen_phone', 'found_location', 'found_date', 'found_pet_image']
    
    def form_valid(self, form):
         form.instance.founder_id = self.request.user.id
         form.instance.founder_username = self.request.user.username
         form.instance.found_status = True
         return super().form_valid(form)
        
class CaseFoundView(LoginRequiredMixin,  UpdateView):
    model = Case
    fields = ['citizen_name', 'citizen_phone', 'found_location','found_date', 'found_pet_image']
    def form_valid(self, form):
         form.instance.founder_id = self.request.user.id
         form.instance.founder_username = self.request.user.username
         form.instance.found_status = True
         return super().form_valid(form)
class CaseConfirmView(LoginRequiredMixin, UpdateView):
    model = Case
    fields = [ 'confirmed_status']
    def form_valid(self,form):
        if form.instance.confirmed_status == False:
            form.instance.founder_id = None
            form.instance.founder_username = None
            form.instance.citizen_name = None
            form.instance.citizen_phone = None
            form.instance.found_location = None
            form.instance.found_date = None
            form.instance.found_status = False
            form.instance.found_pet_image = 'default.jpg'
        return super().form_valid(form)

class CaseUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Case
    fields = ['pet_name', 'lost_date', 'lost_location', 'pet_image','reward', 'user_contact_no', 'user_address']
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        case = self.get_object()
        if self.request.user == case.user:
            return True
        else:
            return False

class CaseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Case
    success_url = '/case/'
    def test_func(self):
        case = self.get_object()
        if self.request.user == case.user:
            return True
        else:
           return False
class CaseFinderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Case
    success_url = '/case/case_finder_list'
    def test_func(self):
        case = self.get_object()
        if self.request.user.username == case.founder_username:
            return True
        else:
           return False
        
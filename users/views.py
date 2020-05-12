from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'You have got your account created {username}!!!, Now you can signin')
            return redirect("signin") #namespace given in path function
        else:
            messages.warning(request,'Account not Created, Invalid inputs!!')
    else:   
        form = UserRegisterForm()
    return render(request,"signup.html",{'form':form}) 
def signin(request):
    return render(request,"signin.html",{})
#def index(request):
#    return HttpResponse("<h1> hello index</h1>")
def home(request):
    return render(request,"home.html",{'footer_text':['this is the basic page','which contains nav bar']})
def mainhome(request):
    return render(request,"mainhome.html",{})
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile) #request.FILES for images
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request,f'You have successfully updated your account  {username}!!!')
            return redirect("profile") #namespace given in path function
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'profile.html',context)


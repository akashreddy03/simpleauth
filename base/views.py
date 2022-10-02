from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error')
    context = {}
    return render(request, 'base/login.html', context)

def registerPage(request):
    form = UserForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            logout(request)
        form = UserForm(request.POST)
        if form.is_valid():
            try: 
                user = form.save()
                login(request, user)
                return redirect('home')
            except:
                print("Error in try catch")
        else:
            print("error")
    context = {'form': form}
    return render(request, 'base/register.html', context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('home')
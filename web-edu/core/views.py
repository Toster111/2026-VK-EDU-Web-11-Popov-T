from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/signup.html')

def profile(request):
    return render(request, 'core/profile.html')

def logout(request):
    return render(request, 'core/logout.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            fm = UserCreationForm()
            messages.success(request, 'Your Account created succesfully')
    else:
        fm = UserCreationForm()
    return render(request, 'login/signup.html', {'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request ,user)
                    messages.success(request, 'Logged in succesfully')
                    return redirect('home')
                else:
                    messages.info(request, 'Username or Password Maybe wrong')
        else:
            fm = AuthenticationForm()
        return render(request, 'login/login.html', {'form':fm})
    else:
        return redirect('home')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out Succesfully!!!!!!!!!! ')
    return redirect('login')

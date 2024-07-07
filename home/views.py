from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("/")
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid credentials. Please try again.'})

    # GET request (render the login form)
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

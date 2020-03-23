from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check passwords equality
        if password == password2:
            # username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                # email
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'email already registered with another user')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, email=email)
                    user.save()
                    auth.login(request, user)
                    messages.success(
                        request, 'You have been registered successfull and loged in')
                    return redirect('index')

        else:
            messages.error(request, 'Passwords do not match')

            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid Username or Password')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been logged Out')
    return redirect('index')
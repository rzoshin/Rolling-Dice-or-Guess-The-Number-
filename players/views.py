
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


def gamePage(request):
    return render(request, 'home.html')


def gtnGame(request):
    return render(request, 'gtn.html')

def gtnGameRule(request):
    return render(request, 'gtnRules.html')


def rdGame(request):
    return render(request, 'rd.html')


def rdGameRules(request):
    return render(request, 'rdRules.html')


def loginUser(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gtn-page')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Account was created for {form.cleaned_data.get('email')}")
            return redirect('login-user')
    context = {'form': form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login-user')

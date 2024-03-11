from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    # POST
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        # A
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            # AA
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    # GET
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    return render(request, 'users/register.html')

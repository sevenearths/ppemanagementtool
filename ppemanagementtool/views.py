from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from hospital.views import ListView


def loginView(request, username=None, password=None):
    if request.method == 'POST' and request.POST:
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(ListView)
            else:
                messages.add_message(request, messages.ERROR, 'Login incorrect')
    if username and password:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(ListView)
        else:
            messages.add_message(request, messages.ERROR, 'Login incorrect')
    return render(request, 'ppemanagementtool/login.html', {})

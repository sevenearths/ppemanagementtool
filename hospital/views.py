from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from hospital.models import Hospital, Inventory, Stock

@login_required
def ListView(request):
    return render(request, 'hospital/list.html', {'hospitals': Hospital.objects.all()})

@login_required
def FormView(request, hospital_name):
    hospital = Hospital.objects.filter(name=hospital_name.replace('-', ' ')).first()
    if hospital:
        return render(request, 'hospital/form.html', {'hospital':hospital})
    return redirect(ListView)

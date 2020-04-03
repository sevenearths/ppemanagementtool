from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from hospital.models import Hospital, Inventory, Stock
from hospital.forms import InventoryForm

@login_required
def ListView(request):
    return render(request, 'hospital/list.html', {'hospitals': Hospital.objects.all()})

@login_required
def FormView(request, hospital_name):
    if request.method == 'GET':
        return FormGET(request, hospital_name)
    if request.method == 'POST':
        return FormPOST(request, hospital_name)


# internal functions

def FormGET(request, hospital_name):
    hospital = Hospital.objects.filter(name=hospital_name.replace('-', ' ')).first()
    if hospital is None:
        messages.add_message(request, messages.ERROR, 'Hospital does not exist')
        return redirect(ListView)
    forms = []
    for stock in Stock.objects.all():
        initial_data = {
            'hospital':hospital,
            'stock': stock,
        }
        form = InventoryForm(initial=initial_data)
        last_update = Inventory.objects.filter(hospital=hospital,stock=stock).first()
        if last_update:
            form = InventoryForm(instance=last_update)
        details = {
            'form':form,
            'stock': stock,
            'last_update': last_update
        }
        forms.append(details)
    data = {
        'hospital':hospital,
        'forms': forms
    }
    return render(request, 'hospital/form.html', data)

def FormPOST(request, hospital_name):
    form = InventoryForm(request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Data saved')
    else:
        messages.add_message(request, messages.ERROR, 'Data NOT saved')
    return FormGET(request, hospital_name)
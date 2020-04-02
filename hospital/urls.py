from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListView, name='hospital_list'),
    path('form/<slug:hospital_name>', views.FormView, name='hospital_form'),
]

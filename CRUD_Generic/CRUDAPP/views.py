from dataclasses import fields
from django.shortcuts import render
from.models import Employee
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ShowEmployee(ListView):
    model=Employee
    

class AddEmployee(CreateView):
    model=Employee
    fields='__all__'
    success_url= reverse_lazy('showEmp_url')

class UpdateEmployee(UpdateView):
    model=Employee
    fields='__all__'
    success_url= reverse_lazy('showEmp_url')
    


class DeleteEmployee(DeleteView):
    model=Employee
    fields='__all__'
    success_url= reverse_lazy('showEmp_url')
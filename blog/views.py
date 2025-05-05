from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Emp

# Create your views here.

class EmpListView(ListView):
    model = Emp
    template_name = 'home.html'

class EmpDetailView(DetailView):
    model = Emp
    template_name = 'emp_detail.html'

from django.shortcuts import render

from django.urls import reverse_lazy


from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . models import Emp





# Create your views here.

class EmpListView(ListView):
    model = Emp
    template_name = 'home.html'

class EmpDetailView(DetailView):
    model = Emp
    template_name = 'emp_detail.html'

class EmpCreateView(CreateView):
    model = Emp
    template_name='emp_new.html'
    fields = '__all__'


class EmpUpdateView(UpdateView):
    
    model = Emp

    fields = '__all__'

    template_name = 'emp_edit.html'

class EmpDeleteView(DeleteView):

    model = Emp

    template_name = 'emp_delete.html'

    success_url = reverse_lazy('home')









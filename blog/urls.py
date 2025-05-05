from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmpListView.as_view(), name='home'),
    path('emp/<int:pk>/', views.EmpDetailView.as_view(), name='emp_detail'),
    ]
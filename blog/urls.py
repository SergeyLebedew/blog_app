from django.urls import path


from . import views

urlpatterns = [
    path('', views.EmpListView.as_view(), name='home'),

    path('emp/<int:pk>/', views.EmpDetailView.as_view(), name='emp_detail'),

    path('emp/new', views.EmpCreateView.as_view(), name='emp_new'),

    path('emp/<int:pk>/edit/', views.EmpUpdateView.as_view(), name='emp_edit'),

    path('emp/<int:pk>/delete/', views.EmpDeleteView.as_view(), name='emp_delete'),
    ]

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.employee_create, name='employee_create'),
    path('list/', views.employee_list, name='employee_list'),
]

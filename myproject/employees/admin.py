from django.contrib import admin
from .models import Employee, Project

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'email', 'designation', 'role', 'project', 'timestamp')
    search_fields = ('employee_id', 'name', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

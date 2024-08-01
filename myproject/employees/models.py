from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('Employee', 'Employee'),
        ('Lead', 'Lead'),
        ('Manager', 'Manager'),
    ]
    
    ROLE_CHOICES = [
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Tester', 'Tester'),
        # Add more roles as needed
    ]

    employee_id = models.CharField(
        max_length=10, 
        primary_key=True, 
        validators=[MinLengthValidator(1)],
        unique=True
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator()]
    )
    designation = models.CharField(
        max_length=10,
        choices=DESIGNATION_CHOICES
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        blank=True,
        null=True
    )
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(6)]
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)  # Set this to auto_now_add

    def __str__(self):
        return f'{self.name} ({self.employee_id})'

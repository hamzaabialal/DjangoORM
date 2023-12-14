from django.contrib import admin
from .models import Departements, Student
# Register your models here.

@admin.register(Departements)
class DepartemenetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'faculty']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'father_name']
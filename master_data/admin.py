from django.contrib import admin
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name']


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title']


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'contact_person',
        'phone'
    ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = [
        'emp_code',
        'name',
        'designation',
        'department',
        'contractor',
        'current_status',
        'daily_wage'
    ]

    list_filter = [
        'department',
        'designation',
        'current_status',
    ]

    search_fields = [
        'emp_code',
        'name',
        'cnic',
        'phone'
    ]
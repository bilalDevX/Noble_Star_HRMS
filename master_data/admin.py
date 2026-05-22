from django.contrib import admin
from .models import Plant, Department, Designation, Contractor, Employee


# =========================
# 🏭 PLANT ADMIN
# =========================
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name',)
    ordering = ('name',)


# =========================
# 🏢 DEPARTMENT ADMIN
# =========================
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


# =========================
# 👨‍🔧 DESIGNATION ADMIN
# =========================
@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    ordering = ('title',)


# =========================
# 🏗️ CONTRACTOR ADMIN
# =========================
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'contact_person', 'phone')
    search_fields = ('company_name', 'contact_person', 'phone')


# =========================
# 👷 EMPLOYEE ADMIN (CORE HRMS)
# =========================
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'emp_code',
        'name',
        'cnic',
        'plant',
        'department',
        'designation',
        'current_status',
        'daily_wage'
    )

    list_filter = (
        'plant',
        'department',
        'designation',
        'current_status'
    )

    search_fields = (
        'emp_code',
        'name',
        'cnic',
        'phone'
    )

    ordering = ('emp_code',)

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Basic Info", {
            'fields': (
                'emp_code',
                'name',
                'father_name',
                'cnic',
                'phone',
                'address'
            )
        }),

        ("Company Structure", {
            'fields': (
                'plant',
                'department',
                'designation',
                'contractor'
            )
        }),

        ("Documents", {
            'fields': (
                'profile_pic',
                'cnic_front',
                'cnic_back'
            )
        }),

        ("Salary Info", {
            'fields': (
                'daily_wage',
                'overtime_rate'
            )
        }),

        ("Status Info", {
            'fields': (
                'current_status',
                'reference',
                'remarks'
            )
        }),

        ("System Info", {
            'fields': (
                'created_at',
                'updated_at'
            )
        }),
    )
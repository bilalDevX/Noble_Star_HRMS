from django.db import models


# =========================
# 🏭 PLANT (MAIN COMPANY UNITS)
# =========================
class Plant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


# =========================
# 🏢 DEPARTMENT
# =========================
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# =========================
# 👨‍🔧 DESIGNATION
# =========================
class Designation(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


# =========================
# 🏗️ CONTRACTOR
# =========================
class Contractor(models.Model):
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


# =========================
# 👷 EMPLOYEE MASTER (CORE HRMS)
# =========================
class Employee(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('resigned', 'Resigned'),
    )

    emp_code = models.CharField(max_length=20, unique=True, db_index=True)
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)

    cnic = models.CharField(max_length=15, unique=True, db_index=True)
    phone = models.CharField(max_length=20)

    # 🏭 PLANT ASSIGNMENT (MOST IMPORTANT)
    plant = models.ForeignKey(
        Plant,
        on_delete=models.PROTECT,
        related_name='employees'
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees'
    )

    designation = models.ForeignKey(
        Designation,
        on_delete=models.SET_NULL,
        null=True
    )

    contractor = models.ForeignKey(
        Contractor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    address = models.TextField()

    # 📸 DOCUMENTS
    profile_pic = models.ImageField(
        upload_to='employees/profile/',
        null=True,
        blank=True
    )

    cnic_front = models.ImageField(
        upload_to='employees/cnic/',
        null=True,
        blank=True
    )

    cnic_back = models.ImageField(
        upload_to='employees/cnic/',
        null=True,
        blank=True
    )

    # 💰 SALARY INFO
    daily_wage = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    overtime_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # 📊 STATUS
    current_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        db_index=True
    )

    reference = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    # 🕒 TIMESTAMPS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['emp_code']
        indexes = [
            models.Index(fields=['emp_code']),
            models.Index(fields=['cnic']),
            models.Index(fields=['plant']),
            models.Index(fields=['department']),
        ]

    def __str__(self):
        return f"{self.emp_code} - {self.name}"
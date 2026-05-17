from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Contractor(models.Model):
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Employee(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('resigned', 'Resigned'),
    )

    emp_code = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)

    cnic = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=20)

    address = models.TextField()

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

    joining_date = models.DateField()

    resign_date = models.DateField(
        blank=True,
        null=True
    )

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

    current_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    line_location = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    reference = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['emp_code']

    def __str__(self):
        return f"{self.emp_code} - {self.name}"
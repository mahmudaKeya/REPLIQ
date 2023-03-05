from django.db import models
from django.utils import timezone
from django.apps import apps
from django.apps import AppConfig

# app = AppConfig(name='tracker')

class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'tracker'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    # description = models.TextField()
    condition = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(default=timezone.now)
    checked_in_at = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=255)
    condition_when_checked_in = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.device} - {self.employee}'

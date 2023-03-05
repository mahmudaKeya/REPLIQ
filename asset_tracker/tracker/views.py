from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from tracker.models import Company, Employee, Device, DeviceLog


class CompanyListView(View):
    def get(self, request):
        companies = Company.objects.all()
        return render(request, 'company_list.html', {'companies': companies})


class CompanyDetailView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, id=company_id)
        employees = Employee.objects.filter(company=company)
        return render(request, 'company_detail.html', {'company': company, 'employees': employees})


class DeviceListView(View):
    def get(self, request, company_id):
        devices = Device.objects.filter(company_id=company_id)
        return render(request, 'device_list.html', {'devices': devices, 'company_id': company_id})


class DeviceDetailView(View):
    def get(self, request, company_id, device_id):
        device = get_object_or_404(Device, id=device_id, company_id=company_id)
        return render(request, 'device_detail.html', {'device': device, 'company_id': company_id})


class DeviceLogView(View):
    def get(self, request, company_id, device_id):
        device = get_object_or_404(Device, id=device_id, company_id=company_id)
        employees = Employee.objects.filter(company_id=company_id)
        return render(request, 'device_log.html', {'device': device, 'employees': employees, 'company_id': company_id})

    def post(self, request, company_id, device_id):
        device = get_object_or_404(Device, id=device_id, company_id=company_id)
        employee = get_object_or_404(Employee, id=request.POST['employee'])
        condition_when_checked_out = request.POST['condition_when_checked_out']
        DeviceLog.objects.create(device=device, employee=employee, condition_when_checked_out=condition_when_checked_out)
        return redirect('device_detail', company_id=company_id, device_id=device_id)

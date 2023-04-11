from multiprocessing import context
from django.shortcuts import render
from employee.forms import *
# Create your views here.

def home(request):
    officeform = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        "officeform":officeform,
        "employeeform":employeeForm
    }
    return render(request,'index.html',context)
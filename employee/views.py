from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import EmpForm
from .models import Employee
from django.conf import settings
# Create your views here.

@login_required()
def empForm(request):
    form = EmpForm()
    return render(request,'employee/addemp.html',{'form':form})

@login_required(redirect_field_name="accounts/index.html")
def addEmp(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'employee/addemp.html',{'error':"Employee Added Successfully...!!!",'form':EmpForm()})
        else:
            return render(request,'employee/addemp.html',{'error':"Employee Not Added.",'form':EmpForm()})

@login_required(redirect_field_name="index.html")
def empDetails(request):
    employees = Employee.objects.all()
    return render(request,'employee/show.html',{'employees':employees})

@login_required(redirect_field_name="index.html")
def editEmp(request,id):
    emp = Employee.objects.get(eid=id)
    return render(request,'employee/edit.html',{'emp':emp})

@login_required(redirect_field_name="index.html")
def updateEmp(request,id):
    if request.method == "POST":
        emp = Employee.objects.get(eid=id)
        form = EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('empdetails')
        else:
            return render(request,'edit.html',{'emp':emp})


@login_required (redirect_field_name="index.html")   
def destroy(request,id):
    emp = Employee.objects.get(eid=id)
    emp.delete()
    return redirect('empdetails')
    

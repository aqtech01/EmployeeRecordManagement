from multiprocessing import AuthenticationError
from django.db import IntegrityError
from django.shortcuts import render,redirect

from employee.forms import EmployeeEducationForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect("employee_signin")
    return render(request, "employee/index.html",{"title":"Home"})

def employee_signup(request):
   
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        employee_code = data.get("employee_code")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        
        if password != confirm_password:
            messages.error(request, "Password and Confirm Password should be the same")
            return render(request, "employee/signup.html", {"title": "Employee SignUp"})
        
        try:
            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, password=password, email=email)
            EmployeeDetail.objects.create(user=user, employee_code=employee_code)
            messages.success(request, "Employee Created Successfully")
            return redirect("employee_signin")
        except IntegrityError:
            messages.error(request, "A user with this email or employee code already exists.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    
    return render(request, "employee/signup.html", {"title": "Employee SignUp"})
def employee_signin(request):
    
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")
        try:
            user = authenticate(username= email,password=password)
            if User:
                login(request,user)
                return redirect("/")
            else:
                messages.error("User not found")
        except AuthenticationError as e:
            return f" Error : {e}"
   
    return render(request, "employee/signin.html",{"title":"Signin"})


def profile(request):
    if not request.user.is_authenticated:
        return redirect("employee_signin")
    
    user = request.user
    employee= EmployeeDetail.objects.get(user=user)

    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        employee_code = data.get("employee_code")
        employee_department = data.get("employee_department")
        employee_designation = data.get("employee_designation")
        employee_contact = data.get("employee_Contact")
        employee_gender = data.get("employee_gender")
        employee_joining_date = data.get("employee_joining_date")
        # Update the value after geeting the value from form 
        employee.user.first_name= first_name
        employee.user.last_name = last_name
        employee.employee_code= employee_code
        employee.employee_department = employee_department
        employee.employee_designation = employee_designation
        employee.employee_contact = employee_contact
        employee.employee_gender = employee_gender
        if employee_joining_date:
            employee.employee_joining_date = employee_joining_date
            try:
                employee.user.save()
                employee.save()
                messages.success(request, "Profile Updated Successfully")
            except:
                return "Something Wrong"
            
    return render(request, "employee/profile.html",{"employee":employee,"title":"Profile"})


def employee_logout(request):
    logout(request)
    return redirect("home")
# Employee Education Details

def employee_education(request):

    form = EmployeeEducationForm()
    if request.method == "POST":
        form = EmployeeEducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")


    return render(request,"employee/education.html",{"form":form})

# Admin Login 

def admin_signin(request):
    return render(request,"employee/admin/signin.html")

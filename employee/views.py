from multiprocessing import AuthenticationError
from django.db import IntegrityError
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request, "employee/index.html")

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
    return render(request, "employee/signin.html")
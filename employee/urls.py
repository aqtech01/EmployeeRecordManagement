from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("employee_signup/",employee_signup,name="employee_signup"),
    path("employee_signin/",employee_signin,name="employee_signin"),
]

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    employee_code = models.IntegerField(default=0)
    employee_department = models.CharField(max_length=100,null=True)
    employee_desigantion = models.CharField(max_length=100, null=True)
    employee_contact = models.CharField(max_length=100,null=True)
    employee_gender = models.CharField(max_length=50,null=True)
    employee_joining_date = models.DateField(null=True,)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) :
        return self.user.username


class EmployeeEducation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # Post Graduation
    postg_course = models.CharField(max_length=100,null=True)
    postg_passing_year = models.CharField(max_length=30,null=True)
    postg_institiute= models.CharField(max_length=100,null=True)
    postg_percentage = models.CharField(max_length=20,null=True)

    # Graduation

    graduation_course = models.CharField(max_length=100,null=True)
    graduation_passing_year = models.CharField(max_length=30,null=True)
    graduation_institiute= models.CharField(max_length=100,null=True)
    graduation_percentage = models.CharField(max_length=20,null=True)
    # Higher Scondary
    highers_course = models.CharField(max_length=100,null=True)
    highers_passing_year = models.CharField(max_length=30,null=True)
    highers_institiute= models.CharField(max_length=100,null=True)
    highers_percentage = models.CharField(max_length=20,null=True)
    # Scondary
    scondary_course = models.CharField(max_length=100,null=True)
    scondary_passing_year = models.CharField(max_length=30,null=True)
    scondary_institiute= models.CharField(max_length=100,null=True)
    scondary_percentage = models.CharField(max_length=20,null=True)

    def __str__(self) :
        return self.user.username
    


class EmployeeExperience(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        # Comapny 1 Details
        compnay1_name=models.CharField(max_length=100,null=True)
        company1_desigantion = models.CharField(max_length=100,null=True)
        company1_duration = models.CharField(max_length=100,null=True)
        company1_salary = models.CharField(max_length=100,null=True)

        # Comapny 2 Details

        compnay2_name=models.CharField(max_length=100,null=True)
        company2_desigantion = models.CharField(max_length=100,null=True)
        company2_duration = models.CharField(max_length=100,null=True)
        company2_salary = models.CharField(max_length=100,null=True)
       #comapny 3 Details

        compnay3_name=models.CharField(max_length=100,null=True)
        company3_desigantion = models.CharField(max_length=100,null=True)
        company3_duration = models.CharField(max_length=100,null=True)
        company3_salary = models.CharField(max_length=100,null=True)

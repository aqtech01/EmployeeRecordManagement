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
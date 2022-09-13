from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registration(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20, default='')
    lastname = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=10, default='')
    contact = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=500, default='')
    user_type = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.firstname



class UserDetail(models.Model):
    contact_id= models.CharField(max_length=15,null=True)
    Address = models.CharField(max_length=100, null=True)
    Department = models.CharField(max_length=100, null=True)

    def __Str__(Self):
        return Self.user.username


class Leave(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    leave_id= models.IntegerField (primary_key=True,default=" ")
    # user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    leaves_name=models.CharField(max_length=100, null=True)
    total_leave = models.CharField(max_length=100, null=True)
    consume_leave = models.CharField(max_length=100, null=True)
    balance_leave= models.CharField(max_length=100, null=True)

    def __Str__(Self):
        return Self.User.Username

class Leave_Application(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    # leave_id= models.ForeignKey(User,on_delete=models.CASCADE)
    application_id = models.IntegerField( primary_key=True, default=" ")
    # user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    To_date=models.DateField ()  #(max_length=100, null=True)
    From_date = models.DateField (null=True,blank=True)
    Reason = models.CharField(max_length=200, null=True)
    leave_status= models.BooleanField ()#(max_length=100, null=True)

    def __Str__(Self):
        return Self.User.Username

class Department(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
     # user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    dept_id = models.IntegerField( primary_key=True, default=" ")
    Dept_name = models.CharField(max_length=200, null=True)


    def __Str__(Self):
        return Self.User.Username


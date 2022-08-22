from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import  MinValueValidator

class User_Role(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    name_role = models.CharField(max_length=50,unique=True ,null=True,blank=True)

    def __str__(self):
        return self.name_role 

class Customer(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    phone_No = models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name +  " " + self.last_name  
        

class Adminstrator(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name +  " " + self.last_name  
        
class Countrie(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=50,unique=True ,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return self.name


class Airline_Companie(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=70,unique=True ,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    countrie = models.ForeignKey(Countrie, on_delete=models.CASCADE,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  


class Flight(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    status =models.BooleanField(default=True)
    airline_Companie = models.ForeignKey(Airline_Companie, on_delete=models.CASCADE,null=True,blank=True)
    origin_countrie = models.ForeignKey(Countrie,related_name='origin_countrie', on_delete=models.CASCADE,null=True,blank=True)
    destination_countrie = models.ForeignKey(Countrie,related_name='destination_countrie',on_delete=models.CASCADE,null=True,blank=True)
    departure_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    landing_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    remaining_tickets = models.IntegerField(MinValueValidator(1),null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    price = models.CharField(max_length=10,null=True,blank=True)        

    def __str__(self):
        return "origin countrie: " + str(self.origin_countrie) +  " |" + "destination countrie: " + str(self.destination_countrie)  


class Tickets(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    flight= models.ForeignKey(Flight, on_delete=models.CASCADE, null=True,blank=True)
    number_of_tickets = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return  str(self.flight) + "| customer name: " + str(self.customer)  +  " number of tickets:  " + str(self.number_of_tickets)

class UserProfile(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    user_role = models.ForeignKey(User_Role,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return " name: " + str(self.user) +  " role: " + str(self.user_role)  
        
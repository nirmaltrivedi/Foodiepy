from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
	owner_name = models.ForeignKey(User,on_delete=models.CASCADE)
	res_name = models.CharField(max_length=200)
	phone_num = models.BigIntegerField(null=True, blank=True)
	add_line1 = models.TextField(null=True, blank=True)
	add_line2 = models.TextField(null=True, blank=True)
	city = models.CharField(max_length=50,null=True, blank=True)
	state = models.CharField(max_length=50,null=True, blank=True)
	staff = models.IntegerField(null=True, blank=True)
	open_time = models.TimeField(null=True, blank=True)
	close_time = models.TimeField(null=True, blank=True)
	res_type = models.CharField(max_length=50,null=True, blank=True)
	founded_year = models.IntegerField(null=True, blank=True)
	website = models.URLField(null=True, blank=True)
	instagram = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.res_name

class Customer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	add_line1 = models.TextField()
	add_line2 = models.TextField()
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cuisine = models.CharField(max_length=50)
	pro_name = models.CharField(max_length=200)
	pro_price = models.BigIntegerField()

	def __str__(self):
		return self.cuisine

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			('Cancelled','Cancelled'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.CharField(max_length=200,null=True,default="")

	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def _str_(self):
		return self.product
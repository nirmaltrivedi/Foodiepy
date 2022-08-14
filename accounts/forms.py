from django.forms import ModelForm
from .models import Order, Customer, Product
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['customer','product','status']

class CreateProduct(ModelForm):
	class Meta:
		model = Product
		fields = ['cuisine','pro_name','pro_price']


class CreateCustomer(ModelForm):
	class Meta:
		model = Customer
		fields = ['name','phone','email','add_line1','add_line2','city','state']


class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(label="First name")
	last_name = forms.CharField(label="Last name")
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

	def save1(self, commit=True):
		user = super(CreateUserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		first_name = self.cleaned_data["first_name"]
		last_name = self.cleaned_data["last_name"]

		user.first_name = first_name
		user.last_name = last_name
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user



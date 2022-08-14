from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.forms import inlineformset_factory
from .filter import OrderFilter
import pickle
from numpy import asarray
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# from .decorators import unauthenticated_user, allowed_users, admin_only
from django.http import HttpResponse
# Create your views here.


def landingpage(request):

	return render(request,'accounts/landingpage.html')


def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save1()
			user = form.cleaned_data.get('username')
			# group = Group.objects.get(name='customer')
			# user.groups.add(group)
			# Customer.objects.create(
			# 	user=user,
			# 	name=user.username,
			# )
			messages.success(request, 'Account was created for ' + user)

			return redirect('home')

	context = {'form': form}
	return render(request, 'accounts/register.html', context)

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('landing')

@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for delivery').count()
    cancelled = orders.filter(status='Cancelled').count()

    context = {'orders': orders, 'customers': customers,'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending,'out_for_delivery':out_for_delivery,'cancelled':cancelled}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def userPage(request):
	orders = request.user.customer.order_set.all()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()


	context = {'orders': orders, 'total_orders': total_orders,
			   'delivered': delivered, 'pending': pending}
	return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def create_customer(request):
	profile = CreateCustomer()
	if request.method == 'POST':
		forms = CreateCustomer(request.POST)
		# forms['user'] = CreateUserForm.objects.get()
		if forms.is_valid():
			profile = forms.save(commit=False)
			profile.user = request.user
			profile.save()
			# forms.save()
			return redirect('home')
	context ={'form':profile}
	return render(request, 'accounts/create_customer.html',context)


@login_required(login_url='login')
def create_product(request):
	product = CreateProduct()
	if request.method == 'POST':
		forms = CreateProduct(request.POST)
		if forms.is_valid():
			product = forms.save(commit=False)
			product.user = request.user
			product.save()
			return redirect('home')
	context ={'form':product}
	return render(request, 'accounts/create_product.html',context)


@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()
	order_count = orders.count()
	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs
	context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter':myFilter}
	return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('home')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('home')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)

def forecasting(request):
    if request.POST:
        model = pickle.load(open('gradientboostmodel.pkl', 'rb'))
        category = request.POST['category']
        cuisine = int(request.POST['cuisine'])
        week = int(request.POST['week'])
        checkout_price = float(request.POST['checkout_price'])
        base_price = float(request.POST['base_price'])
        emailer = int(request.POST['emailer'])
        homepage = int(request.POST['homepage'])
        city = int(request.POST['city'])
        region = int(request.POST['region'])
        op_area = float(request.POST['op_area'])
        center_type = int(request.POST['center_type'])
        category = int(category)
        list = [category,cuisine,week,checkout_price,base_price,emailer,homepage,city,region,op_area,center_type]
        data = asarray([list])
        output = model.predict(data)
        output = int(output)
        if output < 0:
            output = 0
        context = {'output':output,'category':category,'cuisine':cuisine,'week':week,'checkout_price':checkout_price,'base_price':base_price,'emailer':emailer,'homepage':homepage,'city':city,'region':region,'op_area':op_area,'center_type':center_type}
        return render(request, 'accounts/forecasting.html', context)
    return render(request,'accounts/forecasting.html')


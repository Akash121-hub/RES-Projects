from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decoraters import unauthorized_user

@unauthorized_user
def registerPage(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success('You have {} successfully registered'.format(user))
			return redirect('login')
	context = {form:'form'}
	return render(request, 'accounts/register.html', context)

@unauthorized_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login (request, user)
			return redirect('home')
		else:
			messages.info(request, 'username or password is incorrect')
			return render(request, 'accounts/login.html')
	context = {}
	return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logoutPage(request):
	logout(request)
	return redirect('login')


def userPage(request):
	context = {}
	return render(request, 'accounts/user.html', context)






@login_required(login_url='login')
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending, 'customers':customers }

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk):
	customer = Customer.objects.get(id=pk)

	orders = customer.order_set.all()
	order_count = orders.count()
	myFilter = OrderFilter(request.GET, queryset=orders)
	order = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)


def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html')

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)
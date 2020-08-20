from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import TodoModel
from .forms import TodoForm
# Create your views here.
def index(request):
	item_list = TodoModel.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	form = TodoForm()
	page = { 
             "forms" : form, 
             "list" : item_list, 
             "title" : "TODO LIST", 
           }
	return render(request, 'index.html', page)

def remove(request, item_id): 
    item = TodoModel.objects.get(id=item_id) 
    item.delete() 
    messages.info(request, "item removed !!!") 
    return redirect('index') 

def signup(request):
	context = {}
	form = UserCreationForm(request.POST)
	context['form'] = form
	if request.method == 'POST':
		if form.is_valid():
			usr = form.save()
			usr.save()
			auth_login(request, usr)
			return redirect('index')
	else:
		return render(request, "register.html", context)
			#usr = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'])
def login(request):
	
	username = request.POST.get('username1')
	password = request.POST.get('password1')

	usr = authenticate(request, username=username, password = password)
	#auth_login(request, usr)
	if usr is not None:
		auth_login(request, usr)
		return redirect('index')
	else:
		return render(request, "login.html")

def logout(request):
	auth_logout(request)
	#messages.info(request, "Logged out successfully!")
	return redirect('index')
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this


# Create your views here.
def homepage(request):
	return render(request, template_name='home.html')

def mainpage(request):
	return render(request, template_name='mainpage.html')


def register_request(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Registration successful.')
			return redirect('homepage')
		messages.error(request, 'Registration failed' )
	form = NewUserForm()
	return render (request=request, template_name='register.html', context={'register_form':form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request=request,template_name='mainpage.html')
			else:
				messages.error(request,"Invalid username or password.")
		
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

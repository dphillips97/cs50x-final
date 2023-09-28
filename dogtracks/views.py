from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.urls import reverse

from .models import *

def index(request):

	if request.user.is_authenticated:

		pets = Animal.objects.filter(owner=request.user)

		visits = Visit.objects.filter(requester=request.user)

		context = {"pets": pets,
					"visits": visits}

		return render(request, "dogtracks/dashboard.html", context)

	else:
		
		return render(request, "dogtracks/login.html")

def add_pet(request):

		if request.method == 'POST':

			form = AnimalForm(request.POST)

			if form.is_valid():
				
				pet = form.save(commit=False)
				pet.owner = request.user
				pet.save()
			
				return HttpResponseRedirect(reverse('index'))
		else:
			form = AnimalForm()

		# If GET or form is not valid
		return render(request, "dogtracks/add-pet.html", {"form": form})

def update_pet(request, id):

	pet = Animal.objects.get(id=id)
	context = {"pet": pet}
	return render(request, "dogtracks/update-pet.html", context)

def remove_pet(request, id):

	pet = Animal.objects.get(id=id)
	context = {"message": f"{pet.name} removed."}
	pet.delete()
	return HttpResponseRedirect(reverse('index'))


def login_view(request):
	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		
		# Successful login
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))

		# Can't autenticate
		else:
			return render(request, 'dogtracks/login.html', 
				{"message": "Please try again."})

	# GET call
	else:
		return render(request, 'dogtracks/login.html')

def logout_view(request):

	logout(request)
	return HttpResponseRedirect(reverse("index"))

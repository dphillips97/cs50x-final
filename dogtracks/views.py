from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import JsonResponse, HttpResponseForbidden
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

def edit_pet(request, id=None):
# Create an instance or existing pet OR new pet
# to use same logic for edit and update

	# If id is passed in the url then this is an edit
	# So return existing pet object
	if id:
		pet = Animal.objects.filter(id=id).first()
		title = f"Editing Info for {pet.name}"

		if pet.owner != request.user:
			return HttpResponseForbidden()

	# No id; create new Animal()
	else:
		pet = Animal(owner=request.user)
		title = "Let's add your pet!"

	# Submit: must pass instance for create and edit. 
	# Do not need 'commit=False' since new pet will have owner set
	# from this view and existing pet already has owner
	if request.method == 'POST':

		form = AnimalForm(request.POST, instance=pet)
		
		if form.is_valid():
			pet.save()
			return HttpResponseRedirect(reverse('index'))

	# Return unbound form
	elif request.method == 'GET':

		form = AnimalForm(instance=pet)

	context = {"form": form,
				"title": title}

	return render(request, "dogtracks/pet-form.html", context)


def remove_pet(request, id):

	pet = Animal.objects.get(id=id)
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

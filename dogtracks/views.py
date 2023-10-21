from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json
from datetime import date
from .models import *

def index(request):

	if request.user.is_authenticated:

		pets = Animal.objects.filter(owner=request.user)

		context = {"pets": pets}
					#"visits": visits

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


def edit_visit(request, id=None):
# Create an instance or existing pet OR new pet
# to use same logic for edit and update
	if id:
		visit = Visit.objects.filter(id=id).first()
		title = f"Editing Visit #{visit.id}"

		if visit.requester != request.user:
			return HttpResponseForbidden()

	# No id; create new Visit()
	else:
		visit = Visit(requester=request.user)
		title = "Request a Visit"

	# Submit: must pass instance for create and edit. 
	# Do not need 'commit=False' since new pet will have owner set
	# from this view and existing pet already has owner
	if request.method == 'POST':

		form = VisitForm(request.POST, instance=visit)
		
		# Set status to 'request' upon submit even if visit status is 'cancel'
		if form.is_valid():

			visit.status = 'request'
			visit.save()
			return HttpResponseRedirect(reverse('index'))

	# Return unbound form
	elif request.method == 'GET':

		form = VisitForm(instance=visit)

	context = {"form": form,
				"title": title}

	return render(request, "dogtracks/visit-form.html", context)


def remove_visit(request, id):

	visit = Visit.objects.get(id=id)
	visit.delete()
	return HttpResponseRedirect(reverse('index'))

def change_visit_status(request, id):

	visit = Visit.objects.get(id=id)

	visit_status = visit.status

	if visit_status == 'cancel':
		visit.status = 'request'
	elif visit_status == 'request':
		visit.status = 'cancel'

	visit.save()

	return HttpResponseRedirect(reverse('index'))


def visit_type(request, visit_type):

	try:
		if visit_type == 'all':
			visits = Visit.objects.filter(requester=request.user).all()
		else:
			visits = Visit.objects.filter(status=visit_type).filter(requester=request.user).all()
	except:
		message = 'No visits found'

	return render(request, "dogtracks/visit-list.html", {'visits': visits})

		

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

# Borrowed from project 4 Network b/c I can't get
# a CreateUser form to work - maybe a AbstractUser
# class issue
def register(request):
	
	if request.method == "POST":

		username = request.POST["username"]
		password = request.POST["password"]
		password_confirm = request.POST["password_confirm"]
        
        # Handle in model eventually
		if password != password_confirm:
			return render(request, "dogtracks/register.html", {
				"message": "Passwords must match."})
		try:
			new_user = User.objects.create_user(username, password)
			new_user.save()

		except:
			return render(request, "dogtracks/register.html", {
				"message": "Username already taken, please choose another."})
        
		# Success
		login(request, new_user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "dogtracks/register.html")
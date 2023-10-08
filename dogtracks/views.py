from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json

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


def edit_visit(request, id=None):
# Create an instance or existing pet OR new pet
# to use same logic for edit and update
	if id:
		visit = Visit.objects.filter(id=id).first()
		title = f"Editing Info for Visit #{visit.id}"

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
		
		if form.is_valid():
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


# API call
@csrf_exempt
def visit_status(request, id):

	payload = {'message': None}

	try:
		visit = Visit.objects.get(id=id)

	except:

		payload['message'] = 'Can not find visit'

	if request.method == 'PUT':

		if visit.status == 'cancel':
			visit.status = 'request'
		elif visit.status in ('request', 'confirm'):
			visit.status = 'cancel'
		
		visit.save()

		payload['message'] = 'Visit updated successfully.'

	else:
		payload['message'] = 'PUT request required.'

	return JsonResponse(payload, safe=False)



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

from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from dogtracks.models import User, Animal, Visit
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
	list_display = ['name', 'owner', 'species']


# Fancy stuff from https://realpython.com/customize-django-admin-python/
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
	list_display = ['id', 'requester', 'status', 'start', 'duration', 'view_animals_link']
	list_filter = ['status','start']

	def view_animals_link(self, obj):

		# Get count of pets from user who requested visit
		pets = Animal.objects.filter(owner=obj.requester)
		pets_count = pets.count()

		url = reverse("admin:dogtracks_animal_changelist")
		url += "?"
		url += urlencode({"animal__owner": f"{obj.requester}"})

		return pets_count
		
		# return format_html('<a href="{}">{} Pets</a>', url, pets_count)

	view_animals_link.short_description = "Pet Count"

	

	

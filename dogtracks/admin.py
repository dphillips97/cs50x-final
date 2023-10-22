from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from dogtracks.models import User, Animal, Visit

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
	list_display = ['name', 'owner', 'species']

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
	list_display = ['id', 'requester', 'status', 'start', 'duration']
	list_filter = ['status','start']

	

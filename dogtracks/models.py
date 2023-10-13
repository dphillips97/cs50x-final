from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.forms.widgets import NumberInput
from datetime import date

# Create your models here.
class User(AbstractUser):
	pass

class Animal(models.Model):

	CHOICES = (('dog', 'Dog'), ('cat', 'Cat'), ('horse', 'Horse'), ('other', 'Other'))

	# shows up as owner_id
	owner = models.ForeignKey(User, related_name='animals', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=25, null=False, blank=False, verbose_name="Pet name")
	photo = models.FileField(upload_to='images', null=True, blank=True)
	breed = models.CharField(max_length=25, blank=True)
	species = models.CharField(choices=CHOICES, max_length=10, blank=True)
	birthday = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

	def __str__(self):
		return f"{self.name}"
	

class AnimalForm(ModelForm):
	class Meta:
		model = Animal
		fields = ['name', 'breed', 'species', 'birthday', 'photo']
		widgets = {'birthday': forms.NumberInput(attrs={'type': 'date'})}

class Visit(models.Model):

	# (database value, showing_to_user_in_modelforms)
	CHOICES = (('request','Request'), ('confirm', 'Confirm'), ('complete', 'Complete'), ('cancel','Cancel'))
	
	requester = models.ForeignKey(User, related_name='visits', on_delete=models.SET_NULL, null=True)
	status = models.CharField(choices=CHOICES, max_length=10, default='request')
	start = models.DateField(auto_now=False,auto_now_add=False)
	end = models.DateField(auto_now=False,auto_now_add=False)
	notes = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"Visit ({self.status}) by user {self.requester}"

	@property
	def get_visit_length(self):
		visit_length = self.end - self.start
		return visit_length.days

	# Need to override base class method since we're calculating duration
	def save(self, *args, **kwargs):
		self.visit_length = self.get_visit_length
		super(Visit, self).save(*args, **kwargs)

class VisitForm(ModelForm):
	class Meta:
		model = Visit
		fields = ['start', 'end', 'notes']
		widgets = {
					'start': forms.NumberInput(attrs={'type': 'date'}),
					'end': forms.NumberInput(attrs={'type': 'date'})
					}


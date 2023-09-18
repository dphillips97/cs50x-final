from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

	pass


class Animal(models.Model):

	# shows up as owner_id
	owner = models.ForeignKey(User, related_name='animals', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=25, null=False, blank=False)
	photo = models.FileField(upload_to='media/', null=True)
	breed = models.CharField(max_length=25, blank=True)
	species = models.CharField(max_length=25, blank=True)
	birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)

	def __str__(self):
		return f"{self.name}"

class AnimalForm(ModelForm):
	class Meta:
		model = Animal
		fields = ['name', 'photo', 'breed', 'species', 'birthday']


class Visit(models.Model):

	# (database value, showing_to_user_in_modelforms)
	CHOICES = (('request','Request'), ('confirm', 'Confirm'), ('complete', 'Complete'), ('cancel','Cancel'))
	
	requester = models.ForeignKey(User, related_name='visits', on_delete=models.SET_NULL, null=True)
	status = models.CharField(choices=CHOICES, max_length=10)
	start = models.DateField(auto_now=False,auto_now_add=False)
	end = models.DateField(auto_now=False,auto_now_add=False)

	def __str__(self):
		return f"Visit ({self.status}) by user {self.requester}"
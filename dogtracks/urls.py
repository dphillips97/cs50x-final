from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('', views.index, name='index'),
	path('update-pet/<int:id>', views.update_pet, name="update_pet"),
	path('remove-pet/<int:id>', views.remove_pet, name="remove_pet"),
]
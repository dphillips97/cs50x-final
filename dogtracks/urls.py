from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('', views.index, name='index'),

	# Add and update use same view
	path('add-pet/', views.edit_pet, name="add_pet"),
	path('update-pet/<int:id>', views.edit_pet, name="update_pet"),

	path('remove-pet/<int:id>', views.remove_pet, name="remove_pet"),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
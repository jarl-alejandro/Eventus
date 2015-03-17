from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ("email", "nombre", "is_admin")
	list_filter = ("is_admin", "nombre",)
	fieldsets = (
		(None, { 'fields':("email", "password") }),
		("Info Personal", { 'fields':('avatar', 'ciudad', 'edad', 'nombre',) }),
		("Permissions", { 'fields':("is_admin",) })	
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields':('email', 'nombre', 'password1', 'password2')
		}),
	)

	search_fields = ('email',)
	ordering = ("email",)

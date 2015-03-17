from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **user_data):
		if not email:
			raise ValueError("El email es obligatorio")

		user = self.model(
			email = self.normalize_email(email),
			**user_data
		)

		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, email, password, **user_data):
		user = self.create_user(email,
			password = password,
			**user_data
		)
		user.is_admin = True
		user.save(using = self._db)
		return user

class User(PermissionsMixin, AbstractBaseUser):
	email = models.EmailField(unique = True)
	avatar = models.ImageField(upload_to = "avatar")
	ciudad = models.CharField(max_length = 140)
	nombre = models.CharField(max_length = 140)
	edad = models.IntegerField(default = 0)

	is_active = models.BooleanField(default = True)
	is_admin = models.BooleanField(default = False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nombre', 'edad', 'ciudad']

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin
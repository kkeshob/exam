from django.db import models
from admin_dash.models import Course
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
	def create_user(self,roll,phone,name,password=None):
		if not roll:
			raise ValueError('You Dont have Permission to do exam')
		user = self.model(
			roll=roll,
            phone=phone,
            name=name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self,roll,phone,name, password):
		user = self.create_user(roll,phone,name,password=password)
		user.is_admin = True
		user.is_staff=True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	phone= models.CharField(verbose_name='phone number', max_length=12,unique=True)
	name=models.CharField(max_length=150,null=True)
	roll=models.CharField(max_length=20,verbose_name='roll',unique=True)
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	date_joind=models.DateTimeField(verbose_name='date joind', auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff=models.BooleanField(default=False)
	USERNAME_FIELD = 'roll'
	REQUIRED_FIELDS = ['name','phone']
	objects = UserManager()

	def __str__(self):
		return self.name

	def has_perm(self, perm, obj=None):
		return self.is_admin
	
	def has_module_perms(self, app_label):
		return True

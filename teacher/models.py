from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,AbstractUser, PermissionsMixin

class Student(models.Model):
    name = models.CharField("Name", max_length=20)
    age=models.IntegerField()
    grade=models.IntegerField()

class Teacher(models.Model):
    name  = models.CharField('Teacher Name',max_length=35,unique=True,)
    age=models.IntegerField()
    subject=models.CharField(max_length=30)
    
# class UserManager(BaseUserManager):
#     def create_user(self,username,password,**kwargs):
#         user=self.model(username=username)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         return self._create_user(**extra_fields)

class User(AbstractUser):
    pass
    # username=models.CharField(unique=True, max_length=16)
    # is_student=models.BooleanField(default=False)
    # # objects=UserManager()

    # USERNAME_FIELD='username'
    # REQUIERED_FIELDS=[]


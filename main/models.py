from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from .manager import *


class User(AbstractUser,PermissionsMixin):
    ROLE = (
        (1, 'ADMIN'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    GENDER = (
        (1, 'MALE'),
        (2, 'FEMALE'),
    )

    username = None
    user_id = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=245,unique=True,blank=True)
    role = models.IntegerField(choices=ROLE,default=1)
    gender = models.IntegerField(choices=GENDER,default=1)
    middle_name = models.CharField(max_length=100,blank=True)
    profile_pic = models.ImageField(upload_to='media/profile_pic',default='dashboard/assets/img/logo.png')
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []
    objects = UserManager()
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Classes(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Classes."""

        verbose_name = 'Classes'
        verbose_name_plural = 'Classess'

    def __str__(self):
        return self.name + self.code

class Section(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Classes."""

        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return self.name + self.code


class Student(models.Model):


    admin = models.OneToOneField(User,on_delete=models.CASCADE)
    student_id = models.IntegerField(blank=True,null=True)
    dob = models.DateField(max_length=8)
    mobile_number1 = models.IntegerField()
    mobile_number2 = models.IntegerField(blank=True, null=True)
    father_name =models.CharField(max_length=100)
    mother_name =models.CharField(max_length=100)
    address = models.TextField()
    permanent_address =models.TextField()
    aadhar_number = models.IntegerField()
    ssmid = models.IntegerField()
    aadhar_image = models.ImageField(upload_to='media/student/aadhar_pic')
    ssmid_image = models.ImageField(upload_to='media/student/ssmid_pic')
    date_of_admission = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Student'
        verbose_name_plural = 'Studentss'

    def __str__(self):

        pass

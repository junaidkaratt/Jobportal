from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
import enum

class UserRole(enum.Enum):
    JOBSEEKER="jobseeker"
    EMPLOYER="employer"


class User(AbstractUser):
    ROLE_CHOICES=[
        ( UserRole.JOBSEEKER.value, 'job Seeker'),
        ( UserRole.EMPLOYER.value, 'Employer'),
    ]


    username= None
    email= models.EmailField(unique=True)
    full_name= models.CharField(max_length=100, null=True)
    phone_number= models.CharField(max_length=15, null=True)
    roles= models.CharField(max_length=10, choices=ROLE_CHOICES, default="")
    is_verified= models.BooleanField(default= False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name']

    objects= CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.get_roles_display()})"
    



# Create your models her

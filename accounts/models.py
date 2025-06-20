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
    

class jobSeekerProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume/', null=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    education = models.TextField(blank=True, null=True)
    is_deleted= models.BooleanField(default=False)

    def __str__(self):
        return f"jobseekerProfile: {self.user.email}"

class employerProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, null=True)
    company_website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    is_deleted= models.BooleanField(default=False)

    def __str__(self):
        return f"employerProfile: {self.user.email}"

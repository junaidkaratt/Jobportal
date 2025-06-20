from django.contrib import admin
from .models import User, jobSeekerProfileModel, employerProfileModel

admin.site.register(User)

admin.site.register(jobSeekerProfileModel)

admin.site.register(employerProfileModel)
# Register your models here.

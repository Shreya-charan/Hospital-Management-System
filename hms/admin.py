from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Doctor,Patient,Department

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Doctor)
admin.site.register(Patient)

admin.site.register(Department)
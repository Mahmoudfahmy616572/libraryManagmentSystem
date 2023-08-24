from django.contrib import admin
from .models import profile , User
# Register your models here.

admin.site.register(profile)

# @admin.register(profile)
# class StudentAdmin(admin.ModelAdmin):
#     List_display = profile.DisplayFields

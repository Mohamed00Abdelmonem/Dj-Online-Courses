from django.contrib import admin
from .models import Profile
from unfold.admin import ModelAdmin

# Register your models here.


admin.site.register(Profile, ModelAdmin)

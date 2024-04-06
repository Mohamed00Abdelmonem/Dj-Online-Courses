from django.contrib import admin
from .models import Instructor_Profile, Student_Profile
# Register your models here.


admin.site.register(Instructor_Profile)
admin.site.register(Student_Profile)
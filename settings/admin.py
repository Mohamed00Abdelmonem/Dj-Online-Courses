from django.contrib import admin
from .models import Company
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class About_us(SummernoteModelAdmin):  
    summernote_fields = '__all__'

admin.site.register(Company, About_us)

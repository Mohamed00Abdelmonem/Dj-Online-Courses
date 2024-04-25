# settings.py
from .models import Company
from django.contrib.auth.models import User
def get_company_data(request):
    data = Company.objects.last()
    user = request.user
    return {'data': data, 'user':user}

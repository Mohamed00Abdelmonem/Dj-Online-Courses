# settings.py

def get_company_data(request):
    from .models import Company
    data = Company.objects.last()
    return {'data': data}

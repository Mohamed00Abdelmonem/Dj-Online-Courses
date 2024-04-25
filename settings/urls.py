from django.urls import path
from .views import home, generate_ollama3_text

app_name = 'settings'
urlpatterns = [
    path('', home),
    path('ai/', generate_ollama3_text, name='ai'),

]
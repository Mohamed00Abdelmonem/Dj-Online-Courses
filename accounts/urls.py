from django.urls import path
from .views import signup, activate, InstractorList
app_name = 'accounts'

urlpatterns = [
    path('signup', signup),
    path('<str:username>/activate', activate),
    path('instractors', InstractorList.as_view(), name = 'instractor'),

]
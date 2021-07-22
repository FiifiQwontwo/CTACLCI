from django.urls import path
from .views import *

app_name = 'contact'

urlpatterns = [
    path('on_contact/', contact_view, name='contact_us'),
    path('sux/', success_view, name='success_page'),
]

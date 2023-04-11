from django.urls import path
from .views import *

urlpatterns = [
    path('', tasklist, name='home'),
]

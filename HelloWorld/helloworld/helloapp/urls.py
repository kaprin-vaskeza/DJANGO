# pages/urls.py
from django.urls import path

from .views import hello_view , name_view

urlpatterns = [
    path('hello', hello_view, name='hello'),
    path('name', name_view, name='name'),
]
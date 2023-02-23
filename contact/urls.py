from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUS.as_view(), name='contact'),
    path('', views.AboutUS.as_view(), name='About'),
]
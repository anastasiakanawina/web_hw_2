from django.contrib import admin
from django.urls import path, include

from catalog.views import index, home, contacts

urlpatterns = {
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
}
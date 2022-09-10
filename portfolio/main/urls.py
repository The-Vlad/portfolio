from django.contrib import admin
from django.urls import path
from . import views as view

urlpatterns = [
    path('about/', view.about),
    path('index/', view.index)
]

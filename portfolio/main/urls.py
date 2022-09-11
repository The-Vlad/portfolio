from django.contrib import admin
from django.urls import path
from . import views as view


app_name = "main"
urlpatterns = [
    path('about/', view.about, name='about'),
    path('', view.index, name='home'),
    path('<str:page>/', view.other_page, name='member'),
]

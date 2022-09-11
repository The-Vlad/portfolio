from django.contrib import admin
from django.urls import path
from . import views as view
from .views import other_page


urlpatterns = [
    path('about/', view.about),
    path('', view.index),
    path('<str:page>/', view.other_page, name='member')
]

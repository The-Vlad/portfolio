from django.urls import path
from . import views as view

urlpatterns = [
    path('about/', view.about),
    path('', view.index),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('vista2/',views.vista2),
]
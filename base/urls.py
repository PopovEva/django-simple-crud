from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test/',views.test),
    path('cars/',views.cars),
    path('cars/<int:id>/',views.cars)
]



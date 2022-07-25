from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.crear_familiares, name='Formulario'),
]

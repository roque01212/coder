from django.urls import path
from . import views

app_name='familia_app'

urlpatterns = [
    path('formulario/', views.FamiliaCreateView.as_view(), name='Formulario'),
    path('lista/', views.FamiliaListView.as_view(), name='ListaFamiliares'),
    path('delete/<pk>/', views.FamiliaDeleteView.as_view(), name='Delete'),
    path('update/<pk>/', views.FamiliaUpdateView.as_view(), name='Update'),
]

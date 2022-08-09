from django.urls import path
from . import views

app_name='familia_app'

urlpatterns = [
    path('', views.inicio, name='Index'),
    path('formulario/', views.FamiliaCreateView.as_view(), name='Formulario'),
    path('lista/', views.FamiliaListView.as_view(), name='ListaFamiliares'),
    path('delete/<pk>/', views.FamiliaDeleteView.as_view(), name='Delete'),
    path('update/<pk>/', views.FamiliaUpdateView.as_view(), name='Update'),
    path('buscar/', views.buscar, name='Buscar'),
    path("busquedanombre/", views.buscar_familia, name="Buscarnombre"),
    


    path('zapas/', views.ZapasreateView.as_view(), name='Zapas'),
    path('listado-zapa/', views.mostrar_zapatillas, name='Listado-zapas'),
    path('update-zapas/<pk>/', views.ZapasUpdateView.as_view(), name='Update-zapas'),
    path('delete-zapas/<id>/', views.eliminar_zapas, name='Delete-zapas'),

    path('listar/',views.MascotasListView.as_view(),name='ListaMascotas'),
    path('crear/', views.MascotaCreateView.as_view(), name='CrearMascota'),
    path('delete-mascota/<pk>/', views.MascotaDeleteView.as_view(), name='Delete-mascota'),
    path('update-mascota/<pk>/', views.MascotaUpdateView.as_view(), name='Update-mascota')

]

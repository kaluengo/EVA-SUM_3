from django.urls import path
from . import views 


urlpatterns = [
    
    path('', views.home ,name='home'),
    
    path('mascotas/', views.mascotas,name='mascota'),
    path('contacto/', views.contacto,name='contacto'),
    path('registrarMascota/', views.registrarMascota),
    path('edicionMascota/<codigo>', views.edicionMascota),
    path('editarMascota/<codigo> ', views.editarMascota),
    path('eliminacionMascota/<codigo>', views.eliminacionMascota),
    path('agregarArticulo/', views.Add_Articulo),
    path('edicionArticulo/<codigo>', views.Edicion_Articulo),
    path('editarArticulo/', views.Edit_Articulo),
    path('eliminarArticulo/<codigo>', views.Del_Articulo),
    path('consumo/', views.consumoApi,name='consumoApi'),
    path('logout/', views.logout_request, name="logout")
    
    
 
]

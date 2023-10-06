from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path ('', index, name = 'index'),
    path ('categoria/', categoria, name='categoria'),
    path ('cliente/', cliente, name='cliente'),
    path ('producto/',producto, name='producto'),
    path('formulario-producto/',formProducto,name="formularioProducto"),
    path('formulario-categoria/',formCategoria,name="formularioCategoria"),
    path('formulario-cliente/',formCliente,name="formularioCliente"),
    path('lista-productos',listar_productos,name="ListaProductos"),
    path('busqueda-producto/',busquedaProducto,name="BusquedaProducto"),
    path('buscar/',buscar,name="Buscar"),
]
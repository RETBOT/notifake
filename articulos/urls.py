# by: RETBOT 
# articulos/url.py
from django.urls import path
from .views import (
    VistaListaArticulos,
    VistaEditarArticulo,
    VistaDetalleArticulo,
    VistaEliminarArticulo,
    VistaCrearArticulo,
    )
# by: RETBOT 
urlpatterns = [
    path('',VistaListaArticulos.as_view(), name='lista_articulos'),
    path('<int:pk>/editar/',VistaEditarArticulo.as_view(), name='editar_articulos'),
    path('<int:pk>/detalle/',VistaDetalleArticulo.as_view(), name='detalle_articulo'),
    path('<int:pk>/eliminar/',VistaEliminarArticulo.as_view(), name='eliminar_articulo'),
    path('nuevo/',VistaCrearArticulo.as_view(), name='nuevo_articulo')
]
# by: RETBOT 

from django.urls import path
from apps.anuncio.views import index, AnuncioCreate, AnuncioUpdate, AnuncioDelete, AnuncioDetail, anuncios_search, anuncios_usuario
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'anuncio'
urlpatterns = [
    path('listar/', anuncios_search, name='anuncio_listar'),
    path('listar/usuario', anuncios_usuario, name='anuncio_usuario'),
    path('crear/', login_required(AnuncioCreate.as_view()), name='anuncio_crear'),
    path('editar/<pk>/', AnuncioUpdate.as_view(), name='anuncio_editar'),
    path('eliminar/<pk>/', AnuncioDelete.as_view(), name='anuncio_delete'),
    path('detalles/<pk>/', AnuncioDetail.as_view(), name='anuncio_detalles'),
]

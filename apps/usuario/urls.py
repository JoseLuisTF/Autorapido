from django.urls import path
from apps.usuario.views import create_user_view

app_name = 'usuario'
urlpatterns = [
    path('registrarse/', create_user_view, name='registro' ),

]

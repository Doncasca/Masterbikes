from unicodedata import name
from django.urls import path
from aplicacion.views import crear, eliminar, home, modificar, mantencion

urlpatterns = [
    path('',home,name="home"),
    path('mantencion/',mantencion,name="mantencion"),
    path('crear/',crear,name="crear"),
    path('modificar/<id>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar,name="eliminar")
]
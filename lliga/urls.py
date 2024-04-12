from django.contrib import admin
from django.urls import include, path

from lliga import views

urlpatterns = [
    path("menu", views.menu, name="menu"),
    path("menuEquip", views.menuEquip, name="menuEquip"),
    path("crearLliga", views.crearLliga, name="crearLliga"),
    path("crearEquip", views.crearEquip, name="crearEquip"),
    path("editarEquipos", views.editarEquipos, name="editarEquipos"),
    path("classificacio/<int:lliga_id>", views.classificacio, name="classificacio")
]
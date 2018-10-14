from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("add_address", views.add_address,name="address"),
    path("addresses", views.addresses,name="addresses"),
    path('edit/<list_id>', views.edit ,name = "edit"),

]

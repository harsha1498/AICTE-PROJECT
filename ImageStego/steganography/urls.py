from django.urls import path
from .views import home_view, encrypt_image_view, decrypt_image_view

urlpatterns = [
    path("", home_view, name="home"),  # Home page
    path("encrypt/", encrypt_image_view, name="encrypt_image"),
    path("decrypt/", decrypt_image_view, name="decrypt_image"),
]

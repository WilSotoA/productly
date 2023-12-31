from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.detail, name="detail"),
    path("form", views.form, name="create"),
]

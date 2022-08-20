from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detect", views.cam, name="detect"),
    path("records", views.records, name="records")
]

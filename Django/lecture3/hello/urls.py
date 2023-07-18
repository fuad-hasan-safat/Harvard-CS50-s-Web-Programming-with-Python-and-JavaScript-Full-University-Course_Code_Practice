
from django.urls import path

from . import views # dot(.) reffers current directory


urlpatterns = [
    path("", views.index, name="index"),
    path("hasan", views.hasan, name="hasan"),
    path("safat", views.safat, name="safat")
]
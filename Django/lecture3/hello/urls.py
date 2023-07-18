
from django.urls import path

from . import views # dot(.) reffers current directory


urlpatterns = [
    path("", views.index, name="index")
]
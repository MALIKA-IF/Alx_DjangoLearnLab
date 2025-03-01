from django.urls import path
from . import views
from .views import index, Details

urlpatterns = [
    path("", index, name="index"),
    path("",Details.as_view(),name="details")


]
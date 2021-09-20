from django.urls import path
from . import views

urlpatterns = [
    path("",views.ImpDateCreate.as_view(),name="add_dates"),
]

from django.urls import path
from . import views

urlpatterns = [
path("hadith/", views.HadithListCreate.as_view(), name = "hadith-list-create"),
path("hadith/<int:pk>/" , views.HadithRetrieveUpdateDestroy.as_view(), name = "retupdey")
]

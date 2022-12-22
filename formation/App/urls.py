from django.urls import path
#from App.views import index
from App.views import *
urlpatterns = [
  #  path("route/",fonction,name)
  path ("i/",index),
  path("ii/<str:up>",home),
  path('Affiche/',Affiche,name="Aff"),
  path('AfficheProjet/',AfficheProjet.as_view(),name="aff_projet"),
  path('DeleteProjet/<int:pk>',DeleteProjet.as_view(),name="delete_projet"),
  path('AjoutProjet/',AjoutProjet.as_view(),name="add_projet"),
  path('UpdateProjet/<int:pk>',UpdateProjet.as_view(),name="update_projet")
]

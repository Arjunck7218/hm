from django.urls import path
from . import views
app_name='patients'
urlpatterns=[
path('addpatiants/',views.registerpatiants,name="addpatiants"),
path('master/',views.getmaster,name="master"),
path('home/',views.gethome,name="home"),
path('contact/',views.getcontact,name="contact"),
path('aboutas/',views.getaboutas,name="aboutas")
]
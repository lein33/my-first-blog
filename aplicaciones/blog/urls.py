from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$',home, name = 'index'),
    url(r'^generales/$',generales, name = 'generales'),
    url(r'^programacion/$',programacion, name = 'programacion'),
    url(r'^tecnologia/$',tecnologia, name = 'tecnologia'),
    url(r'^tutoriales/$',tutoriales, name = 'tutoriales'),
    url(r'^videojuegos/$',videojuegos, name = 'videojuegos'),
    url(r'^(?P<slug>\w+)',detallePost, name = 'detalle_post'),
]

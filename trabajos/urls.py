from django.urls import path
from trabajos.views import Mensura, Estadoparcelario, Relevamiento, Amojonamiento, Replanteo, PropiedadHorizontal, Unificacion, Loteo, Usucapion, BarrioCerradoClub

urlpatterns = [
    path('mensura/', Mensura, name='mensura'),
    path('estado-parcelario/', Estadoparcelario, name='estado-parcelario'),
    path('relevamiento/', Relevamiento, name='relevamiento'),
    path('amojonamiento/', Amojonamiento, name='amojonamiento'),
    path('replanteo/', Replanteo, name='replanteo'),
    path('propiedad-horizontal/', PropiedadHorizontal, name='propiedad-horizontal'),
    path('unificacion/', Unificacion, name='unificacion'),
    path('loteo/', Loteo, name='loteo'),
    path('usucapion/', Usucapion, name='usucapion'),
    path('barrio-cerrado-club-campo/', BarrioCerradoClub, name='barrio-cerrado-club'),
]
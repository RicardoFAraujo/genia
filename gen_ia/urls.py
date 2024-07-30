from django.urls import path
from gen_ia.views import genia, cadastro


urlpatterns = [
   path('genia', genia, name='genia'),
   path('cadastro', cadastro, name='cadastro'),
]
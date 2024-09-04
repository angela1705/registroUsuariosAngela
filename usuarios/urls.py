from django.urls import path
from .views import listar_personas, crear_persona

urlpatterns = [
    path ("",listar_personas,name='listar_personas'),
    path('crear/',crear_persona,name='crear_persona')
]

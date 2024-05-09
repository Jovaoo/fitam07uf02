from django.urls import path
from .views import lista_automoviles

urlpatterns = [
    path('automoviles/', lista_automoviles, name='lista_automoviles'),
]
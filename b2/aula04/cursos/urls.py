from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sair/', views.sair, name='sair'),
    path('curso/<int:id>', views.curso, name = 'curso'),
    path('aula/<int:id>', views.aula, name = 'aula'),
]
from django.urls import path
from publico import views


urlpatterns = [
 
    path('geral/', views.geral, name='geral')

]


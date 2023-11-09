from django.urls import path
from django.http import HttpResponse
from .models import Promotor, Festival, Interprete
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('promotores/', views.index_promotores, name='indexPromotor'),
    path('promotores/<int:promotor_id>/', views.show_promotores, name='promotorDetail'), 
    path('festivales/', views.index_festivales, name='festivales'),
    path('festivales/<int:festival_id>/', views.show_festivales, name='festivalDetail'), 
    path('interpretes/', views.index_interpretes, name='interpretes'),
    path('interpretes/<int:interprete_id>/', views.show_interpretes, name='interpreteDetail'), 
    #""" path('actuaciones/', views.index_actuaciones, name='actuaciones'),
    #path('actuaciones/<int:actuacion_id>/', views.show_actuacion, name='actuacion_detail'),  """
]
from django.urls import path
from django.http import HttpResponse
from .models import Promotor, Festival, Interprete, Actuacion
from . import views

urlpatterns = [
    path('', views.index_festivales, name='index'),
    path('promotores/', views.index_promotores, name='indexPromotor'),
    #path('promotores/<int:promotor_id>/', views.show_promotor, name='promotor_detail'), 
    #path('festivales/', views.index_festivales, name='festivales'),
    #path('festivales/<int:festival_id>/', views.show_festival, name='festival_detail'), 
    #path('interpretes/', views.index_interpretes, name='interpretes'),
    #path('interpretes/<int:interprete_id>/', views.show_interprete, name='interprete_detail'), 
    #""" path('actuaciones/', views.index_actuaciones, name='actuaciones'),
    #path('actuaciones/<int:actuacion_id>/', views.show_actuacion, name='actuacion_detail'),  """
]
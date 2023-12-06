from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('promotores/', views.index_promotores, name='indexPromotor'),
    path('promotores/<int:promotor_id>/', views.show_promotores, name='promotorDetail'), 
    path('festivales/', views.index_festivales, name='festivales'),
    path('festivales/<int:festival_id>/', views.show_festivales, name='festivalDetail'), 
    path('interpretes/', views.index_interpretes, name='interpretes'),
    path('interpretes/<int:interprete_id>/', views.show_interpretes, name='interpreteDetail'), 
    path('formularioInterprete/', views.add_interprete, name='addInterprete'),
    path('formularioFestival/', views.add_festival, name='addFestival'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

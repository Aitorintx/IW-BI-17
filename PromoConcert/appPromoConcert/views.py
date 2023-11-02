from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Promotor, Festival, Interprete, Actuacion

def index_promotores(request):
    promotores = get_list_or_404(Promotor.objects.all())
    output = ', '.join([promotor.namePromotor for promotor in promotores])
    return HttpResponse(output)

def show_promotor(request, promotor_id):
    promotor = get_object_or_404(Promotor, pk=promotor_id)
    output = f'Detalles del promotor: {promotor.idPromotor}, {promotor.namePromotor}, {promotor.infoPromotor}'
    return HttpResponse(output)

def index_festivales(request):
    festivales = get_list_or_404(Festival.objects.all())
    output = ', '.join([festival.nombreFestival for festival in festivales])
    return HttpResponse(output)

def show_festival(request, festival_id):
    festival = get_object_or_404(Festival, pk=festival_id)
    output = f'Detalles del festival: {festival.idFestival}, {festival.nombreFestival}, {festival.infoFestival}, {festival.fecha}, Promotor: {festival.idPromotor.namePromotor}'
    return HttpResponse(output)

def index_interpretes(request):
    interpretes = get_list_or_404(Interprete.objects.all())
    output = ', '.join([interprete.nameInterprete for interprete in interpretes])
    return HttpResponse(output)

def show_interprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, pk=interprete_id)
    output = f'Detalles del intérprete: {interprete.idInterprete}, {interprete.nameInterprete}, {interprete.infoInteprete}'
    return HttpResponse(output)

def index_actuaciones(request):
    actuacion = get_list_or_404(Actuacion.objects.all())
    output = ', '.join([str(Actuacion.idActuacion) for actuation in actuacion])
    return HttpResponse(output)

def show_actuacion(request, actuacion_id):
    actuacion = get_object_or_404(Actuacion, pk=actuacion_id)
    output = f'Detalles de la actuación: {actuacion.idActuacion}, Intérprete: {actuacion.idInterprete.nameInterprete}, Festival: {actuacion.idFestival.nombreFestival}'
    return HttpResponse(output)

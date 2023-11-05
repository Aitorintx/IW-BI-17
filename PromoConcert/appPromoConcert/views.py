from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Promotor, Festival, Interprete, Actuacion

def index_promotores(request):
    promotores = get_list_or_404(Promotor.objects.all())
    output = ', '.join([promotor.namePromotor for promotor in promotores])
    return HttpResponse(request, 'indexPromotor.html', {'output': output})

def show_promotor(request, promotor_id):
    promotor = get_object_or_404(Promotor, pk=promotor_id)

    festivalesPropios = Festival.objects.filter(idPromotor=promotor_id)          # Actuaciones del festival
    festivales = []

    for festival in festivalesPropios:
        festivalHecho = get_list_or_404(Festival, pk=festival.idFestival)       #Interpretes que aparezcan
        festivales.append(festivalHecho.nameFestival)            # Nombres de los intérpretes

    output = f'Detalles del promotor: {promotor.idPromotor}, {promotor.namePromotor}, {promotor.infoPromotor} \n Festivales: '
    
    if festivales:
        for fest in festivales:
            output += '\n' + (fest)
    
    return HttpResponse(request, 'promotorDetail.html', output)

def index_festivales(request):
    festivales = get_list_or_404(Festival.objects.all())
    output = ', '.join([festival.nombreFestival for festival in festivales])
    return HttpResponse(request, 'indexFestivales.html', {'output': output})

def show_festival(request, festival_id):
    festival = get_object_or_404(Festival, pk=festival_id)

    actuaciones = Actuacion.objects.filter(idFestival=festival_id)          # Actuaciones del festival
    interpretes = []

    for actuacion in actuaciones:
        interprete = get_list_or_404(Interprete, pk=actuacion.idInterprete)       #Interpretes que aparezcan
        interpretes.append(interprete.nameInterprete)            # Nombres de los intérpretes

    output = f'Detalles del festival: {festival.idFestival}, {festival.nombreFestival}, {festival.infoFestival}, {festival.fecha}, Promotor: {festival.idPromotor.namePromotor}. \n Interpretes: '

    if interpretes:
        for interprete in interpretes:
            output += '\n' + (interprete)
    
    return HttpResponse(request, 'festivalDetail.html', output)

def index_interpretes(request):
    interpretes = get_list_or_404(Interprete.objects.all())
    output = ', '.join([interprete.nameInterprete for interprete in interpretes])
    return HttpResponse(request, 'indexInterpretes.html', {'output': output})

def show_interprete(request, interprete_id):
    interprete = get_list_or_404(Interprete, pk=interprete_id)

    actuaciones = Actuacion.objects.filter(idInterprete=interprete_id)          # Actuaciones del festival
    festivales = []

    for actuacion in actuaciones:
        festival = get_object_or_404(Festival, pk=actuacion.idFestival)       #Interpretes que aparezcan
        festivales.append(festival.nameFestival)            # Nombres de los intérpretes

    output = f'Detalles del intérprete: {interprete.idInterprete}, {interprete.nameInterprete}, {interprete.infoInteprete} \n Actuaciones: '
    
    if festivales:
        for festival in festivales:
            output += '\n' + (festival)
    
    return HttpResponse(request, 'interpreteDetail.html', output)

""" 
def index_actuaciones(request):
    actuacion = get_list_or_404(Actuacion.objects.all())
    output = ', '.join([str(Actuacion.idActuacion) for actuation in actuacion])
    return HttpResponse(output)

def show_actuacion(request, actuacion_id):
    actuacion = get_object_or_404(Actuacion, pk=actuacion_id)
    output = f'Detalles de la actuación: {actuacion.idActuacion}, Intérprete: {actuacion.idInterprete.nameInterprete}, Festival: {actuacion.idFestival.nombreFestival}'
    return HttpResponse(output)
 """
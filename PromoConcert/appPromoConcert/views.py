from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Promotor, Festival, Interprete
from django.shortcuts import render

#def appPromoConcert_view(request):
#    # Your view logic goes here
#    promotores = get_list_or_404(Promotor.objects.all())
#    output = ', '.join([promotor.namePromotor for promotor in promotores])
#    return render(request, 'appPromoConcert/template_name.html', output)

def index(request):
	promotores = get_list_or_404(Promotor.objects.order_by('namePromotor'))
	context = {'lista_promotores': promotores }
	return HttpResponse(render(request, 'index.html', {'output': context}), content_type='text/html', status=200)


def index_promotores(request):
    promotores = get_list_or_404(Promotor.objects.all())
    output = {'lista_promotores': promotores}
    return render(request, 'indexPromotor.html', output)


def show_promotores(request, promotor_id):
    promotor = get_object_or_404(Promotor, pk=promotor_id)
    contexto = {'promotor' : promotor}
    return render(request, 'promotorDetail.html', contexto)


def index_festivales(request):
    festivales = get_list_or_404(Festival.objects.all())
    output = {'lista_festivales': festivales}
    return render(request, 'indexFestivales.html', output)


def show_festivales(request, festival_id):
    festival = get_object_or_404(Festival, pk=festival_id)
    contexto = {'festival' : festival}
    return render(request, 'festivalDetail.html', contexto)


def index_interpretes(request):
    interpretes = get_list_or_404(Interprete.objects.all())
    output = {'lista_interpretes': interpretes}
    return render(request, 'indexInterpretes.html', output)


def show_interpretes(request, interprete_id):
    interprete = get_object_or_404(Interprete, pk=interprete_id)
    contexto = {'interprete' : interprete}
    return render(request, 'interpreteDetail.html', contexto)



""" def show_festival(request, festival_id):
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
    
    return HttpResponse(request, 'interpreteDetail.html', output) """

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
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Promotor, Festival, Interprete
from django.shortcuts import render, redirect
from .forms import InterpreteForm, FestivalForm

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


def add_interprete(request):
    if request.method == 'POST':
        form = InterpreteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexInterpretes') 
    else:
        form = InterpreteForm()
    return render(request, 'formularioInterprete.html', {'form': form})

def add_festival(request):
    if request.method == 'POST':
        form = FestivalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexFestivales')
    else:
        form = FestivalForm()

    return render(request, 'formularioFestival.html', {'form': form})


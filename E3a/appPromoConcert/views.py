from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView
from .models import Promotor, Festival, Interprete
from django.shortcuts import render, redirect
from .forms import InterpreteForm, FestivalForm
from django.views import View
from .models import Contacto
from .forms import ContactoForm, CustomAuthenticationForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages



def index(request):
	promotoresFiltrados = Festival.objects.raw('SELECT * FROM( SELECT * FROM appPromoConcert_Festival ORDER BY nombreFestival DESC) GROUP BY promotor_id ')
	context = {'lista_promotores': promotoresFiltrados }
	return render(request, 'index.html', context)


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
            return redirect('interpretes') 
    else:
        form = InterpreteForm()
    return render(request, 'formularioInterprete.html', {'form': form})

def add_festival(request):
    if request.method == 'POST':
        form = FestivalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('festivales')
    else:
        form = FestivalForm()

    return render(request, 'formularioFestival.html', {'form': form})

def loginF(request):
    if request.method == 'POST':
        promotores = get_list_or_404(Promotor.objects.all())
        authorized_usernames = [promotor.namePromotor for promotor in promotores]

        entered_username = request.POST.get('username', '')  # Get the entered username from the form
        if entered_username in authorized_usernames:
            # Username matches one of the names in the Promotor objects
            # Perform actions for a successful match, for example, setting a session variable
            request.session['authenticated'] = True
            return redirect('addFestival')
        else:
            # Username doesn't match any name in the Promotor objects
            # Handle authentication failure, for example, show an error message
            pass

    return render(request, 'loginF.html')


def loginI(request):
    if request.method == 'POST':
        promotores = get_list_or_404(Promotor.objects.all())
        authorized_usernames = [promotor.namePromotor for promotor in promotores]

        entered_username = request.POST.get('username', '')  # Get the entered username from the form
        if entered_username in authorized_usernames:
            # Username matches one of the names in the Promotor objects
            # Perform actions for a successful match, for example, setting a session variable
            request.session['authenticated'] = True
            return redirect('addInterprete')
        else:
            # Username doesn't match any name in the Promotor objects
            # Handle authentication failure, for example, show an error message
            pass

    return render(request, 'loginI.html')


class PromotoresList(ListView):
    model = Promotor
    template_name = 'indexPromotor.html'
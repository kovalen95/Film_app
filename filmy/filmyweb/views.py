from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm
from . models import Film, Ocena, DodatkoweInfo
from django.contrib.auth.decorators import login_required




def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    ocena = Ocena.objects.all()
    # id1film = Film.objects.filter(id=1)
    # id1film = Film.objects.get(id=1)
    return render(request, 'filmyweb/filmy.html', {'filmy': wszystkie})

@login_required
def nowy_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False) # commit = False czy zapisujemy w pamieci a nie jeszcze w bazie danych
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe # pole dodatkowe dla modelu film
        film.save()
        return redirect(wszystkie_filmy)
    return render(request, 'filmyweb/film_form.html', {'form': form_film, 'form_dodatkowe':form_dodatkowe, 'nowy': True})

@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    oceny = Ocena.objects.filter(film=film)


    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    form_ocena = OcenaForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)  # commit = False czy zapisujemy w pamieci a nie jeszcze w bazie danych
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe  # pole dodatkowe dla modelu film
        film.save()
        return redirect(wszystkie_filmy)
    return render(request, 'filmyweb/film_form.html', {'form': form_film, 'form_dodatkowe': form_dodatkowe, 'oceny': oceny, 'nowy': False})


@login_required
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'filmyweb/potwierdz.html', {'film': film})

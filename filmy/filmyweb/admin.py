from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor


# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"] # wybieramy pola ktore maja byc widoczne w adminie
    # exclude = ["opis"] # ktore pole ma byc nie pokazywane
    list_display = ["tytul", "imdb_rating", "rok"] # widok ze jest tytul i obok w filmach rozne pola
    list_filter = ("rok",) # filtrujemy pod wzgledem roku filmy, wyswietla sie filtr po prawej
    search_fields = ("tytul","opis") # szuka slow w opisie i w filmie

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)
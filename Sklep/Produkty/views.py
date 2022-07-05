from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria
from django.shortcuts import render

def index(request):
    zapytanie = Produkty.objects.all()
    produkt   = Produkty.objects.get(pk=2)
    kategoria = Kategoria.objects.all()
    dane = {'kategoria': kategoria}
    return render(request, "szablon.html", dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {
        'kategoria_user': kategoria_user,
        'kategoria_produkt': kategoria_produkt,
        'kategorie': kategorie
    }
    return render(request, 'kategoria_produkt.html', dane)


def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategoria = Kategoria.objects.all()
    dane = {'produkt_user' : produkt_user, 'kategoria': kategoria}
    return render(request, 'produkt.html', dane)
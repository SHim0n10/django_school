from django.shortcuts import render, HttpResponse
from . models import *

def vypis_shop(request):
    kategorie = Kategoria.objects.all().order_by("nazov")
    produkty = Produkt.objects.all().order_by("nazov")
    uzivatelia = Uzivatelia.objects.all().order_by("meno")
    return render(request, "shop/index.html", {"kategorie":kategorie, "produkty":produkty, "uzivatelia":uzivatelia})

def vypis_kategorie(request):
    kategorie = Kategoria.objects.all().order_by("nazov")
    return render(request, "shop/index.html", {"kategorie":kategorie})

def vypis_produkty(request):
    produkty = Produkt.objects.all().order_by("nazov")
    return render(request, "shop/index.html", {"produkty":produkty})

def vypis_uzivatelov(request):
    uzivatelia = Uzivatelia.objects.all().order_by("meno")
    return render(request, "shop/index.html", {"uzivatelia":uzivatelia})

def vypis_objednavky(request):
    objednavky = Objednavka.objects.all().order_by("id_objednavky")
    return render(request, "shop/index.html", {"objednavky":objednavky})
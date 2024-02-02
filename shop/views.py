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

def vypis_kategoriu(request, kategoria):
    kategoria = Kategoria.objects.get(nazov=kategoria)
    produkty = Produkt.objects.filter(kategoria_id=kategoria.pk).order_by("nazov")
    produkt_list = []
    for produkt in produkty:
        produkt_list.append(produkt)
    #return HttpResponse(f"{trieda}<br>{ucitel}<br>{studenti_list}")
    return render(request, "shop/kategoria.html", {"produkty":produkt_list, "kategoria":kategoria})

def vypis_produkt(request, produkt):
    produkt = Produkt.objects.get(product_id=produkt)
    return render(request, "shop/produkt.html", {"produkt":produkt})
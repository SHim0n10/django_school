from django.shortcuts import render, HttpResponse
from . models import *

def vypis_blog(request):
    posty = Post.objects.all().order_by("cas")
    return render(request, "blog/index.html", {"posty":posty})

def vypis_kategorie(request):
    kategorie = Kategoria.objects.all().order_by("nazov")
    return render(request, "blog/index.html", {"kategorie":kategorie})

def vypis_uzivatelov(request):
    uzivatelia = Uzivatel.objects.all().order_by("nick")
    return render(request, "blog/index.html", {"uzivatelia":uzivatelia})

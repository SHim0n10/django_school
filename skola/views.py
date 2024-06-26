from django.shortcuts import render, HttpResponse
from . models import *
from . forms import *

def vypis_skola(request):
    triedy = Trieda.objects.all().order_by("nazov")
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti})

def vypis_studenti(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"studenti":studenti})

def vypis_student(request, student):
    student = Student.objects.get(id=student)
    trieda = Trieda.objects.get(id=student.trieda_id)
    ucitel = Ucitel.objects.get(trieda_id=trieda.id)
    return render(request, "skola/student_detail.html", {"student":student, "ucitel":ucitel, "trieda":trieda})


def vypis_triedy(request):
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy})

def vypis_ucitelia(request):
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"ucitelia":ucitelia})

def vypis_ucitel(request, ucitel):
    ucitel = Ucitel.objects.get(id=ucitel)
    try: 
        kruzok = Kruzok.objects.get(ucitel=ucitel.pk)
    except:
        kruzok = ""
    if ucitel.trieda:
        trieda = Trieda.objects.get(id=ucitel.trieda_id).nazov
        if kruzok:
            return render(request, "skola/ucitel_detail.html", {"ucitel":ucitel, "trieda":trieda, "kruzok":kruzok})
        return render(request, "skola/ucitel_detail.html", {"ucitel":ucitel, "trieda":trieda})
    if kruzok:
        return render(request, "skola/ucitel_detail.html", {"ucitel":ucitel, "kruzok":kruzok})
    return render(request, "skola/ucitel_detail.html", {"ucitel":ucitel})

def vypis_trieda(request, trieda):
    trieda_obj = Trieda.objects.get(nazov=trieda)
    studenti = Student.objects.filter(trieda_id=trieda_obj.pk).order_by("priezvisko")
    studenti_list = []
    for student in studenti:
        studenti_list.append(student)
    ucitel = Ucitel.objects.get(trieda_id=trieda_obj.pk)
    #return HttpResponse(f"{trieda}<br>{ucitel}<br>{studenti_list}")
    return render(request, "skola/trieda_list.html", {"trieda":trieda, "ucitel":ucitel, "studenti":studenti_list})

def vypis_kruzky(request):
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/kruzky.html", {"kruzky":kruzky})

def vypis_kruzok(request, kruzok):
    kruzok_obj = Kruzok.objects.get(skratka=kruzok)
    ucitel = Ucitel.objects.get(id=kruzok_obj.ucitel_id)
    # studenti
    studenti = Student.objects.filter(kruzok=kruzok_obj.pk).order_by("priezvisko")
    

    return render(request, "skola/kruzok_detail.html", {"kruzok":kruzok_obj, "ucitel":ucitel, "studenti":studenti})


def pridat_uzivatel(request):
    if request.method == "GET":
        return render(request, "skola/pridat_uzivatel.html")
    else:
        uzivatel = Uzivatel(
            meno = request.POST["meno"],
            priezvisko = request.POST["priezvisko"],
            email = request.POST["email"],
            datum = request.POST["datum"]
        )
        uzivatel.save()
        return HttpResponse("OK")
    
def pridat_uzivatel2(request):
    if request.method == "GET":
        form = UzivatelForm()
    else:
        form = UzivatelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
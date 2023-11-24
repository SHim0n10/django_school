from django.shortcuts import render, HttpResponse
from . models import *

def vypis_student():
    studenti = Student.objects.all()
    return HttpResponse(studenti)

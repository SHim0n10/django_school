from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello</h1>")

def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")

def slovo(request, slovo):
    return HttpResponse(f"<h1>Hello {slovo}</h1>")
import random
import django
import os
from datetime import date
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *
"""
f = open("ULICE1.txt", "r")
lines = f.readlines()

studenti = Ucitel.objects.all()

for i in studenti:
    print(i.pk)
    random_line = random.choice(lines)
    ulica, psc, obec = random_line.split(";")
    i.ulica = f'{ulica} {random.randint(1,2000)}'
    i.psc = f'{psc}'
    i.obec = f'{obec}'
    i.save()
"""
studenti = Student.objects.all()


today = date.today()

for i in studenti:
    trieda = i.trieda.nazov
    if trieda[0] == "1":
        start_date = date(today.year - 16, 1, 1)
        end_date = date(today.year - 16, 12, 31)
    elif trieda[0] == "2":
        start_date = date(today.year - 17, 1, 1)
        end_date = date(today.year - 17, 12, 31)
    elif trieda[0] == "3":
        start_date = date(today.year - 18, 1, 1)
        end_date = date(today.year - 18, 12, 31)
    elif trieda[0] == "4":
        start_date = date(today.year - 19, 1, 1)
        end_date = date(today.year - 19, 12, 31)

    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + timedelta(days=rand_days)
    


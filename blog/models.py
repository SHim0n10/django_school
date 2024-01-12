from django.db import models

class Kategoria(models.Model):
    nazov = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.nazov}"

class Uzivatel(models.Model):
    nick = models.CharField(max_length=50)
    meno = models.CharField(max_length=50)
    priezvisko = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nick}"

class Post(models.Model):
    nazov = models.CharField(max_length=50)
    cas = models.DateTimeField(auto_now=False, auto_now_add=False)
    autor = models.ForeignKey(Uzivatel, on_delete=models.SET_NULL, null=True, blank=True)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
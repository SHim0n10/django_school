from django.db import models

class Kategoria(models.Model):
    nazov = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.nazov}"

class Produkt(models.Model):
    nazov = models.CharField(max_length=20)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    popis = models.TextField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.SET_NULL, null=True, blank=True)
    product_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.product_id}"
    
class Uzivatelia(models.Model):
    meno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    zostatok = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.meno} {self.zostatok}"
    
class Objednavka(models.Model):
    id_objednavky = models.CharField(max_length=30)
    product = models.ForeignKey(Produkt, on_delete=models.SET_NULL, null=True, blank=True)
    uzivatel = models.ForeignKey(Uzivatelia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.product.nazov} {self.product.cena} {self.uzivatel.meno}"
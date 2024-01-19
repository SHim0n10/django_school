# Generated by Django 4.2.7 on 2023-12-15 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_produkt_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uzivatelia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meno', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('zostatok', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Objednavka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_objednavky', models.CharField(max_length=30)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.produkt')),
            ],
        ),
    ]
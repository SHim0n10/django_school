# Generated by Django 4.2.7 on 2024-04-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0008_ucitel_narodenie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucitel',
            name='narodenie',
            field=models.DateField(blank=True, null=True),
        ),
    ]
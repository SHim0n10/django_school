# Generated by Django 4.2.7 on 2024-01-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nazov',
            field=models.CharField(default='nazov', max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='numero_medecin',
            field=models.CharField(default='+226', max_length=16, verbose_name='numero medecine'),
        ),
    ]

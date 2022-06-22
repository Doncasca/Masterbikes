# Generated by Django 4.0.5 on 2022-06-22 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0017_alter_bicicleta_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='llegada',
            field=models.DateField(default=datetime.date.today, verbose_name='Dia de llegada (dd/mm/yyyy)'),
        ),
    ]
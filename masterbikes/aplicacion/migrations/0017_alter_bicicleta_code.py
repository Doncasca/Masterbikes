# Generated by Django 4.0.5 on 2022-06-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0016_alter_modelo_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='code',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]

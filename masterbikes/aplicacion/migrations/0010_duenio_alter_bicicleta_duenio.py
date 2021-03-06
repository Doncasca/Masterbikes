# Generated by Django 4.0.4 on 2022-06-07 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_delete_duenio_alter_bicicleta_duenio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duenio', models.CharField(max_length=50, verbose_name='Dueño')),
            ],
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='duenio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.duenio'),
        ),
    ]

# Generated by Django 4.2 on 2024-05-06 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='propietario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]

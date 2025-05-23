# Generated by Django 5.1.6 on 2025-05-04 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HosteriaSol', '0042_rename_email_empleado_correo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='num_per',
            new_name='adultos',
        ),
        migrations.AddField(
            model_name='detallereserva',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk03_idServicio', to='HosteriaSol.servicio'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='ninos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.DeleteModel(
            name='DetalleServicio',
        ),
    ]

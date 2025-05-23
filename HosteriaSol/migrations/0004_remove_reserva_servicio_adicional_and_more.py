# Generated by Django 5.1.6 on 2025-03-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HosteriaSol', '0003_alter_detallereserva_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='servicio_adicional',
        ),
        migrations.AlterField(
            model_name='detallereserva',
            name='precio_neto',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.CharField(choices=[('Recepcionista', 'RECEPCIONISTA'), ('Auxiliar_Aseo', 'AUXILIAR_ASEO'), ('Tecnico_Mantenimiento', 'TECNICO_MANTENIMIENTO'), ('Cocinero', 'COCINERO'), ('Mesero', 'MESERO')], default='Recepcionista', max_length=50),
        ),
        migrations.AlterField(
            model_name='pago',
            name='monto_total',
            field=models.DecimalField(decimal_places=0, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.IntegerField(choices=[(1, 'ADMINISTRADOR'), (2, 'EMPLEADO'), (3, 'CLIENTE')], default=3),
        ),
    ]

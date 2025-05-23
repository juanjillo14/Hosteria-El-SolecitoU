# Generated by Django 4.0.1 on 2025-03-13 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('capacidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('D', 'DISPONIBLE'), ('R', 'RESERVADA'), ('L', 'LIMPIEZA')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
                ('hora', models.TimeField()),
                ('metodo_pago', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(help_text='HH:mm')),
                ('hora_fin', models.TimeField(help_text='HH:mm')),
                ('estado', models.CharField(choices=[('activo', 'ACTIVO'), ('inactivo', 'INACTIVO')], default='activo', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería'), ('P', 'Pasaporte')], max_length=2)),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.CharField(max_length=254)),
                ('rol', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Empleado'), (3, 'Recepcionista'), (4, 'Cliente')], default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio_adicional', models.CharField(max_length=254)),
                ('fecha_reserva', models.DateTimeField(help_text='AAAA-MM-DD HH:mm')),
                ('estado', models.CharField(choices=[('A', 'ACTIVA'), ('D', 'DESHABILITADA')], default='A', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fk1_reserva_cliente', to='HosteriaSol.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('detalle_reserva', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HosteriaSol.detallereserva')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HosteriaSol.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='detallereserva',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HosteriaSol.habitacion'),
        ),
        migrations.AddField(
            model_name='detallereserva',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HosteriaSol.reserva'),
        ),
    ]

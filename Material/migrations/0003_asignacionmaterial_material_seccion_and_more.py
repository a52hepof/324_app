# Generated by Django 4.0.3 on 2022-10-22 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asociado', '0001_initial'),
        ('Material', '0002_alter_material_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsignacion', models.DateField(blank=True, max_length=100, null=True)),
                ('rondaSolar', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='seccion',
            field=models.ManyToManyField(through='Material.AsignacionMaterial', to='Asociado.seccion'),
        ),
        migrations.AddField(
            model_name='material',
            name='tipoMaterial',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Tiendas'), (2, 'Recambios tiendas'), (3, 'Campismo'), (4, 'Herramientas'), (5, 'Pinturas'), (6, 'Electricidad'), (7, 'Fontanería'), (8, 'Mesas y bancos'), (9, 'Infraestructura'), (39, 'Otros campismo'), (40, 'Cocina'), (41, 'Hornillos y roscos'), (42, 'Bombonas y cartuchos'), (49, 'Otros cocina'), (50, 'Didáctico'), (51, 'Otros didáctico'), (90, 'Recambios campismo'), (91, 'Recambios electricidad'), (92, 'Recambios fontanería'), (94, 'Recambios cocina')], null=True),
        ),
        migrations.AddField(
            model_name='revisionmaterial',
            name='resultadoRevision',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Revisión conforme'), (2, 'Desperfectos menores, reparaciones no urgentes'), (3, 'Necesita limpieza'), (4, 'Necesita reparación')], null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='User',
            field=models.CharField(blank=True, choices=[('fernando', 'fernando')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='asignacionmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Material.material'),
        ),
        migrations.AddField(
            model_name='asignacionmaterial',
            name='seccionName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asociado.seccion'),
        ),
    ]

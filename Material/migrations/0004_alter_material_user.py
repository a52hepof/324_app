# Generated by Django 4.0.3 on 2022-10-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Material', '0003_asignacionmaterial_material_seccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='User',
            field=models.CharField(blank=True, choices=[('colibri324', 'colibri324'), ('fernando', 'fernando'), ('milano', 'milano')], max_length=50, null=True),
        ),
    ]

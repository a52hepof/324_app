# Generated by Django 4.0.3 on 2022-10-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccessControl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Scouter'), (2, 'Tutor'), (3, 'Responsable')], default=1, null=True),
        ),
    ]
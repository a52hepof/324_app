# Generated by Django 4.0.3 on 2022-10-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccessControl', '0002_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='autorizado',
            field=models.BooleanField(default=0),
        ),
    ]

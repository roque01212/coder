# Generated by Django 4.0.6 on 2022-07-25 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0002_alter_familia_fecha_nac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='fecha_nac',
        ),
    ]

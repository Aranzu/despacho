# Generated by Django 3.1.2 on 2021-06-19 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_orden', '0002_auto_20210618_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenretiro',
            name='telefono',
        ),
    ]
# Generated by Django 3.1.2 on 2021-12-06 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_auto_20211206_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillorders',
            name='duration',
        ),
    ]
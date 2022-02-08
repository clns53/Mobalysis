# Generated by Django 3.1.2 on 2021-08-29 12:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210829_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='colloq',
        ),
        migrations.AddField(
            model_name='item',
            name='consumed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='consumedOnFull',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='depth',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='effect',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='item',
            name='ffrom',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), default=list, size=None),
        ),
        migrations.AddField(
            model_name='item',
            name='hideFromAll',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='inStore',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='into',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), default=list, size=None),
        ),
        migrations.AddField(
            model_name='item',
            name='requiredAlly',
            field=models.CharField(blank=True, db_index=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='requiredChampion',
            field=models.CharField(blank=True, db_index=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='specialRecipe',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='stacks',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='gold',
            field=models.JSONField(blank=True, db_index=True, default=dict),
        ),
        migrations.AlterField(
            model_name='item',
            name='maps',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='item',
            name='stats',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
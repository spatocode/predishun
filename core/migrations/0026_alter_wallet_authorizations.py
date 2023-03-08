# Generated by Django 4.1 on 2023-03-08 09:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_wallet_authorizations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='authorizations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=5),
        ),
    ]
# Generated by Django 4.1 on 2023-02-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_pricing_free_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='account_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='bank',
            field=models.CharField(default='', max_length=40),
        ),
    ]

# Generated by Django 4.0.6 on 2022-12-05 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sportstips_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportstips',
            old_name='match_day',
            new_name='date',
        ),
        migrations.AlterUniqueTogether(
            name='sportstips',
            unique_together={('sport', 'owner', 'home_team', 'away_team', 'date')},
        ),
    ]
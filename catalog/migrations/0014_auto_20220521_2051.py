# Generated by Django 3.2.3 on 2022-05-21 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20220518_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facultet',
            options={'ordering': ['name_faculteta']},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name_group']},
        ),
        migrations.AlterModelOptions(
            name='napravlenie',
            options={'ordering': ['name_napravlenie']},
        ),
    ]

# Generated by Django 3.2.3 on 2022-06-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_ficsation_propyski'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficsation',
            name='propyski',
            field=models.BinaryField(help_text='Присутсвовал/Отсутсвовал'),
        ),
    ]

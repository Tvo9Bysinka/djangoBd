# Generated by Django 3.2.3 on 2022-06-12 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_alter_studenti_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studenti',
            options={'ordering': ['-last_name']},
        ),
    ]

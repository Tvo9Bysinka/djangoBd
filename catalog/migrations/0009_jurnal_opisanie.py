# Generated by Django 3.2.3 on 2022-05-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20220516_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurnal',
            name='opisanie',
            field=models.TextField(help_text='Описание', max_length=1000, null=True),
        ),
    ]

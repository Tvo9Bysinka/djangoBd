# Generated by Django 3.2.3 on 2022-05-30 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20220526_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jurnal',
            name='data_propyskov',
        ),
        migrations.RemoveField(
            model_name='jurnal',
            name='opisanie',
        ),
        migrations.RemoveField(
            model_name='jurnal',
            name='propyski',
        ),
        migrations.CreateModel(
            name='Ficsation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_propyskov', models.DateField(blank=True, null=True)),
                ('propyski', models.BooleanField(default=True, help_text='Присутсвовал/Отсутсвовал')),
                ('opisanie', models.TextField(blank=True, help_text='Описание', max_length=1000, null=True)),
                ('id_nomer_zapisi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.jurnal')),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2022-06-07 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_alter_ficsation_propyski'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficsation',
            name='id_nomer_zapisi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.jurnal'),
        ),
    ]

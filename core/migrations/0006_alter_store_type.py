# Generated by Django 3.2.7 on 2021-09-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='type',
            field=models.CharField(choices=[('Abarrotes', 'Abarrotes'), ('Autoservicio', 'Autoservicio')], default='Autoservicio', max_length=15, verbose_name='Tipo de tienda'),
        ),
    ]

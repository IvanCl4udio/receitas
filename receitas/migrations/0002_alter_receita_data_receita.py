# Generated by Django 4.1.3 on 2022-12-06 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 12, 6, 10, 38, 34, 78573)),
        ),
    ]
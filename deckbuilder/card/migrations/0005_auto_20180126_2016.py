# Generated by Django 2.0.1 on 2018-01-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_auto_20180125_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='mana_cost',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

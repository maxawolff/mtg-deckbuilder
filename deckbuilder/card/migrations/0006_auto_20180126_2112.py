# Generated by Django 2.0.1 on 2018-01-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_auto_20180126_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='power',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='toughness',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
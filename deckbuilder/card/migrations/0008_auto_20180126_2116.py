# Generated by Django 2.0.1 on 2018-01-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_auto_20180126_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_text',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]

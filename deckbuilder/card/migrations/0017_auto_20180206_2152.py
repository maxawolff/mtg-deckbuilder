# Generated by Django 2.0.1 on 2018-02-06 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0016_auto_20180206_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='Commons',
            new_name='commons',
        ),
        migrations.AddField(
            model_name='card',
            name='mythics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mythics', to='card.Set'),
        ),
    ]

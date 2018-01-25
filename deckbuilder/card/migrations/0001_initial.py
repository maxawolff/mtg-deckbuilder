# Generated by Django 2.0.1 on 2018-01-23 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmc', models.CharField(max_length=20)),
                ('colors', models.CharField(choices=[['W', 'White'], ['U', 'Blue'], ['B', 'Black'], ['R', 'Red'], ['G', 'Green'], ['C', 'Colorless'], ['N', 'Generic']], max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('loyalty', models.IntegerField(blank=True, null=True)),
                ('mana_Cost', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('power', models.IntegerField(blank=True, null=True)),
                ('toughness', models.IntegerField(blank=True, null=True)),
                ('rarity', models.CharField(choices=[['M', 'Mythic-Rare'], ['R', 'Rare'], ['U', 'Uncommon'], ['C', 'Common']], max_length=20)),
                ('card_text', models.CharField(max_length=300)),
                ('card_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cards', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_set', to='card.Card')),
            ],
        ),
    ]
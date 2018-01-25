"""Model of a single magic card."""
from django.db import models


class Card(models.Model):
    """Class for card model."""

    COLORS = (['W', 'White'], ['U', 'Blue'], ['B', 'Black'],
              ['R', 'Red'], ['G', 'Green'], ['C', 'Colorless'],
              ['N', 'Generic'])
    RARITIES = (['M', 'Mythic-Rare'], ['R', 'Rare'],
                ['U', 'Uncommon'], ['C', 'Common'])
    cmc = models.CharField(max_length=20)
    colors = models.CharField(max_length=20, choices=COLORS)
    image = models.ImageField(upload_to='images')
    loyalty = models.IntegerField(null=True, blank=True)
    mana_Cost = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    power = models.IntegerField(null=True, blank=True)
    toughness = models.IntegerField(null=True, blank=True)
    rarity = models.CharField(max_length=20, choices=RARITIES)
    card_text = models.CharField(max_length=300)
    card_type = models.CharField(max_length=20)


class Set(models.Model):
    """Class for set model."""

    name = models.CharField(max_length=50)
    cards = models.ForeignKey(Card, on_delete=models.CASCADE,
                              related_name='from_set', blank=True, null=True)

"""Model of a single magic card."""
from django.db import models
from multiselectfield import MultiSelectField


class Set(models.Model):
    """Class for set model."""

    name = models.CharField(max_length=50)

    def __str__(self):
        """Change how model is displayed when printed."""
        return self.name


class Card(models.Model):
    """Class for card model."""

    COLORS = (['W', 'White'], ['U', 'Blue'], ['B', 'Black'],
              ['R', 'Red'], ['G', 'Green'], ['C', 'Colorless'],
              ['N', 'Generic'])
    RARITIES = (['M', 'Mythic-Rare'], ['R', 'Rare'],
                ['U', 'Uncommon'], ['C', 'Common'])
    cmc = models.CharField(max_length=20)
    colors = MultiSelectField(max_length=100, choices=COLORS)
    image = models.ImageField(upload_to='images')
    loyalty = models.IntegerField(null=True, blank=True)
    mana_cost = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=30)
    power = models.CharField(max_length=5, null=True, blank=True)
    toughness = models.CharField(max_length=5, null=True, blank=True)
    rarity = models.CharField(max_length=20, choices=RARITIES)
    card_text = models.CharField(max_length=600, blank=True, null=True)
    card_type = models.CharField(max_length=50)
    card_subtypes = models.CharField(max_length=50, blank=True, null=True)
    from_set = models.ForeignKey(Set, on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        """Change how model is displayed when printed."""
        return self.name

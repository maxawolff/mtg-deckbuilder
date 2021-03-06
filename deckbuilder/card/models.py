"""Model of a single magic card."""
from django.db import models
from multiselectfield import MultiSelectField
from django.utils.text import slugify


class Set(models.Model):
    """Class for set model."""

    name = models.CharField(max_length=50)
    set_id = models.CharField(max_length=5, null=True, blank=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    # sealed_format = models.ManyToManyField('self')
    big_set = models.ForeignKey('self', on_delete=models.CASCADE,
                                blank=True, null=True, related_name='big_sets')
    small_set = models.ForeignKey('self', on_delete=models.CASCADE,
                                  blank=True, null=True,
                                  related_name='small_sets')
    third_set = models.ForeignKey('self', on_delete=models.CASCADE,
                                  blank=True, null=True,
                                  related_name='third_sets')

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
    number = models.CharField(max_length=10)
    card_text = models.CharField(max_length=600, blank=True, null=True)
    card_type = models.CharField(max_length=50)
    card_subtypes = models.CharField(max_length=50, blank=True, null=True)
    from_set = models.ForeignKey(Set, on_delete=models.CASCADE,
                                 blank=True, null=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    rares = models.ForeignKey(Set, on_delete=models.CASCADE,
                              blank=True, null=True, related_name='rares')
    uncommons = models.ForeignKey(Set, on_delete=models.CASCADE,
                                  blank=True, null=True,
                                  related_name='uncommons')
    commons = models.ForeignKey(Set, on_delete=models.CASCADE,
                                blank=True, null=True, related_name='commons')
    mythics = models.ForeignKey(Set, on_delete=models.CASCADE,
                                blank=True, null=True, related_name='mythics')
    back_side = models.OneToOneField('self', on_delete=models.CASCADE,
                                     blank=True, null=True,
                                     related_name='front_side')
    in_pack = models.BooleanField(default=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Card.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        """Overwrite save to generate slug."""
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    def __str__(self):
        """Change how model is displayed when printed."""
        return self.name


class Deck(models.Model):
    """Class for a deck model."""

    FORMATS = (['ST', 'Standard'], ['SE', 'Sealed'], ['DR', 'Draft'])

    name = models.CharField(max_length=50)
    deck_format = models.CharField(max_length=50, choices=FORMATS)
    card_list = models.ManyToManyField(Card)


# class Transform(models.Model):
#     """Model for the fliped side of a trasnform card."""

#     front =

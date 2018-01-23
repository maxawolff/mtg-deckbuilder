"""Model of a single magic card."""
from django.db import models


class Card(models.Model):
    """Class for card model."""

    cmc = models.CharField(max_length=20)


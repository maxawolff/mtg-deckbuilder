"""Tests for card objects."""
from django.test import TestCase
from card.models import Card, Set


class CardTestCase(TestCase):
    """."""

    def setUp(self):
        """."""
        set1 = Set.objects.create(name='Rivals of Ixalan')
        colors = ['White', 'Black']
        card1 = Card.objects.create(name='something', colors=colors)
        # card1.colors = 'anything'
        # card1.save()

    def test_set_name(self):
        """Test that set object is created with correct name."""
        self.assertTrue(Set.objects.count() == 1)
        rix = Set.objects.first()
        self.assertTrue(rix.name == "Rivals of Ixalan")

    def test_card_created(self):
        """Test that a card object is created with only name."""
        self.assertTrue(Card.objects.count() == 1)
        card1 = Card.objects.first()
        import pdb; pdb.set_trace()

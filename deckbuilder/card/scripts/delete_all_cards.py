"""."""
from card.models import Card, Set


def run():
    """Delete all cards in database."""
    all_cards = Card.objects.all()
    all_cards.delete()
    all_sets = Set.objects.all()
    all_sets.delete()

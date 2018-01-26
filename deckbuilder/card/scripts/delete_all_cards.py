"""."""
from card.models import Card


def run():
    """Delete all cards in database."""
    all_cards = Card.objects.all()
    all_cards.delete()

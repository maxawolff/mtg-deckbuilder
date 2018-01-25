from card import Card, Set
from mtgsdk import Card as SourceCard
from mtgsdk import Set as sourceSet

def run(*args):
    """Add a card to the database from the mtgsdk."""
    if args:
        pass
    else:
        sets = Set.objects.all()
        if not sets:
            return
        cur_set = sets[0]

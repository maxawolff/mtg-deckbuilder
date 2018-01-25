from mtgsdk import Card as SourceCard
from mtgsdk import Set as sourceSet
from card.models import Card, Set

def run(*args):
    """Add a card to the database from the mtgsdk."""
    if args:
        pass
    else:
        sets = Set.objects.all()
        if not sets:
            return
        cur_set = sets[0]
        rivals_cards = SourceCard.where(set='rix')
        rivals_cards = rivals_cards.all()
        for card in rivals_cards:
            new_card = Card.objects.create(name=card.name,
                                           colors=card.colors,
                                           cmc=card.cmc,
                                           image=card.image_url,
                                           mana_cost=card.mana_cost,
                                           rarity=card.rarity,
                                           card_type=card.type,
                                           )
            if card.power:
                new_card.power = card.power
            if card.toughness:
                new_card.toughness = card.toughness
            if card.loyalty:
                new_card.loyalty = card.loyalty
            new_card.save()

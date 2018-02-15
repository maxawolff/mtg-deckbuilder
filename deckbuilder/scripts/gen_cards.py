"""Test."""
from mtgsdk import Card as SourceCard
from mtgsdk import Set as sourceSet
from card.models import Card, Set
from django.utils.text import slugify


def run(*args):
    """Add a card to the database from the mtgsdk."""
    if args:
        # import pdb; pdb.set_trace()
        set_str = args[0]
        cur_set = ''
        try:
            cur_set = sourceSet.find(set_str)
        except:
            print('Set id was invalid, please check id')
            return
        set_in_db = False
        all_sets = Set.objects.all()
        selected_set = ''
        for one_set in all_sets:
            if cur_set.name == one_set.name:
                set_in_db = True
                selected_set = one_set
        if set_in_db:
            cards_in_set = selected_set.card_set.all()
            cards_in_set.delete()
            gen_set(set_str, selected_set)
        else:
            new_set = Set(name=cur_set.name,
                          set_id=cur_set.code,
                          slug=slugify(cur_set.code))
            new_set.save()
            gen_set(set_str, new_set)

    else:
        all_cards = Card.objects.all()
        all_cards.delete()
        sets = Set.objects.all()
        if not sets:
            return
        cur_set = sets[0]
        rivals = SourceCard.where(set='rix')
        rivals_cards = rivals.all()
        for card in rivals_cards:
            new_card = Card.objects.create(name=card.name,
                                           colors=card.colors,
                                           cmc=card.cmc,
                                           image=card.image_url,
                                           mana_cost=card.mana_cost,
                                           rarity=card.rarity,
                                           card_type=card.types,
                                           card_subtypes=card.subtypes,
                                           card_text=card.text,
                                           number=card.number
                                           )
            if card.power:
                new_card.power = card.power
            if card.toughness:
                new_card.toughness = card.toughness
            if card.loyalty:
                new_card.loyalty = card.loyalty
            new_card.save()
            cur_set.card_set.add(new_card)
            if card.rarity == 'Common':
                pass


def gen_set(set_id, set_obj):
    """Given a set id, generate card objects and add to db."""
    raw_cards = SourceCard.where(set=set_id)
    cards = raw_cards.all()
    for card in cards:
        new_card = Card.objects.create(name=card.name,
                                       colors=card.colors,
                                       cmc=card.cmc,
                                       image=card.image_url,
                                       mana_cost=card.mana_cost,
                                       rarity=card.rarity,
                                       card_type=card.types,
                                       card_subtypes=card.subtypes,
                                       card_text=card.text,
                                       number=card.number
                                       )
        if card.power:
            new_card.power = card.power
        if card.toughness:
            new_card.toughness = card.toughness
        if card.loyalty:
            new_card.loyalty = card.loyalty
        new_card.save()
        set_obj.card_set.add(new_card)
        if card.rarity == "Rare":
            set_obj.rares.add(new_card)
        if card.rarity == "Uncommon":
            set_obj.uncommons.add(new_card)
        if card.rarity == "Common":
            set_obj.commons.add(new_card)
        if card.rarity == "Mythic Rare":
            set_obj.mythics.add(new_card)
        if 'b' in card.number:
            possible_cards = Card.objects.filter(from_set=set_obj)
            front_number = card.number[:-1] + 'a'
            front_card = possible_cards.filter(number=front_number)[0]
            front_card.back_side = new_card

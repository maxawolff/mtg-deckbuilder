"""Views for cards, as well as generating from sdk."""
from django.views.generic import TemplateView, ListView, DetailView
from card.models import Card, Set
from random import randint, sample


class TestAddView(TemplateView):
    """Add one card to the database."""

    template_name = "card/test_view.html"


class ListCards(ListView):
    """Show all cards in the database."""

    template_name = "card/list_cards_view.html"
    model = Card

    def get_context_data(self, **kwargs):
        """."""
        context = super(ListCards, self).get_context_data(**kwargs)
        all_sets = Set.objects.all()
        context['all_sets'] = all_sets
        return context


class CardDetail(DetailView):
    """Show detail for one card."""

    template_name = 'card/card_detail_view.html'
    model = Card

    def get_context_data(self, **kwargs):
        """."""
        context = super(CardDetail, self).get_context_data(**kwargs)
        all_sets = Set.objects.all()
        context['all_sets'] = all_sets
        # card = context['object']
        # import pdb; pdb.set_trace()
        return context


class CardsBySet(DetailView):
    """Show all cards of a given set."""

    template_name = 'card/list_cards_in_set.html'
    model = Set

    def get_context_data(self, **kwargs):
        """."""
        context = super(CardsBySet, self).get_context_data(**kwargs)
        all_sets = Set.objects.all()
        context['all_sets'] = all_sets
        cards_in_set = context['object'].card_set.all()
        context['cards'] = cards_in_set
        return context


class GeneratePack(DetailView):
    """docstring for GeneratePack."""

    template_name = 'deckbuilder/generate_pack.html'
    model = Set

    def get_context_data(self, **kwargs):
        """."""
        context = super(GeneratePack, self).get_context_data(**kwargs)
        all_sets = Set.objects.all()
        context['all_sets'] = all_sets
        pack = []
        commons = context['object'].commons.filter(in_pack=True)
        uncommons = context['object'].uncommons.filter(in_pack=True)
        rares = ''
        rare_or_mythic = randint(1, 8)
        if rare_or_mythic == 8:
            rares = context['object'].mythics.filter(in_pack=True)
        else:
            rares = context['object'].rares.filter(in_pack=True)
        common_nums = sample(range(commons.count()), 10)
        uncommon_nums = sample(range(uncommons.count()), 3)
        rare_num = randint(0, rares.count() - 1)
        pack.append(rares[rare_num])
        for num in uncommon_nums:
            pack.append(uncommons[num])
        for num in common_nums:
            pack.append(commons[num])
        context['pack'] = pack
        return context


class CreateSealedDeck(ListView):
    """View for creating a sealed deck."""

"""Views for cards, as well as generating from sdk."""
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView
from card.models import Card, Set
from random import randint


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
        # import pdb; pdb.set_trace()
        # import pdb; pdb.set_trace()
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
        # import pdb; pdb.set_trace()
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
        import pdb; pdb.set_trace()
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
        commons = context['object'].commons.all()
        uncommons = context['object'].uncommons.all()
        rares = ''
        rare_or_mythic = randint(1, 8)
        if rare_or_mythic == 8:
            rares = context['object'].mythics.all()
        else:
            rares = context['object'].rares.all()
        for i in range(10):
            pack.append(commons[randint(1, commons.count() - 1)])
        for i in range(3):
            pack.append(uncommons[randint(1, uncommons.count() - 1)])
        for i in range(1):
            pack.append(rares[randint(1, rares.count() - 1)])
        context['pack'] = pack
        # import pdb; pdb.set_trace()
        return context

"""Views for cards, as well as generating from sdk."""
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView
from card.models import Card, Set


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
        # import pdb; pdb.set_trace()
        # import pdb; pdb.set_trace()
        return context


class CardsBySet(DetailView):
    """Show all cards of a given set."""

    template_name = 'card/list_cards_view.html'
    model = Set

    def get_context_data(self, **kwargs):
        """."""
        context = super(CardsBySet, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        return context

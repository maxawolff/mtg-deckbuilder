"""Views for cards, as well as generating from sdk."""
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from card.models import Card


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
        return context

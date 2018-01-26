"""Views for cards, as well as generating from sdk."""
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView


class TestAddView(TemplateView):
    """Add one card to the database."""

    template_name = "card/test_view.html"

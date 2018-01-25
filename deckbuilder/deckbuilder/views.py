"""Views associated with the core of the site."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Display the home page."""

    template_name = 'deckbuilder/base.html'

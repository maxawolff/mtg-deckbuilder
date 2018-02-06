"""Views associated with the core of the site."""

from django.views.generic import TemplateView, ListView
from card.models import Set


class HomeView(ListView):
    """Display the home page."""

    template_name = 'deckbuilder/base.html'
    model = Set

    def get_context_data(self, **kwargs):
        """."""
        context = super(HomeView, self).get_context_data(**kwargs)
        all_sets = Set.objects.all()
        context['all_sets'] = all_sets
        # import pdb; pdb.set_trace()
        return context

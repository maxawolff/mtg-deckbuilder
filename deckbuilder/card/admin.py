from django.contrib import admin
from card.models import Card, Set

# Register your models here.
admin.site.register(Card)
admin.site.register(Set)


class CardAdmin(object):
    """docstring for CardAdmin."""

    prepopulated_fields = {'slug': ('name',)}

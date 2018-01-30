"""deckbuilder URL Configuration"""
from django.contrib import admin
from django.urls import path
from deckbuilder.views import HomeView
from card.views import TestAddView, ListCards, CardDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='homepage'),
    path('all-cards', ListCards.as_view(), name='all_cards'),
    path('card/<slug:slug>/', CardDetail.as_view(), name='card_detail'),
    path('test', TestAddView.as_view(), name='test_view')
]

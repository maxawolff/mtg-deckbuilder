"""deckbuilder URL Configuration"""
from django.contrib import admin
from django.urls import path
from deckbuilder.views import HomeView
from card.views import TestAddView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='homepage'),
    path('test', TestAddView.as_view(), name='test_view')
]

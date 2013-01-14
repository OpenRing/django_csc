# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# python/django imports
from django.contrib import admin

# project imports
from csc.models import Country, State, City


class CountryAdmin(admin.ModelAdmin):
    """ list display for country model """
    list_display = ('name', 'code')
admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    """ list display for state model """
    list_display = ('name', 'code')
admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    """ list display for city model """
    list_display = ('name', 'code')
admin.site.register(City, CityAdmin)

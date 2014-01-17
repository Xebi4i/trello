from django.contrib import admin
from NBA.apps.NBA_players.models import Player

class PlayerAdmin(admin.ModelAdmin): # some cosmetic changes
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Player information', {'fields': ['team', 'age']}),
    ]

# Register your models here.
admin.site.register(Player, PlayerAdmin) #add app players to admin index page

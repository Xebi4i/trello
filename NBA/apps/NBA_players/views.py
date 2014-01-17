from django.shortcuts import render

from NBA.apps.NBA_players.models import Player

def index(request):
    players_list = Player.objects.all().order_by('-name')
    context = {'players_list': players_list}
    return render(request, 'NBA_players/index.html', context)

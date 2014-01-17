from django.shortcuts import render

from NBA.apps.NBA_players.models import Player

def create_some_players():
    '''
    Create some players, who was see in /players
    '''
    players = [['Tim Duncan', 'San Antonio Spurs', 35], ['Jeff Green', 'Boston Celtics', 27], ['Kevin Durant', 'Oklahoma City Thunder', 25], ['James Jones', 'Miami Heat', 33], ['Dwyane Wade', 'Miami Heat', 32]]
    if str(Player.objects.all()) == '[]':
        for player in players:
            p = Player(name=player[0], team=player[1], age=player[2])
            p.save()

def index(request):
    create_some_players()
    players_list = Player.objects.all().order_by('-name')
    context = {'players_list': players_list}
    return render(request, 'NBA_players/index.html', context)

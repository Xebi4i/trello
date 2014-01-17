from django.test import TestCase

from NBA.apps.NBA_players.models import Player

# Create your tests here.
def create_player(name, team, age):
    return Player.objects.create(name=name, team=team, age=age)

class PlayerViewTests(TestCase):

    def test_player_age_more_than_sixty(self):
        """
        If player have too big age message should be displayed.
        """
        flag = True
        create_player(name="Tony Parker", team="San Antonio Spurs", age=31)
        for pl in Player.objects.all():
            if pl.age > 60:
                flag = False
        self.assertEqual(flag, True)

    def test_player_age_less_than_seventeen(self):
        """
        If player have too small age message should be displayed.
        """
        flag = True
        create_player(name="KG", team="Oklahoma", age=33)
        for pl in Player.objects.all():
            if pl.age < 17:
                flag = False
        self.assertEqual(flag, True)

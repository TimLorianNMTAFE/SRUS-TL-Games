from app.player import Player
import unittest

test_player = Player("Tim", 13)


class PlayerTestMethods(unittest.TestCase):
    def test_name(self):
        self.assertEqual(test_player._name, "Tim")

    def test_uniqueid(self):
        self.assertEqual(test_player._uid, 13)

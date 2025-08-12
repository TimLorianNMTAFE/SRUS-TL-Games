from app.player import Player
import unittest


class UnitTestMethods(unittest.TestCase):
    test_player = Player("Tim", 13)

    def test_name(self):
        self.assertEqual(self.test_player._name, "Tim")

    def test_uniqueid(self):
        self.assertEqual(self.test_player._uid, 13)

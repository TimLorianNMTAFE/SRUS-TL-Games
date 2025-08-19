from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode
import unittest

test_list = PlayerList()
test_player = Player("Tim", 13)
test_node = PlayerNode(test_player)


class PlayerListTestMethods(unittest.TestCase):

    def test_push_when_list_is_empty(self):
        test_list.push(test_node)
        self.assertEqual(type(test_list.get_head()), type(test_node))
        print(type(test_list.get_head()))
        print(type(test_node))

    def test_push_when_list_is_not_empty(self):
        pre_existing_player = Player("Jimbo", 11)
        pre_existing_node = PlayerNode(pre_existing_player)
        test_list.push(pre_existing_node)
        test_list.push(test_node)
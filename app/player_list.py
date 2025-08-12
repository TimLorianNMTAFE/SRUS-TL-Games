import player_node

class PlayerList:
    def __init__(self):
        self._head = None

    def push(self, player):
        _old_head = PlayerList.__init__(self)._head
        _old_next_player = player_node.PlayerNode.get_next_player(player)
        _new_head = player_node.PlayerNode.get_player(player)
        _new_next_player = player_node.PlayerNode.get_next_player(player)
        self._head = _new_head

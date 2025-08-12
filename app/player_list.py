from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self.count = 0

    def push(self, player):
        if self._head is not None:
            new_player = PlayerNode(player)
            new_player.set_next_player(self._head)
            self._head.previous_player = new_player
        else:
            new_player = PlayerNode(player)
        self._head = new_player
        self.count += 1
        
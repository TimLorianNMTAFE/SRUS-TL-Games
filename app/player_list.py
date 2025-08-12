from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self.count = 0

    def push(self, player):
        if self._head is not None:
            new_player_node = PlayerNode(player)
            new_player_node.set_next_player(self._head)
            self._head.previous_player = new_player_node
        else:
            new_player_node = PlayerNode(player)
        self._head = new_player_node
        self.count += 1

    def get_head(self):
        return self._head

    def head_as_string(self):
        return self._head.__str__()

    def iter(self):
        current_player = self._head
        while current_player:
            player_data = current_player.get_head()
            current_player = current_player.next
            yield player_data

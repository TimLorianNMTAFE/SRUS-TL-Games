class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next_player = None
        self._previous_player = None

    # getter method player
    def get_player(self):
        return self._player

    # setter method player
    def set_player(self, player):
        self._player = player

    # getter method next player
    def get_next_player(self):
        return self._next_player

    # getter method previous player
    def get_previous_player(self):
        return self._previous_player

    def __str__(self):
        return self._player, self._previous_player, self._next_player

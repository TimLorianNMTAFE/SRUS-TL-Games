class Player:
    def __init__(self, name, uid):
        self._uid = uid
        self._name = name

    def __str__(self):
        return self._uid.__str__(), self._name.__str__()
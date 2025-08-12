class Player:
    def __init__(self, name, uid):
        self.uid = uid
        self.name = name

    def __str__(self):
        return self.uid.__str__(), self.name.__str__()

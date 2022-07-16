import copy


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def __repr__(self):
        return str(self.x) + " " + str(self.y)

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def get_copy(self):
        return copy.deepcopy(self)

    def check_same_pos(self, other):
        if isinstance(other, Block):
            if other.x == self.x and other.y == self.y:
                return True

        return False

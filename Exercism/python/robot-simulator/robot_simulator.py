NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot(object):
    def __init__(self, bearing: tuple = NORTH, x: int = 0, y: int = 0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self) -> tuple:
        return (self.x, self.y)

    def advance(self) -> None:
        self.x += self.bearing[0]
        self.y += self.bearing[1]

    def turn_right(self) -> None:
        self.bearing = {
            NORTH: EAST,
            EAST: SOUTH,
            SOUTH: WEST,
            WEST: NORTH
        }[self.bearing]

    def turn_left(self) -> None:
        self.bearing = {
            NORTH: WEST,
            EAST: NORTH,
            SOUTH: EAST,
            WEST: SOUTH
        }[self.bearing]

    def simulate(self, instructions: str) -> None:
        for instruct in instructions:
            {
                'R': self.turn_right,
                'L': self.turn_left,
                'A': self.advance
            }[instruct]()

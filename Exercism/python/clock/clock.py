class Clock(object):
    """A clock that handles times without dates."""
    def __init__(self, hour: int, minute: int):
        self._hour = 0
        self._minute = 0
        self.minute += minute
        self.hour += hour

    @property
    def hour(self) -> int:
        return self._hour

    @hour.setter
    def hour(self, value: int):
        self._hour = value % 24

    @property
    def minute(self) -> int:
        return self._minute

    @minute.setter
    def minute(self, value: int):
        self.hour += value // 60
        self._minute = value % 60

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other: object) -> bool:
        return str(self) == str(other)

    def __add__(self, minutes: int) -> object:
        self.minute += minutes
        return self

    def __sub__(self, minutes: int) -> object:
        self.minute -= minutes
        return self

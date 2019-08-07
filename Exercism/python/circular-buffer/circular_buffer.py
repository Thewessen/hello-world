class BufferFullException(Exception):
    def __init__(self, message='Buffer full!'):
        super().__init__(message)


class BufferEmptyException(Exception):
    def __init__(self, message='Buffer empty!'):
        super().__init__(message)


class CircularBuffer(object):
    """Creates a circular buffer of fixed size"""

    def __init__(self, capacity: int):
        self._rc = 0
        self._wc = 0
        self.capacity = capacity
        self.clear()

    def inc_rc(self) -> None:
        self._rc += 1
        self._rc %= self.capacity

    def inc_wc(self) -> None:
        self._wc += 1
        self._wc %= self.capacity

    def read(self):
        value = self.buffer[self._rc]
        if value is None:
            raise BufferEmptyException
        self.buffer[self._rc] = None
        self.inc_rc()
        return value

    def write(self, data):
        if self.buffer[self._wc] is not None:
            raise BufferFullException
        self.buffer[self._wc] = data
        self.inc_wc()

    def overwrite(self, data):
        if self._wc == self._rc:
            self.inc_rc()
        self.buffer[self._wc] = data
        self.inc_wc()

    def clear(self):
        self.buffer = [None] * self.capacity

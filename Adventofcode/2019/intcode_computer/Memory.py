from enum import Enum


class ParamMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Memory:
    """Base memory object with read and write methods.
    Includes mode option for reading"""
    def __init__(self, mem: list[str]):
        self.mem = dict(enumerate(mem))
        self.rel_base = 0

    def __str__(self):
        return ','.join(self.mem.values())

    def read(self, address: int, mode = ParamMode.IMMEDIATE) -> int:
        a = self.mem.get(address, 0)
        if mode == ParamMode.IMMEDIATE:
            return int(a)
        elif mode == ParamMode.POSITION:
            return int(self.mem.get(int(a), 0))
        elif mode == ParamMode.RELATIVE:
            return int(self.mem.get(self.rel_base + int(a), 0))
        else:
            raise ValueError('Unsupported mode: ' + mode)

    def write(self, address: int, value: int) -> None:
        self.mem[address] = str(value)

    def adj_base(self, distance: int) -> None:
        self.rel_base += distance

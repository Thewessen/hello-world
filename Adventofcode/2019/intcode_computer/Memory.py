from enum import Enum


class ParamMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Memory:
    """Base memory object with read and write methods.
    Includes mode option for reading"""
    def __init__(self, mem: list[str]):
        self.mem = list(mem)

    def __str__(self):
        return ','.join(self.mem)

    def read(self, address: int, mode = ParamMode.IMMEDIATE) -> int:
        a = self.mem[address]
        if mode == ParamMode.IMMEDIATE:
            return int(a)
        return int(self.mem[int(a)])

    def write(self, address: int, value: int):
        self.mem[address] = str(value)

from enum import Enum
from Memory import ParamMode


class Instruction(Enum):
    SUM = 1
    PROD = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_TRUE = 5
    JUMP_FALSE = 6
    LESS_THAN = 7
    EQUAL = 8
    ADJ_MEM = 9
    HALT = 99


class Opcode:
    """Opcode reading helper class"""
    def __init__(self, value: int):
        self.op = str(value).rjust(6, '0')

    @property
    def instruction(self) -> Instruction:
        return Instruction(int(self.op[-2:]))

    def mode(self, param: int) -> ParamMode:
        return ParamMode(int(self.op[-1 * param - 2]))

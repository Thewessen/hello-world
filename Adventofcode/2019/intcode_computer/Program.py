from typing import Optional
import sys
sys.path.append('.')
from Memory import Memory, ParamMode
from Opcode import Opcode, Instruction

class Program:
    """Base program object"""
    def __init__(self, mem: list[str], *args):
        self.mem = Memory(mem)
        self.pointer = 0
        self.args = list(args)
        self.done = False

    @classmethod
    def from_str(cls, data: str, *args):
        return cls(data.split(','), *args)

    def __repr__(self):
        return f"Program<args: {repr(self.args)}, pointer: {str(self.pointer)}>"

    def __iter__(self):
        return self
    
    def __next__(self):
        while not self.done:
            self.opcode = Opcode(self.mem.read(self.pointer))
            i = self.opcode.instruction
            if i == Instruction.SUM:
                self.sum()
            if i == Instruction.PROD:
                self.prod()
            if i == Instruction.INPUT:
                self.inp()
            if i == Instruction.OUTPUT:
                return self.out()
            if i == Instruction.JUMP_TRUE:
                self.jump_if_true()
            if i == Instruction.JUMP_FALSE:
                self.jump_if_false()
            if i == Instruction.LESS_THAN:
                self.less_than()
            if i == Instruction.EQUAL:
                self.equals()
            if i == Instruction.ADJ_MEM:
                self.adj_mem_base()
            if i == Instruction.HALT:
                self.done = True
                raise StopIteration("End of program")

    def sum(self):
        a = self._param(1)
        b = self._param(2)
        self._out(3, a + b)
        self.pointer += 4

    def prod(self):
        a = self._param(1)
        b = self._param(2)
        self._out(3, a * b)
        self.pointer += 4

    def inp(self):
        if len(self.args) < 1:
            raise ValueError('Insufficient arguments for program')
        value, *args = self.args
        self.args = args
        self._out(1, value)
        self.pointer += 2

    def out(self):
        output = self._param(1)
        self.pointer += 2
        return output

    def jump_if_true(self):
        value = self._param(1)
        if value == 0:
            self.pointer += 3
            return
        address = self._param(2)
        self.pointer = address

    def jump_if_false(self):
        value = self._param(1)
        if value != 0:
            self.pointer += 3
            return
        address = self._param(2)
        self.pointer = address

    def less_than(self):
        a = self._param(1)
        b = self._param(2)
        self._out(3, int(a < b))
        self.pointer += 4

    def equals(self):
        a = self.mem.read(self.pointer + 1, self.opcode.mode(1))
        b = self.mem.read(self.pointer + 2, self.opcode.mode(2))
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, int(a == b), self.opcode.mode(3))
        self.pointer += 4
    
    def adj_mem_base(self):
        a = self.mem.read(self.pointer + 1, self.opcode.mode(1))
        self.mem.adj_base(a)
        self.pointer += 2

    def _param(self, nr: int) -> int:
        return self.mem.read(self.pointer + nr, self.opcode.mode(nr))

    def _out(self, nr: int, value: int) -> None:
        addr = self.mem.read(self.pointer + nr)
        self.mem.write(addr, value, self.opcode.mode(nr))

    def run(self) -> Optional[int]:
        # intermediate results are only for diagnostics
        result = 0
        for inst in self:
            if type(inst) == int and inst is not None:
                if result != 0:
                    raise ValueError(("Intermediate result none zero"
                                      "Test program failed."))
                result = inst
        return result

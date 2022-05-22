from typing import Optional
import sys
sys.path.append('.')
from Memory import Memory, ParamMode

class Program:
    """Base program object"""
    def __init__(self, mem: list[str], *args):
        self.mem = Memory(mem)
        self.pointer = 0
        self.args = args

    @classmethod
    def from_str(cls, data: str, *args):
        return cls(data.split(','), *args)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            i = int(self.opcode[-2:])
            if i == 1:
                self.sum()
            if i == 2:
                self.prod()
            if i == 3:
                self.inp()
            if i == 4:
                return self.out()
            if i == 5:
                self.jump_if_true()
            if i == 6:
                self.jump_if_false()
            if i == 7:
                self.less_than()
            if i == 8:
                self.equals()
            if i == 9:
                self.adj_mem_base()
            if i == 99:
                raise StopIteration("End of program")

    @property
    def opcode(self):
        op = str(self.mem.read(self.pointer))
        return op.rjust(6, '0')

    def sum(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, a + b)
        self.pointer += 4

    def prod(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, a * b)
        self.pointer += 4

    def inp(self):
        [value, *args] = self.args
        self.args = args
        address = self.mem.read(self.pointer + 1)
        self.mem.write(address, value)
        self.pointer += 2

    def out(self):
        output = self._get_param(1)
        self.pointer += 2
        return output

    def jump_if_true(self):
        value = self._get_param(1)
        if value == 0:
            self.pointer += 3
            return
        address = self._get_param(2)
        self.pointer = address

    def jump_if_false(self):
        value = self._get_param(1)
        if value != 0:
            self.pointer += 3
            return
        address = self._get_param(2)
        self.pointer = address

    def less_than(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, int(a < b))
        self.pointer += 4

    def equals(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, int(a == b))
        self.pointer += 4
    
    def adj_mem_base(self):
        a = self._get_param(1)
        self.mem.adj_base(a)
        self.pointer += 2

    def _get_param(self, nr: int) -> int:
        address = self.pointer + nr
        mode = ParamMode(int(self.opcode[-1 * nr - 2]))
        return self.mem.read(address, mode)

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

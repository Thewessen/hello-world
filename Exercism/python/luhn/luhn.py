class Luhn(object):
    def __init__(self, card_num: str):
        try:
            self.nr = [int(n) for n in card_num.replace(' ', '')]
        except ValueError:
            self.nr = []

    def valid(self) -> bool:
        size = len(self.nr)
        return size > 1 and sum([n * 2 if n * 2 <= 9 else n * 2 - 9
                                for n in self.nr[size-2::-2]]
                                + self.nr[size-1::-2]) % 10 == 0

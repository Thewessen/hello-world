import re


class PhoneNumber:
    def __init__(self, number: str) -> object:
        """Stores a phonenumber according NANP"""
        number = re.sub(" +", " ", number).strip()
        nr = re.match((r"^(?:\+?1)?\W?"
                       r"\(?([2-9][0-9]{2})\)?\W?"
                       r"([2-9][0-9]{2})\W?"
                       r"([0-9]{4})$"), number)
        if nr is None:
            raise ValueError("Not a phonenumber")
        self.number = ''.join(nr.groups())
        self.area_code = nr.group(1)

    def pretty(self) -> str:
        """Pretify phonenumber"""
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"

class Allergies(object):
    """Given a person's allergy score, determine whether or not
    they're allergic to a given item, and their full list of allergies."""
    ALLERGIES = [
            'eggs',
            'peanuts',
            'shellfish',
            'strawberries',
            'tomatoes',
            'chocolate',
            'pollen',
            'cats'
        ]

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item: str) -> bool:
        """Whether or not the person is allergic to"""
        return bool(self.score & (1 << self.ALLERGIES.index(item)))

    @property
    def lst(self) -> list:
        """The full list of allergies"""
        return [a for a in self.ALLERGIES if self.allergic_to(a)]

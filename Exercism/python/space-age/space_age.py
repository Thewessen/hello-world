class SpaceAge(object):
    """Given an age in seconds, calculate how old someone would be on some
    planet"""
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = seconds / 31557600

    def on_mercury(self) -> float:
        """Calculate age on mercury"""
        return round(self.earth / 0.2408467, 2)

    def on_venus(self) -> float:
        """Calculate age on venus"""
        return round(self.earth / 0.61519726, 2)

    def on_earth(self) -> float:
        """Calculate age on earth"""
        return round(self.earth, 2)

    def on_mars(self) -> float:
        """Calculate age on mars"""
        return round(self.earth / 1.8808158, 2)

    def on_jupiter(self) -> float:
        """Calculate age on jupiter"""
        return round(self.earth / 11.862615, 2)

    def on_saturn(self) -> float:
        """Calculate age on saturn"""
        return round(self.earth / 29.447498, 2)

    def on_uranus(self) -> float:
        """Calculate age on uranus"""
        return round(self.earth / 84.016846, 2)

    def on_neptune(self) -> float:
        """Calculate age on neptune"""
        return round(self.earth / 164.79132, 2)


from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string of a Silver Service Taxi."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the current Fare"""
        # round fare to nearest 10 cents
        return self.flagfall + super().get_fare()


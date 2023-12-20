from .FuzzyValue import FuzzyValue


class FuzzyInterval:
    def __init__(self, lower_border, upper_border):
        if upper_border < lower_border:
            upper_border, lower_border = lower_border, upper_border
        self.lower_border = FuzzyValue(lower_border)
        self.upper_border = FuzzyValue(upper_border)

    def __contains__(self, item):
        if self.lower_border.value <= item <= self.upper_border.value:
            return True

    def __add__(self, other):
        if not isinstance(other, FuzzyInterval):
            print("Невозможная операция")
        self.lower_border = FuzzyValue(max(self.lower_border.value, other.lower_border.value))
        self.upper_border = FuzzyValue(min(self.upper_border.value, other.upper_border.value))
from .Equation import *
from FuzzyLogic import Predicate


class MainEquation(dict):
    def __init__(self, consequent_name: str, predicates: Predicate.Predicate, consequent_value: FuzzyValue, composition=None):
        super().__init__()
        if isinstance(consequent_name, str):
            self.consequent_name: str = consequent_name
        else:
            invalid_type_error(self.__init__, consequent_name, str)

        if isinstance(consequent_value, FuzzyValue):
            self.consequent_value: FuzzyValue = consequent_value
        elif isinstance(consequent_value, float):
            self.consequent_value: FuzzyValue = FuzzyValue(consequent_value)
        else:
            invalid_type_error(self.__init__, consequent_value, (FuzzyValue, float))

        self.upper_operator: str = "max"
        self.lower_operator: str = "max"
        if not isinstance(predicates, Predicate.Predicate):
            invalid_type_error(self.__init__, predicates, Predicate.Predicate)
            return
        for predicate in predicates:
            if predicate[0][1] != consequent_name:
                continue
            self[predicate[0][0]] = predicate[1]

    def __repr__(self):
        return f"{self.consequent_name} = {self.upper_operator}{(str(f'{str(self.lower_operator)}({0}, {key}+{value}-1)') for key, value in self.list_of_expressions.items())}) = {self.consequent_value}"

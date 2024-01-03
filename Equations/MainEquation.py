from .Equation import *
from FuzzyLogic import Predicate


class MainEquation:
    def __init__(self, consequent_name: str, predicates: Predicate.Predicate, consequent_value: FuzzyValue, composition=None):
        self.list_of_expressions: dict = dict()
        self.consequent_name: str = consequent_name
        self.consequent_value: FuzzyValue = consequent_value
        self.keys: set = set()
        self.upper_operator: str = "max"
        self.lower_operator: str = "min"
        for predicate in predicates:
            if predicate[0][1] != consequent_name:
                continue
            self.keys.add(predicate[0][0])
            self.list_of_expressions[predicate[0][0]] = predicate[1]

    def __repr__(self):
        return f"{self.consequent_name} = {self.upper_operator}{(str(f'{str(self.lower_operator)}({0}, {key}+{value}-1)') for key, value in self.list_of_expressions.items())}) = {self.consequent_value}"

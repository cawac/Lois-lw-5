from .FuzzyValue import FuzzyValue
from .FuzzyInterval import FuzzyInterval
from functools import reduce


def equality(x, y, name):
    if x < y:
        return {name: None}
    elif x == y:
        return {name: FuzzyInterval(x, 1)}
    else:
        return {name: FuzzyInterval(y, y)}


def less_equal(x, y, name):
    if x < y:
        return {name: FuzzyInterval(0, 1)}
    elif x == y:
        return {name: FuzzyInterval(x, 1)}
    else:
        return {name: FuzzyInterval(0, y)}


operation = {"==": equality,
             "<=": less_equal}


class MainEquation:
    def __init__(self, consequent_name, list_of_predicates, consequent_value, composition=(max, min)):
        self.upper_operation = composition[0]
        self.lower_operation = composition[1]
        self.list_of_expressions = dict()
        self.consequent_name = consequent_name
        self.consequent_value = consequent_value
        for predicate in list_of_predicates:
            if predicate[0][1] != consequent_name:
                continue
            if predicate[0][0] in self.list_of_expressions:
                print("Повторяющийся предикат")
            self.list_of_expressions[predicate[0][0]] = predicate[0][1]


class Equation:
    def __init__(self, x_name, value_x, value_y, binary_operator):
        self.x_name = x_name
        self.value_x = value_x
        self.value_y = value_y
        self.binary_operator = binary_operator

    def calculate_answers(self):
        return self.binary_operator(self.value_x, self.value_y, self.x_name)


class SystemOfEquations(set):

    def __init__(self, type_of_system="or", list_of_systems=None):
        super().__init__()
        self.type_of_system = type_of_system
        if list_of_systems is not None:
            for system in list_of_systems:
                self.add(system)
        self.keys = set()

    def initialize(self, main_equation):
        if main_equation.upper_operation == max:
            for key in main_equation.list_of_expressions.keys:
                self.keys.add(key)
                temp_system_of_equations = SystemOfEquations("and")
                for x, value_x in main_equation.list_of_expressions.items():
                    if key == x:
                        temp_system_of_equations.add(
                            Equation(x, value_x, main_equation.consequent_value, operation["=="]))
                    else:
                        temp_system_of_equations.add(
                            Equation(x, value_x, main_equation.consequent_value, operation["<="]))
                if temp_system_of_equations != len(self.keys):
                    print("Невозможная операция")
                self.add(temp_system_of_equations)

    def calculate_answers(self):
        answers = {key: list() for key in self.keys}
        for item in self:
            calculated_answer = item.calculate_answers()
            if calculated_answer.values()[0] is None:
                return dict()
            answers[calculated_answer.keys()[0]].append(calculated_answer.values()[0])
        if self.type_of_system == "and":
            for key, answer in answers.items():
                answers[key] = reduce(lambda a, b: a + b, answer)

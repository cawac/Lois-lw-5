from .Equation import *
from .Answer import Answer




class SystemOfEquations:
    def __init__(self, type_of_system="and", list_of_systems=None):
        self.list_of_equations = list()
        self.type_of_system = type_of_system
        self.keys = set()
        if list_of_systems is not None:
            for systems in list_of_systems:
                self.list_of_equations.append(systems)
                self.keys.update(systems.keys)

    def add_equation(self, equation):
        self.list_of_equations.append(equation)
        self.keys.update(equation.keys)

    def add_system(self, system):
        self.list_of_equations.append(system)
        self.keys.update(system.keys)

    def initialize(self, main_equation):
        for key in main_equation.keys:
            self.keys.add(key)
            temp_system_of_equations = SystemOfEquations("and")
            for x, value_x in main_equation.list_of_expressions.items():
                if key == x:
                    temp_system_of_equations.add_equation(
                        Equation(x, value_x, main_equation.consequent_value, operation["=="]))
                else:
                    temp_system_of_equations.add_equation(
                        Equation(x, value_x, main_equation.consequent_value, operation["<="]))
            self.list_of_equations.append(temp_system_of_equations)
            if len(self.list_of_equations) != len(self.keys):
                print("Невозможная операция")

    def calculate_answers(self):
        answers = Answer(type_of_answer=self.type_of_system)
        for item in self.list_of_equations:
            answer = item.calculate_answers()
            answers.add_answer(answer)
        return answers

    def __repr__(self):
        return f"{self.type_of_system} {tuple(str(equation) for equation in self.list_of_equations)}"

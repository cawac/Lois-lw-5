# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from .FuzzyValue import FuzzyValue
from .FuzzyInterval import FuzzyInterval
from .Answer import Answer


def equality(x: float, y: float, name: str):
    if y == 0.0:
        return Answer({name: FuzzyInterval(FuzzyValue(0.0), FuzzyValue(1.0 - x))})
    elif y > x:
        return Answer()
    else:
        return Answer({name: FuzzyInterval(FuzzyValue(y - x + 1.0), FuzzyValue(y - x + 1.0))})


def less_equal(x: float, y: float, name: str):
    return Answer({name: FuzzyInterval(FuzzyValue(0.0), FuzzyValue(y - x + 1.0))})


def greater_equal():
    return


operation = {"==": equality,
             "<=": less_equal}


class MainEquation:
    def __init__(self, consequent_name: str, predicates, consequent_value: FuzzyValue, composition = None):
        self.list_of_expressions: dict = dict()
        self.consequent_name: str = consequent_name
        self.consequent_value: FuzzyValue = consequent_value
        self.keys: set = set()
        self.upper_operator: str = "max"
        self.lower_operator: str = "min"
        for predicate in predicates:
            if predicate[0][1] != consequent_name:
                continue
            if predicate[0][0] in self.list_of_expressions:
                print("Повторяющийся предикат")
            self.keys.add(predicate[0][0])
            self.list_of_expressions[predicate[0][0]] = predicate[1]

    def __repr__(self):
        return f"{self.consequent_name} = {self.upper_operator}{(str(f'{str(self.lower_operator)}({0}, {key}+{value}-1)') for key, value in self.list_of_expressions.items())}) = {self.consequent_value}"


class Equation:
    def __init__(self, x_name: str, value_x: FuzzyValue, value_y: FuzzyValue, binary_operator):
        self.x_name: str = x_name
        self.value_x: FuzzyValue = value_x
        self.value_y: FuzzyValue = value_y
        self.binary_operator = binary_operator
        self.keys: set = set()
        self.keys.add(x_name)

    def calculate_answers(self):
        return self.binary_operator(self.value_x.value, self.value_y.value, self.x_name)

    def __str__(self):
        op = str()
        if self.binary_operator == equality:
            op = "=="
        elif self.binary_operator == less_equal:
            op = "<="
        return f"max(0, {self.x_name} + {self.value_x} - 1) {op} {self.value_y}"


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
        return f"{self.type_of_system} { tuple( str(equation) for equation in self.list_of_equations ) }"
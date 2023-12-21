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
from functools import reduce


def equality(x, y, name):
    if x < y:
        return None
    elif x == y:
        return {name: FuzzyInterval(x, 1)}
    else:
        return {name: FuzzyInterval(y, y)}


def less_equal(x, y, name):
    if x < y:
        return {name: FuzzyInterval(0, 1)}
    elif x == y:
        return {name: FuzzyInterval(0, 1)}
    else:
        return {name: FuzzyInterval(0, y)}


operation = {"==": equality,
             "<=": less_equal}

class MainEquation:
    def __init__(self, consequent_name, list_of_predicates, consequent_value):
        self.list_of_expressions = dict()
        self.consequent_name = consequent_name
        self.consequent_value = consequent_value
        self.keys = set()
        for predicate in list_of_predicates:
            if predicate[0][1] != consequent_name:
                continue
            if predicate[0][0] in self.list_of_expressions:
                print("Повторяющийся предикат")
            self.keys.add(predicate[0][0])
            self.list_of_expressions[predicate[0][0]] = predicate[1]


class Equation:
    def __init__(self, x_name, value_x, value_y, binary_operator):
        self.x_name = x_name
        self.value_x = value_x
        self.value_y = value_y
        self.binary_operator = binary_operator
        self.keys = set()
        self.keys.add(x_name)

    def calculate_answers(self):
        return self.binary_operator(self.value_x.value, self.value_y.value, self.x_name)


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
        answers = dict()
        if self.type_of_system == "and":
            answers = {key: list() for key in self.keys}
            for item in self.list_of_equations:
                answer = item.calculate_answers()
                if isinstance(answer, list):
                    bAdded = True
                    index = 1
                    while bAdded:
                        key = "answer" + str(index)
                        if key not in answers:
                            answers[key] = answer
                            bAdded = False
                        else:
                            index += 1
                    continue
                if answer is None:
                    return dict()
                for key, value in answer.items():
                    if key in answers:
                        answers[key].append(value)
                    else:
                        answers[key] = list(value)
            answers = {key: value for key, value in answers.items() if value}
            for key in answers:
                if not key.startswith('answer'):
                    answers[key] = reduce(lambda a, b: a * b, answers[key])
        elif self.type_of_system == "or":
            answers = list()
            for item in self.list_of_equations:
                answer = item.calculate_answers()
                if answer not in answers and answer:
                    answers.append(answer)
            if len(answers) == 1:
                return answers[0]
        for key, value in answers:
            if key.startswith("answer"):


        return answers

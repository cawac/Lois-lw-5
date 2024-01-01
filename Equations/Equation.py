# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from FuzzyLogic.FuzzyValue import FuzzyValue
from FuzzyLogic.FuzzyInterval import FuzzyInterval
from Equations.Answer import Answer


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



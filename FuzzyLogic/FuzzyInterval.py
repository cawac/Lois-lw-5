# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


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

    # def __add__(self, other):
    #     if not isinstance(other, FuzzyInterval):
    #         print("Невозможная операция")
    #     self.lower_border = FuzzyValue(max(self.lower_border.value, other.lower_border.value))
    #     self.upper_border = FuzzyValue(min(self.upper_border.value, other.upper_border.value))

    def __mul__(self, other):
        if not isinstance(other, FuzzyInterval):
            print("Невозможная операция")
        self.lower_border = FuzzyValue(max(self.lower_border.value, other.lower_border.value))
        self.upper_border = FuzzyValue(min(self.upper_border.value, other.upper_border.value))

    def __repr__(self):
        return str(self)
    def __str__(self):
        if self.lower_border.value == self.upper_border.value:
            return "{" + str(self.upper_border) + "}"
        else:
            return "[" + str(self.lower_border) + "," + str(self.upper_border) + "]"

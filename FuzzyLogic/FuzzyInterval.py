# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from .FuzzyValue import FuzzyValue
from .functions import invalid_type_error


class FuzzyInterval:
    def __init__(self, lower_border: FuzzyValue, upper_border: FuzzyValue) -> None:
        if upper_border < lower_border:
            upper_border, lower_border = lower_border, upper_border

        if isinstance(lower_border, FuzzyValue):
            self.lower_border: FuzzyValue = lower_border
        elif isinstance(lower_border, float):
            self.lower_border: FuzzyValue = FuzzyValue(lower_border)
        else:
            invalid_type_error(self.__init__, lower_border, FuzzyValue)

        if isinstance(upper_border, FuzzyValue):
            self.upper_border: FuzzyValue = upper_border
        elif isinstance(upper_border, float):
            self.upper_border: FuzzyValue = FuzzyValue(upper_border)
        else:
            invalid_type_error(self.__init__, upper_border, FuzzyValue)

    def __contains__(self, item: FuzzyValue) -> bool:
        if isinstance(item, (FuzzyValue, float)):
            return self.lower_border <= item <= self.upper_border
        else:
            invalid_type_error(self.__contains__, item, FuzzyValue)

    def __mul__(self, other):
        if other is None:
            return None
        if isinstance(other, FuzzyInterval):
            if self.lower_border <= other.upper_border and other.lower_border <= self.upper_border:
                return FuzzyInterval(max(self.lower_border, other.lower_border),
                                     min(self.upper_border, other.upper_border))
            else:
                return None
        else:
            invalid_type_error(self.__mul__, other, FuzzyInterval)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.lower_border.value == self.upper_border.value:
            return "{" + str(self.lower_border) + "}"
        else:
            return "[" + str(self.lower_border) + ", " + str(self.upper_border) + "]"

    def __eq__(self, other) -> bool:
        if isinstance(other, FuzzyInterval):
            return self.lower_border.value == other.lower_border.value \
                and self.upper_border.value == other.upper_border.value
        else:
            invalid_type_error(self.__eq__, other, FuzzyInterval)

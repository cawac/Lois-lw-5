# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from .functions import invalid_type_error


class FuzzyValue:
    def __init__(self, value: float):
        if isinstance(value, float):
            self.value: float = max(0.0, min(1.0, round(value, 8)))
        else:
            invalid_type_error(self.__init__, value, float)

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        if isinstance(other, FuzzyValue):
            return self.value < other.value
        else:
            invalid_type_error(self.__lt__, other, FuzzyValue)

    def __le__(self, other):
        if isinstance(other, FuzzyValue):
            return self.value <= other.value
        else:
            invalid_type_error(self.__le__, other, FuzzyValue)

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


class FuzzySet(set):
    def add(self, element, fuzzy_value: FuzzyValue) -> None:
        for item in self:
            if item[0] == element:
                return
        if isinstance(fuzzy_value, FuzzyValue):
            super().add((element, fuzzy_value))
        elif isinstance(fuzzy_value, float):
            super().add((element, FuzzyValue(fuzzy_value)))
        else:
            invalid_type_error(self.__init__, fuzzy_value, FuzzyValue)

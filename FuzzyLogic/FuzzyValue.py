# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


# operations = {
#     't_norm': lambda val1, val2: FuzzyValue(val1.value * val2.value),
#     'implication': lambda val1, val2: FuzzyValue(1) if val1.value <= val2.value else FuzzyValue(val2.value / val1.value)
# }


class FuzzyValue:
    def __init__(self, value):
        self.value = max(0.0, min(1.0, value))

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

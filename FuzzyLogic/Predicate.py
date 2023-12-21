# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from .FuzzySet import FuzzySet


class Predicate(FuzzySet):
    def __init__(self, set1=None, set2=None, implication=None, predicate=None):
        super().__init__()

        if predicate:
            for i, j in predicate:
                self.add((i[0], i[1]), j)
        else:
            for element_from_set1 in set1:
                for element_from_set2 in set2:
                    self.add(
                        (element_from_set1[0], element_from_set2[0]),
                        implication(element_from_set1[1], element_from_set2[1])
                    )

    @property
    def image(self):
        return {item[0][1] for item in self}
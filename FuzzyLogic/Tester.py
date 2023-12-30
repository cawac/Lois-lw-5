# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from .FuzzyEntityController import FuzzyEntityController
from unittest import TestCase
from .FuzzyInterval import FuzzyInterval
from .FuzzyValue import FuzzyValue


class Tester(TestCase):
    def test_all(self, consequents, predicates):
        self.test_expression(consequents["Y1"], predicates["P1"],
                             {"x1": FuzzyInterval(FuzzyValue(0.8), FuzzyValue(0.8))})
        self.test_expression(consequents["Y3"], predicates["P3"],
                             {"x1": FuzzyInterval(FuzzyValue(0.9), FuzzyValue(0.9))})
        self.test_expression(consequents["Y4"], predicates["P4"],
                             {"x1": FuzzyInterval(FuzzyValue(0.0), FuzzyValue(1.0)),
                              "x2": FuzzyInterval(FuzzyValue(1.0), FuzzyValue(1.0))})

    def test_expression(self, consequent, predicate, excepted):
        answers = FuzzyEntityController.calculate_answer(consequent, predicate)
        self.assertEqual(answers, excepted)

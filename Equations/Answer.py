# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from FuzzyLogic.FuzzyInterval import FuzzyInterval
from FuzzyLogic.functions import invalid_type_error
from itertools import permutations
from functools import reduce

class Answer(dict):
    def __init__(self, intervals=None, solutions=None, type_of_answer=None):
        super().__init__()
        if solutions is None:
            solutions = list()
            self.solutions = solutions
        if intervals is None:
            intervals = dict()
        if type_of_answer is None:
            type_of_answer = "and"
        self.type_of_answer = type_of_answer
        for key, value in intervals.items():
            self[key] = value
        self.have_solution = True

    def add_answer(self, answer):
        if isinstance(answer, Answer):
            if not self.have_solution:
                return
            if self.type_of_answer == "or":
                if answer.have_solution:
                    self.add_solution(answer)
            elif self.type_of_answer == "and":
                if answer.is_empty() or not answer.have_solution:
                    self.have_solution = False
                elif answer.solutions:
                    self.add_solution(answer)
                elif answer:
                    self.add_interval(answer)

    def add_interval(self, answer):
        if not isinstance(answer, dict):
            invalid_type_error(self.add_interval, answer, dict)
        for variable, interval in answer.items():
            if variable in self:
                self[variable] *= interval
            else:
                self[variable] = interval
            if self[variable] is None:
                self.have_solution = False

    def add_solution(self, solution):
        if not isinstance(solution, Answer):
            invalid_type_error(self.add_interval, solution, Answer)
        else:
            bFinded = False
            for solution1 in self.solutions:
                if solution1 == solution:
                    bFinded = True
                    break
            if not bFinded:
                self.solutions.append(solution)

    def is_empty(self):
        return not self and not self.solutions

    def reduce(self):
        # self.answers = [answer for answer in self.answers if answer.have_solution]
        for answer in self.solutions:
            answer.reduce()
        if self.type_of_answer == "and":
            if not self.solutions:
                return
            for key, value in self.items():
                for answer in self.solutions:
                    if key in answer:
                        answer[key] *= value
                    else:
                        answer[key] = value
                    if answer[key] is None:
                        answer.have_solution = False
            super().clear()
        return

    def __repr__(self):
        result = str()
        for key in sorted(self):
            result += f"{key + ' э ' + str(self[key])}" + '\n'
        for answer in self.solutions:
            if answer.type_of_answer == "and":
                result += "{" + str(answer) + "}\n"
            elif answer.type_of_answer == "or":
                result += "[" + str(answer) + "]\n"
        return '\n' + result

    def clear(self) -> None:
        super().clear()
        self.solutions = None

    def combinations(self):
        result = Answer()
        # solutions = (lower_solution for solution in self.solutions for lower_solution in solution)
        # for answer in permutations(solutions):
        #     temp_answer = reduce(lambda a, b: )
        #     result.add_solution()

    def __eq__(self, other):
        if len(self) == len(other) and len(self.solutions) and len(other.solutions):
            for key in self:
                if key not in other:
                    return False
            for solution in self.solutions:
                bFinded = False
                for solution2 in other.solutions:
                    if solution == solution2:
                        bFinded = True
                        break
                if not bFinded:
                    return False
            return True
        return False

    def multiplication(self, other):
        pass
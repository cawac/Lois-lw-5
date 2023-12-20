# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 6 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({min({xi}U{yi})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)

class FuzzyCounter:
    def __init__(self):
        self.__reference_consequent = {}
        self.__consequent = {}
        self.__antecedent = []

    def __str__(self):
        formatted_string = 'Решение:\n'
        l = len(self.__antecedent) - 1
        for solution in self.__antecedent:
            for i, value in enumerate(solution):
                if isinstance(value, tuple):
                    formatted_string += f'x{i + 1} ∈ [{value[0]}, {value[1]}]\n'
                else:
                    formatted_string += f'x{i + 1} = {value}\n'
            if l:
                formatted_string += 'ИЛИ\n'
                l -= 1
        formatted_string += '=======================\n'
        return formatted_string

    def solver(self, ai, y):
        answer = []
        curr_main_index = 0
        for a_main in ai:
            curr_main_index += 1
            curr_secondary_index = 0
            curr_answer = []

            for a_secondary in ai:
                curr_secondary_index += 1

                if curr_main_index == curr_secondary_index:
                    if a_main > y:
                        curr_answer.append(y)
                    if a_main == y:
                        curr_answer.append(tuple([y, 1]))
                else:
                    if a_secondary > y:
                        curr_answer.append(tuple([0, y]))
                    if a_secondary == y or a_secondary < y:
                        curr_answer.append(tuple([0, 1]))

            if a_main >= y and curr_answer:
                answer.append(curr_answer)
        return answer

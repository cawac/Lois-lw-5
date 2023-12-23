# Лабораторная работа 5 по дисциплине ЛОИС
# Выполнена студентами группы 021702 БГУИР
# Свиридовой М. О., Платоновым А. В. и Войшнис М. А.
# Вариант 8 - Реализация обратного нечёткого логического вывода на основе операции нечёткой композиции (max({max({0}U{xi+yi-1})|i}))
# 20.12.2023
# Использованные материалы:
# Нечеткая логика: алгебраические основы и приложения(Блюмин, Шуйкова)
# Логические основы интеллектуальнвых систем. Практикум:учебно-метод. пособие(Голенков В.В., Ивашенко В.П.)


from FuzzyLogic import Equation, FuzzyEntityController

menu = ("1- Вычесилить анцедент\n"
        "2- Добавить нечёткое множество\n"
        "3- Добавить предикат\n"        
        "exit- Выход\n")

if __name__ == "__main__":
    fuzzy_entity_controller = FuzzyEntityController.FuzzyEntityController()
    all_sets = fuzzy_entity_controller.read_sets_from_file("sets.json")
    all_predicates = fuzzy_entity_controller.read_predicates_from_file("predicates.json")
    while True:
        choice = input(menu)
        match choice:
            case "1":
                for set_name, fuzzy_set in all_sets.items():
                    print(set_name, ":", fuzzy_entity_controller.get_text_of_fuzzy_set(fuzzy_set))

                choiced_consequent = input("Выберите консеквент: ")
                consequent = all_sets[choiced_consequent]

                for predicate_name, predicate in all_predicates.items():
                    print(predicate_name, ":", fuzzy_entity_controller.get_text_of_fuzzy_predicate(predicate))

                choiced_predicate = input("Выберите предикат: ")
                predicate = all_predicates[choiced_predicate]

                main_system_of_equations = Equation.SystemOfEquations("and")
                for consequen in consequent:
                    main_equation = Equation.MainEquation(consequen[0], predicate, consequen[1])
                    system_of_equations = Equation.SystemOfEquations("or")
                    system_of_equations.initialize(main_equation)
                    main_system_of_equations.add_system(system_of_equations)
                answers = main_system_of_equations.calculate_answers()
                print("Решение: ", answers)
                # if len(matrix) != len(my_fuzzy_counter.consequent.values()):
                #     raise ValueError("Длина правила и консеквента не совпадают.")

            case "2":

                input_string2 = input(
                    "Введите эталонный консеквент(числа из промежутка [0; 1]. Дробную часть отделять точкой, "
                    "новый элемент - пробелом. Пример: x1:0.1 x2:0.2):\n")

            case "3":
                fuzzy_entity_controller
            case "exit":
                break
            case _:
                print("Выберите пункт меню")

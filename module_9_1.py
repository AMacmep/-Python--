# Домашнее задание по теме "Введение в функциональное программирование"
def apply_all_func(int_list, *functions):
    results = {}

    for functions_n in functions:
        results[functions_n.__name__] = functions_n(int_list)
    return results


def min(list1: int): #Переопределил встроенную функцию min
    min_number = list1[0]
    for number in list1:
        if min_number <= number:
            continue
        else:
            min_number = number
    return min_number


list1 = [1, 2, -3, -6, 5, 4, ]

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
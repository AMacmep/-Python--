# Домашнее задание по теме "Try и Except".
def add_everything_up(a, b):
    try:
        summ = a + b
        return summ
    except (TypeError):
        summ = str(a) + str(b) #'Сложение после перевода в строку ',
        return summ


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

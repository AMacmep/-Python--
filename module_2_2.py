#Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = int(input("Введите первое число "))
second = int(input("Введите второе число "))
third = int(input("Введите третье число "))
if first == second and second==third:
    consilience = 3
elif first==second or first== third or second==third:
    consilience = 2
else:
    consilience = 0
print("Количество повторяющихся чисел: ", consilience)










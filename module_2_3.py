#Домашняя работа по уроку "Стиль кода часть II. Цикл While."
my_list=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index=0
while index <=len(my_list):
    if my_list[index] > 0:
        print(my_list[index])
    if my_list[index] < 0:
        break
    index +=1

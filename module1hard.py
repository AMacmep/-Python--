#Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=sorted(list(students)) #Переводим множество в список и сортируем, чтобы можно было обращаться к элементам по индексу
academik_report={}#создаем словарь
for N in range(len(students_list)):#цикл для работы с элементами списков
    avg = sum(grades[N]) / len(grades[N])
    academik_report.update({students_list[N]: avg})
print(academik_report)
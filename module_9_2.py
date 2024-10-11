# Домашнее задание по теме "Списковые, словарные сборки"
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(n) for n in first_strings if len(n) >= 5]
print(first_result)
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)
summar_strings = first_strings + second_strings
third_result = {(a): len(a) for a in summar_strings if len(a) % 2 == 0}
print(third_result)

# Домашнее задание по теме "Позиционирование в файле".
def custom_write(file_name, strings):
    strings_pozitions = {(1, 0): ""}
    low = 0

    work_file = open(file_name, 'w', encoding='utf-8')
    work_file.write('')
    work_file.close()
    work_file = open(file_name, 'a', encoding='utf-8')
    for list_string in strings:
        low += 1
        bite_pozition = work_file.tell()
        strings_pozitions.update({(low, bite_pozition): list_string})
        work_file.write(list_string + '\n')
    work_file.close()
    return strings_pozitions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

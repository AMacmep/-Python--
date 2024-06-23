#Практическое задание по теме: "Словари и множества"
#2. Работа со словарями:
my_dict={'one': 2001, 'two': 2002, 'three': 2003, 'four': 2004}
print(my_dict)
print(my_dict['two'])
print(my_dict.get('three'))
print(my_dict.get('five'))
my_dict.update({'five': 2005,
               'sex': 2006})
print(my_dict.pop('three'))
print(my_dict)
#Работа с множествами:
my_set ={' ', 1, 'two', '3', True, True, 2, 'two', 1, False, 1, '3', 3, (5, 6, 7)}
print(my_set)
my_set.update({'four', 4})
print(my_set.discard(1))
print(my_set)
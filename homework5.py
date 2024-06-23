#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
immutable_var =[1, '2','three',False], 4, 'five',True #Задаем неизменяемый объект - кортеж
print(type(immutable_var))
print(immutable_var)
#immutable_var[1]='six' #Выдает ошибку,так как кортеж (tuple) не изменяемый
#immutable_var.append('seven') #Выдает ошибку,так как кортеж (tuple) не изменяемый
immutable_var[0][0]='one' # При этом, есть возможность изменить данные списка включенного в кортеж
print(immutable_var)
mutable_list =[[1, '2','three',False], 4, 'five',True] #Задаем изменяемый список
print(type(mutable_list))
print(mutable_list)
mutable_list[1]='six'
mutable_list.append('seven')
mutable_list[0][3]=8
print(mutable_list)
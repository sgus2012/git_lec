from xmlrpc.client import boolean


#Типы переменных:

#int - целые числа
#float - числа с плавующей точкой 
#boolean - логические переменные (True, False)
#str - строки
#list - списки

#примеры переменных
#Если мы ставим пустую переменную value перед кодом , то мы должны приравнять ее к None
value = None
a = 123
b = 1.23
c = "Сергей"
print(a)
print(b)
print(c)
value = 12345
print(value)

#Находим тип данных
value = None
a = 123
b = 1.23
c = "Сергей"
print(type(a))
print(type(b))
print(type(c))
value = 12345
print(type(value))

# \n - это новая строка

print (a,b,c) # Вывод перменных в строку без знаков препинания

print (a, '-',b,'-',c) # Вывод переменных в строку со знаками препенания (Вариант 1)
print ('{} - {} - {}'.format(a,b,c)) # Вывод переменных в строку со знакоми препинания (Вариант 2)
print ('{1} - {2} - {0}'.format(a,b,c)) # Изменения порядка значений
print (f'{a} - {b} - {c}') # Вывод переменных в строку с любым типом переменных (Вариант 3 (Интерпаляция))


f = True
print(f)

list = ['1','2','Сергей',1,2,3,4.5, True] # Список\Массив.Лучше использовать для каждого типа отдельный список.
col = [1,2,3]
print(list)
print(col)


# print() - отвечает за вывод данных
# input() - отвечает за ввод данных

print('Введите a');  # пример без арифмитических действий
a=input();
print('Введите b');
b=input()
print(a,b)
print('{} {}'.format(a,b))
print(f'{a} {b}')

print('Введите a');  # пример с арифмитических действий (Целые числа)
a=int(input());   # добавляем int
print('Введите b');
b=int(input());   # добавляем itn  
print(a + b)      # добавляем арифмитический знак
print('{} {}'.format(a,b))
print(f'{a} {b}')

print('Введите a');  # пример с арифмитических действий (Вещественные числа)
a=float(input());   # добавляем float
print('Введите b');
b=float(input());   # добавляем float  
print(a - b)      # добавляем арифмитический знак
print('{} {}'.format(a,b))
print(f'{a} {b}')

# Функция round окрукляет значения при арифмитических действиях
# например 1.3 * 3 = 3.900000004, но  round(1.3*3) = 4 или round(1.3*3 , 5) = 3.9000


a = 3   # Сокращенные операции 
a += 5
print(a)
 

a = 1 > 4 #логические операции
print(a) # - false

a = 1 < 4 and 5 > 2
print(a) # - True

a = 1 > 2 or 4 < 6
print(a) # - True

a = [1 , 2 , 3 , 4]
print(a)
print(2 in a) # - True
print(not 2 in a) # - False

is_odd = a[0] % 2 == 0
print(is_odd) # - False
# И т.д



 
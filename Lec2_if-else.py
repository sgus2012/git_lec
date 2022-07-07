#if, if-else

import weakref


a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:    
    print(b)


# if, if-elif

username = input('Введите имя; ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждал вас, Марина!')
elif username == 'Ильна':
    print('Ильнар - топ')
else:
    print('Привет, ', username)


# ЦИКЛЫ
# цикл while
original = 23 # инвертация чисел (23) в нашем случае
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)    


# конструкция for

for i in 1,2,3,4,5:   #возведение в квадрат все перечисленные числа
    print(i**2)



list = [1,2,3,4,21,6]   #возведение в квадрат списка
for i in list:
    print(i**2)


r = range(10)   # Перечисление всех чисел от 0 до (10) 9
for i in r:
    print(i)


r = range(1, 10)   # Перечисление всех чисел от 1 до (10) 9
for i in r:
    print(i)

    r = range(1, 10, 2)   # Перечисление всех чисел от 1 до (10) 9, где (2) - это шаг
for i in r:
    print(i)

# все прописанное ранее можно употреблять и со строками 



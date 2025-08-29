# считывает три числа и подсчитывает сумму только положительных чисел.

a = int(input())
b = int(input())
c = int(input())

if a > 0:
    a = a
else:
    a = 0
if b > 0:
    b = b
else:
    b = 0
if c > 0:
    c = c
else:
    c = 0
print(a + b + c)

a, b, c = int(input()), int(input()), int(input())
total = 0
if a > 0:
    total = total + a
if b > 0:
    total = total + b
if c > 0:
    total = total + c
print(total)

answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')

word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')

num = int(input())

last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа
if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')

# Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  # переменная счётчик
if num1 % 2 == 0:  # если четное число-делится на 2 без остатка, добавляем в переменную счетчик.
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:  # если нечетное число не делится на 2 без остатка, в переменную не добавляем.
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1

print(counter)

password1 = input()
password2 = input()

if password1 == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')

num = int(input())  # для заданного четырехзначного числа выполняется следующее соотношение:
part_of_a_num4 = num % 10  # сумма первой и последней цифр равна разности второй и третьей цифр
part_of_a_num3 = num // 10 % 10
part_of_a_num2 = num // 100 % 10
part_of_a_num1 = num // 1000 % 10

point1 = (part_of_a_num1) + (part_of_a_num4)
point2 = (part_of_a_num2) - (part_of_a_num3)

if point1 == point2:
    print('ДА')
else:
    print('НЕТ')

# являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num2 - num1 == num3 - num2:
    print('YES')
else:
    print('NO')

# определяет наименьшее из двух чисел
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num2)
else:
    print(num1)

num1 = int(input())  # наименьшее из четырёх чисел
num2 = int(input())
num3 = int(input())
num4 = int(input())

point = min(num1, num2, num3, num4)
print(point)

#  наименьшее из четырёх чисел
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a < b:
    min_ab = a
else:
    min_ab = b

if c < d:
    min_cd = c
else:
    min_cd = d

if min_ab < min_cd:
    min_abcd = min_ab
else:
    min_abcd = min_cd

print(min_abcd)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
# Создаётся специальная переменная (m), которая будет хранить минимальное значение (минимум),
# сравниваясь со всеми введёнными числами поочерёдно.
m = a      # I число сравнивать не с чем, поэтому оно прямо записывается в спец. переменную.
if b < m:  # Сравнивается II число со спец. переменной.
    m = b  # Если II число меньше, чем значение спец. переменной, то текущий минимум обновляется.
if c < m:  # Сравнивается III число со спец. переменной... И далее поочерёдно перебираются все числа
    m = c  # Если очередное число меньше, чем значение спец. переменной, то текущий минимум обновляется,
if d < m:  # иначе специальная переменная, содержащая текущий минимум остаётся без изменений.
    m = d  #
print(m)   # Вывод "накопленного результата" в процессе сравнения всех чисел.

# по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
num = int(input())

if num <= 13:
    print('детство')
elif 14 <= num <= 24:
    print('молодость')
elif 25 <= num <= 59:
    print('зрелость')
elif num >= 60:
    print('старость')

num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')

# программа, которая проверяет, что все три цифры натурального трёхзначного числа различны.
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')

# координатам точки, не лежащей на осях координат,
# определяется номер четверти, в которой она находится.
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

# второй вариант решения про координаты
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')


num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')

a = int(input())


x = int(input())

if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())

if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')


x = int(input())

if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Является ли год с данным номером високосным.
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет,
# может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа
# от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES» (без кавычек), если из первой клетки ходом ладьи можно попасть во вторую,
# или «NO» (без кавычек) в противном случае.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a == c) or (b == d):
    print('YES')
else:
    print('NO')

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли король
# попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES» (без кавычек), если из первой клетки ходом короля можно попасть во вторую,
# или «NO» (без кавычек) в противном случае.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = c - a
y = d - b

if (-1 <= x <= 1) and (-1 <= y <= 1):
    print('YES')
else:
    print('NO')

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == c or a == c - 1 or a == c + 1) and (b == d or b == d + 1 or b == d - 1):
    print("YES")
else:
    print("NO")

traffic_light_signal = input('Введите сигнал светофора: ')

if traffic_light_signal == 'красный':
    print('Стой!')
elif traffic_light_signal == 'желтый':
    print('Приготовься...')
elif traffic_light_signal == 'зеленый':
    print('Иди!')
# Даны три целых числа, сколько среди них совпадающих: 3 (если все совпадают), 2 (если два совпадает)
# или 0 (если все числа различны).
a, b, c = int(input()), int(input()), int(input())

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

# Даны три различных целых числа. Найти серединное значение из этих чисел.
a = int(input())
b = int(input())
c = int(input())

if a > b > c or a < b < c:
    print(b)
elif a > c > b or a < c < b:
    print(c)
else:
    print(a)

month = int(input())
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)

# Программа, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических операций ('+', '-', '*',' /'),
# то выведите результат применения этой операции к введённым ранее числам,
# в противном случае выведите «Неверная операция» (без кавычек).
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!» (без кавычек).
a = int(input())
b = int(input())
n = input()

if n == '+':
    print(a + b)
elif n == '-':
    print(a - b)
elif n == '*':
    print(a * b)
elif n == '/' and b == 0:
    print('На ноль делить нельзя!')
elif n == '/':
    print(a / b)
else:
    print('Неверная операция')

# Программа, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести
# название вторичного цвета, который получится в результате.
color1 = input()
color2 = input()

if color1 == 'красный' and color2 == 'синий':
    print('фиолетовый')
elif color1 == 'синий' and color2 == 'красный':
    print('фиолетовый')
elif color1 == 'синий' and color2 == 'желтый':
    print('зеленый')
elif color1 == 'желтый' and color2 == 'синий':
    print('зеленый')
elif color1 == 'желтый' and color2 == 'красный':
    print('оранжевый')
elif color1 == 'красный' and color2 == 'желтый':
    print('оранжевый')
elif color1 == 'красный' and color2 == 'красный':
    print('красный')
elif color1 == 'желтый' and color2 == 'желтый':
    print('желтый')
elif color1 == 'синий' and color2 == 'синий':
    print('синий')
else:
    print('ошибка цвета')

a, b = input(), input()

if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
    print('оранжевый')
elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
    print('зеленый')
elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
    print(a)
else:
    print('ошибка цвета')

n, m = input(), input()
R = 'красный'
B = 'синий'
Y = 'желтый'
if n not in (R, B, Y) or m not in (R, B, Y):
    print('ошибка цвета')
elif n == m:
    print(n)
elif (n == R and m == B) or (n == B and m == R):
    print('фиолетовый')
elif (n == R and m == Y) or (n == Y and m == R):
    print('оранжевый')
else:
    print('зеленый')

# На колесе рулетки карманы пронумерованы от 0 до 36. Программа, которая считывает номер кармана и показывает,
# является ли этот карман зеленым, красным или черным. Программа должна вывести сообщение об ошибке,
# если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
x = int(input())

if x > 36 or x < 0:
    print('ошибка ввода')
elif x == 0:
    print('зеленый')
elif 1 <= x <= 10:
    if x % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= x <= 18:
    if x % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= x <= 28:
    if x % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= x <= 36:
    if x % 2 == 0:
        print('красный')
    else:
        print('черный')


# На числовой прямой даны два отрезка:[a1,b1], [a2, b2].
# Найти их пересечение, если это: отрезок, точка, пустое множество.
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
# a1 < b1
# a2 < b2

if b1 < a2 or b2 < a1:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a2 > a1 and b2 < b1:
    print(a2, b2)
elif a1 > a2 and b2 > b1:
    print(a1, b1)
elif a1 < a2 and b1 == b2:
    print(a2, b2)
elif a1 == a2 and b2 < b1:
    print(a2, b2)
elif a1 == a2 and b1 == b2:
    print(a1, b1)
elif a1 == a2 and b2 > b1:
    print(a1, b1)
elif a2 < a1 and b1 == b2:
    print(a1, b1)
elif a1 < a2 and b1 < b2 and a2 < b1:
    print(a2, b1)
elif a2 < a1 and b2 < b1 and a1 < b2:
    print(a1, b2)

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a2 < a1:
    # теперь отрезок a1, b1 точно левее (по крайней мере своим левым концом) отрезка a2, b2
    a1, b1, a2, b2 = a2, b2, a1, b1

if a2 > b1:
    print("пустое множество")
elif a2 == b1:
    print(a2)
else:
    if b1 < b2:
        print(a2, b1)
    else:
        print(a2, b2)

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
else:
    if a1 > a2:
        a2 = a1
    if b1 > b2:
        b1 = b2
    if a2 == b1:
        print(a2)
    else:
        print(a2, b1)


a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((a + b) % 2 == 0) and ((c + d) % 2 == 0):
    print('YES')
elif ((a + b) % 2 != 0) and ((c + d) % 2 != 0):
    print('YES')
else:
    print('NO')

# Напишите программу, которая упорядочивает три числа от большего к меньшему.
a, b, c = int(input()), int(input()), int(input())

d = max(a, b, c)
e = min(a, b, c)
f = ((a + b + c) - (d + e))
print(d)
print(f)
print(e)

# Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется
# средней по величине цифре.
n = int(input())

a = n % 10
b = n // 10 % 10
c = n // 100 % 10
d = max(a, b, c)
e = min(a, b, c)
f = (a + b + c) - (d + e)

if f == d - e:
    print('Число интересное')
else:
    print('Число неинтересное')

# "Манхэттенское" расстояние между двумя точками, координаты которых заданы.
p1 = int(input())
q1 = int(input())
p2 = int(input())
q2 = int(input())

m = abs(p1 - q1)
n = abs(p2 - q2)
print(m + n)

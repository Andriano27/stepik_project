# Напишите функцию draw_triangle(), которая выводит звёздный равнобедренный треугольник
# с основанием и высотой, равными 15 и 8 соответственно
def draw_triangle():
    for i in range(8):
        print(' ' * (8 - 1 - i) + '*' * (1 + i * 2))
draw_triangle()

def draw_triangle():
    m = 15
    for i in range(1, m + 1, 2):
        print(' ' * ((m - i) // 2) + '*' * i)
draw_triangle()

# Интернет-магазин осуществляет экспресс доставку для своих товаров по цене 1000 рублей за первый товар и
# 120 рублей за каждый последующий товар. Напишите функцию get_shipping_cost(quantity), которая принимает
# в качестве аргумента натуральное число quantity – количество товаров в заказе – и возвращает стоимость
# доставки.
def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120
n = int(input())
print(get_shipping_cost(n))

# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа
# n и k и возвращает значение биномиального коэффициента
# Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть:
# n!=1⋅2⋅3⋅…⋅n
from math import *
def compute_binom(n, k):
    return int(factorial(n)/(factorial(k) * factorial(n - k)))
n = int(input())
k = int(input())
print(compute_binom(n, k))

def factorial(m):
    c = 1
    for i in range(1, m+1):
        c *= i
    return c
def compute_binom(n, k):
    return (factorial(n)/(factorial(k)*(factorial(n-k))))
n = int(input())
k = int(input())
print(compute_binom(n, k))

# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num
# и возвращает его словесное описание на русском языке. Число 1≤num≤99.
def number_to_words(num):
    s = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', '']
    s2 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num <= 20:
        return s[num - 1]
    else:
        return s2[num // 10 - 2] + ' ' + s[num % 10 - 1]
n = int(input())
print(number_to_words(n))

# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык
# ru или en и number – номер месяца (от 1 до 12 включительно) и возвращает название месяца
# на русском или английском языке.
def get_month(language, number):
    months_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    months_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return months_ru[number - 1]
    return months_en[number - 1]
lan = input()
num = int(input())
print(get_month(lan, num))

# Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними
# двумя цифрами года. Напишите функцию is_magic(date), которая принимает в качестве аргумента
# строковое представление корректной даты и возвращает значение True, если дата является магической,
# или False в противном случае.
def is_magic(date):
    s = date.split('.')
    if int(s[0]) * int(s[1]) == int(s[2]) % 100:
        return True
    return False
date = input()
print(is_magic(date))

# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации
# шрифтов, чтобы можно было в одной фразе рассмотреть все глифы. Напишите функцию is_pangram(text),
# которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True,
# если текст является панграммой, или False в противном случае.
def is_pangram(text):
    s_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.replace(' ', '')
    text = text.lower()
    for i in s_list:
        if i not in text:
            return False
    return True
text = input()
print(is_pangram(text))

def is_pangram(text):
    for i in range(97,123):
        if not chr(i) in text.lower():
            return False
    return True
text = input()
print(is_pangram(text))

flag = True   # флажок поднят
while flag:   # пока флажок True, цикл работает
    text = input("Введите слово (или 'стоп'): ")
    if text == "стоп":
        flag = False   # опускаем флажок → цикл остановится
    else:
        print("Вы ввели:", text)

total = 1
while total < 10:
    num = int(input())
    total *= num
    print(total)

num = int(input())
total = 0
while abs(num) <= 5:
    total += num
    num = int(input())
print(total)

name = input()
while len(name) > 3:
    name = input()
print(name)

language = 'Русский'
if language != 'English' != 'Español':
    print('Язык по умолчанию не является ни английским, ни испанским')
if language != 'English' != 'Русский':
    print('Язык по умолчанию не является ни английским, ни русским')

a = 4
b = -5
c = 2 * a + b
d = (a - b) // 4
e = 3 * (a + b)
f = a % 5 + b
g = a * b + 21
print(c, d, e, f, g)

a = 2.5
b = 3
c = b / 2
d = a ** 2
e = (2 * a + b) / 2
f = a // b
g = (a + 2 * b) % 2
print(c, d, e, f, g)

for i in range(3):
    print(0, end='+')

for i in range(2):
    print('we will')
print('rock you')

for i in range(4):
    print(i, end='*')

for i in range(4):
    j = i + 1
    print(i, j)

total = 0
for i in range(3):
    total = total - i
    print(total)

total = 0
for i in range(10):
    total = total + i
    if i == 9:
        total = 1
print(total)

# Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты
# концов отрезка (x1; y1), (x2; y2) и возвращает координаты точки являющейся серединой данного отрезка.
def get_middle_point(x1, y1, x2, y2):
    a = (x_1 + x_2)/2
    b = (y_1 + y_2)/2
    return a, b
# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())
# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и
# возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
import math
def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * (radius ** 2)
    return c, s
# считываем данные
r = float(input())
# вызываем функцию
length, square = get_circle(r)
print(length, square)

from math import pi
def get_circle(radius):
    length = 2 * pi * radius
    area = pi * radius ** 2
    return length, area
r = float(input())
length, square = get_circle(r)
print(length, square)

# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
# a, b, c – коэффициенты квадратного уравнения a(x**2)+bx+c=0 и возвращает его корни в порядке возрастания.
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    x = -(b / (2 * a))
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    if d > 0:
        return (min(x1, x2), max(x1, x2))
    elif d == 0:
        return x1, x2
# считываем данные
a, b, c = int(input()), int(input()), int(input())
# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    x = -(b / (2 * a))
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    if d > 0:
        return (min(x1, x2), max(x1, x2))
    elif d == 0:
        return x1, x2
# считываем данные
a, b, c = int(input()), int(input()), int(input())
# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)


def draw_box():
    for _ in range(5):
        print('*' * 7)
draw_box()
print()
draw_box()
print()
draw_box()

# объявление функции
def print_message():
    print('Я - Артур,')
    print('король британцев. ')
# вызов функции
print_message()

def welcome():
    print('Добро пожаловать!')
print('Начинаем изучать функции')
welcome()

# Напишите функцию draw_box(), которая выводит звёздный прямоугольник с размерами 14×10
def draw_box():
    for i in range(1, 15):
        if i == 1 or i == 14:
            print('*' * 10)
        else:
            print('*' + ' ' * 8 + '*')
draw_box()

def draw_box():
    print("*" * 10)
    for i in range(12):
        print("*", "*", sep=" " * 8)
    print("*" * 10)
draw_box()

def draw_box():
    print('*'*10 + '\n' + ('*' + ' '*8 + '*\n')*12 + '*'*10)
draw_box()

# Напишите функцию draw_triangle(), которая выводит звёздный прямоугольный треугольник с катетами, равными 10
def draw_triangle():
    for i in range(10):
        print((1 + i) * '*')
draw_triangle()

def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')
draw_triangle()

def draw_triangle():
    for i in range(1, 11):
        print('*' * i)
draw_triangle()

def print_number(a, b, c):
    d = (a + c) // b
    print(d)
print_number(2, 3, 11)

def print_text(text, num):
    while num > 0:
        print(text, end='')
        num -= 1
print_text('Python', 4)

def print_double(num):
    num *= 2
    print(num)
num = 10
print_double(num)
print(num)

def triple(num):
    num *= 3
num = 10
triple(num)
print(num)

# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека; surname – фамилия человека; patronymic – отчество человека;
# а затем выводит на печать ФИО человека. ФИО должны иметь верхний регистр.
# Объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep='')
# считываем данные
name, surname, patronymic = input().upper(), input().upper(), input().upper()
# вызываем функцию
print_fio(name, surname, patronymic)

def print_fio(name, surname, patronymic):
    full_name = (surname[0] + name[0] + patronymic[0]).upper()
    print(full_name)
name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)

def print_fio(name, surname, patronymic):
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())
name, surname, patronymic = input(), input(), input(),
print_fio(name, surname, patronymic)

def print_fio(name, surname, patronymic):
    [print(m[0].upper(),end='') for m in [surname,name,patronymic]]
name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)

# Напишите функцию print_case_counts(s), которая принимает на вход строку s и выводит для неё текст в
# следующем формате: Букв в верхнем регистре: <U>; Букв в нижнем регистре: <L>,
# где <U>, <L> – количество букв в верхнем и нижнем регистрах соответственно.
# Функция должна игнорировать любые небуквенные символы, так как они не имеют регистра.
# объявление функции
def print_case_counts(s):
    digit_upper = sum([1 for digit in s if digit.isupper()])  # вводим переменную digit_upper для букв
    # верхнего регистра, затем используем встроенную функцию sum для вычисления суммы элементов,
    # затем создаем список, в котором пишем: всякий раз добавлять 1, перебирая элементы строки,
    # если элемент будет в верхнем регистре.
    digit_lower = sum([1 for digit in s if digit.islower()])  # аналогично как с верхним регистром
    print('Букв в верхнем регистре:', digit_upper)
    print('Букв в нижнем регистре:', digit_lower)
# считываем данные
s = input()
# вызываем функцию
print_case_counts(s)


def print_case_counts(s):
    uppers = lowers = 0
    for c in s:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
    print(f'Букв в верхнем регистре: {uppers}')
    print(f'Букв в нижнем регистре: {lowers}')
s = input()
print_case_counts(s)

def print_case_counts(s):
    print(f"Букв в верхнем регистре: {len([c for c in s if c.isupper()])}")
    print(f"Букв в нижнем регистре: {len([c for c in s if c.islower()])}")
s = input()
print_case_counts(s)

# Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать
# сумму его цифр.
def print_digit_sum(num):
    s = 0
    while num != 0:
        last_digit = num % 10
        s += last_digit
        num = num // 10
    print(s)
n = int(input())
print_digit_sum(n)

def print_digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    print(digit_sum)
n = int(input())
print_digit_sum(n)

def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))
n = int(input())
print_digit_sum(n)

# Напишите функцию print_sorted_hyphen(s), которая принимает строку s, состоящую из слов,
# разделённых дефисами, и выводит эти слова на одной строке в лексикографическом порядке,
# разделённые дефисами.
def print_sorted_hyphen(s):
    words = s.split('-')
    words.sort()
    print(*words, sep='-')
s = input()
print_sorted_hyphen(s)

def print_sorted_hyphen(s):
    seq = s.split('-')
    seq.sort()
    new_s = '-'.join(seq)
    print(new_s)
s = input()
print_sorted_hyphen(s)

def print_sorted_hyphen(s):
    words = s.split()
    words.sort()
    print(*words, sep = '-')
s = input().replace('-', ' ')
print_sorted_hyphen(s)

# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника; а затем выводит его.
def draw_triangle(fill, base):
    for i in range(1, n + 2):  # если основание нечетное, начинаем с ширины 1, если четное - 2.
        print('*' * i)
    for i in range(n, 0, -1):
        print('*' * i)
fill = input()  # символ-заполнитель
base = int(input()) // 2  # ширина основания равнобедренного треугольника
draw_triangle(fill, base)  # вызываем функцию

def draw_triangle(fill, base):  # объявляем функцию
    for i in range(1, base // 2 + 2):  # base - это целая часть от деления нечетного числа на 2,
        # плюс прибавляем 2, так как верхняя граница не входит, включительно до середины равнобедренного
        # треугольника
        print(fill * i)  #
    for i in range(base // 2, 0, -1):  # начинается со следующего числа после вершины,
        # 0 не входит в последовательность, и отрицательный шаг
        print(fill * i)
fill = input()  # символ-заполнитель
base = int(input())
draw_triangle(fill, base)  # вызываем функцию

def draw_triangle(fill, base):
    for i in range(base // 2):
        print(fill * (i + 1))
    for i in range(base // 2, -1, -1):
        print(fill * (i + 1))
fill = input()  # символ-заполнитель
base = int(input())
draw_triangle(fill, base)  # вызываем функцию

def draw_triangle(fill, base):
    print(*[fill * (min(i, base + 1 - i)) for i in range(1, base + 1)], sep="\n")
fill = input()  # символ-заполнитель
base = int(input())
draw_triangle(fill, base)  # вызываем функцию

# Тимур живёт в Москве, а Антон – в Перми. Каждый раз, когда они договариваются о времени созвона,
# Тимур говорит московское время, а Антону в уме приходится переводить его на пермское. Но иногда Антон
# переводит время неправильно и опаздывает на созвон, из-за чего Тимур сильно злится. Разница по времени
# между Москвой и Пермью составляет 2 часа (в Перми на 2 часа больше). Напишите функцию
# print_perm_time_call(msc_time), которая принимает на вход строку – время созвона по московскому времени –
# в формате hh:mm и выводит время созвона по пермскому времени в следующем формате: Созвон будет в HH:MM.
# Где HH:MM – время созвона по пермскому времени. Гарантируется, что время созвона по московскому
# времени будет не позднее 21:59.
def print_perm_time_call(msc_time):
    hourses = int(msc_time[:2])
    minutes = msc_time[2:]
    perm_time = hourses + 2
    perm_time_str = f'{perm_time:02}'  # это способ записать число с ведущим нулем, если оно меньше 10:
    # perm_time это число, которое мы форматируем, : это начало указания формата,
    # 0 - мы заполняем пустое место нулями, 2 - общая длина строки должна быть 2 символа.
    print(f'Созвон будет в {perm_time:02}{minutes}.')
msc_time = input()
print_perm_time_call(msc_time)

def print_perm_time_call(msc_time):
    msc_time = msc_time.split(':')  # разбиваем строку ввода на слова с разделителем ":"
    h = msc_time[0]  # часы по московскому времени - индекс первого слова из списка msc_time
    m = msc_time[1]  # минуты - индекс второго слова из списка msc_time
    new_h = int(h) + 2  # часы по пермскому времени, московское время, переведенное в числовой регистр + 2
    if new_h < 10:  # если пермское время меньше 10
        new_h = '0' + str(new_h)  # преобразуем его в строку и добавляем впереди 0
    print(f'Созвон будет в {new_h}:{m}.')
msc_time = input()
print_perm_time_call(msc_time)

# Напишите функцию print_symbol_counts(s), которая принимает на вход слово s и выводит для каждой
# буквы этого слова в лексикографическом порядке в нижнем регистре на отдельной строке количество её
# вхождений в это слово в следующем формате:<L>: <N>, где <L> – некоторая буква слова s, <N> – количество
# вхождений этой буквы в слово s. Если в слове встречается одна и та же буква в разных регистрах,
# то мы считаем это одной и той же буквой.
# объявление функции
def print_symbol_counts(s):
    s = s.lower()  # переводим в нижний регистр
    unique_letters = []  # сюда будем добавлять буквы, которых еще не было
    for ch in s:  # собираем список уникальных букв
        if ch not in unique_letters:
            unique_letters.append(ch)
    for i in range(len(unique_letters)):  # сортировка пузырьком
        for j in range(len(unique_letters) - i - 1):
            if unique_letters[j] > unique_letters[j + 1]:
                unique_letters[j], unique_letters[j + 1] = unique_letters[j + 1], unique_letters[j]
    for ch in unique_letters:  # выводим количество каждой буквы
        count = 0
        for c in s:
            if c == ch:
                count += 1
        print(f'{ch}: {count}')
# считываем данные
s = input()
# вызываем функцию
print_symbol_counts(s)


def print_symbol_counts(s):
    s = s.lower()  # меняем регистр на нижний
    unique_letters = []  #с оздаем пустой список
    for c in s:  # идем циклом по строке
        if c not in unique_letters:  # если в списке нет буквы
            unique_letters.append(c)  # добаляем буквы в новый список
    unique_letters.sort()  # сортируем элементы нового списка по возрастанию
    for c in unique_letters:  # проходим циклом по новому списку
        counts = s.count(c)  # подсчитываем количество элементов
        print(f'{c}: {counts}')
s = input()
print_symbol_counts(s)

from collections import Counter
def print_symbol_counts(s: str) -> None:
    cnt = sorted(Counter(s.lower()).items())
    print('\n'.join(f'{c}: {n}' for c, n in cnt))
print_symbol_counts(input())


# объявление функции
def print_symbol_counts(s):
    # приводим строку к нижнему регистру
    s = s.lower()
    # получаем уникальные буквы и сортируем их
    res = sorted(set(s))
    # подсчитываем количество вхождений каждой буквы
    for char in res:
        count = s.count(char)
        print(f'{char}: {count}')
# считываем данные
s = input()
# вызываем функцию
print_symbol_counts(s)

def print_symbol_counts(s):
    lst = [0] * 31
    base = ord('a') if ord(s[0]) < 1000 else ord('а')
    for c in s.lower():
        lst[ord(c) - base] += 1
    for i in range(31):
        if lst[i]:
            print(f"{chr(i + base)}: {lst[i]}")
s = input()
print_symbol_counts(s)

# Пример функции на основе загадки про слона и холодильник.
def put_in_fridge(animal):  # animal - параметр
    cnt = 1
    print(cnt, '. Открыть холодильник.', sep='')
    cnt += 1
    if animal != 'жираф':
        print(cnt, '. Достать оттуда жирафа.', sep='')
        cnt += 1
    print(cnt, '. Засунуть в холодильник ', animal, 'а.', sep='')
    cnt += 1
    print(cnt, '. Закрыть холодильник.', sep='')
print('Что нужно сделать, чтобы засунуть в холодильник жирафа?')
subject = 'жираф'
put_in_fridge(subject)      # subject - аргумент
print()
print('Что нужно сделать, чтобы засунуть в холодильник слона?')
subject = 'слон'
put_in_fridge(subject)


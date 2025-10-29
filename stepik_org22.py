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


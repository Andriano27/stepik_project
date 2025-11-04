# https://stepik.org/course/68343/syllabus
x = 5
def add():
    x = 3
    x = x + 5
    print(x)
add()
print(x)

x = 5
def add():
    global x
    x = 3
    x = x + 5
    print(x)
add()
print(x)

def double(num):
    return num * 2
print(double(10))

def triple(num):
    num = num * 3
print(triple(4))

def double(num):
    print(num * 2)  # внутренняя функция вернула удвоенное значение
print(double(7))  # внешняя функция, за неимением явного 'return' вернула None

def triple(num):
    print(num * 3)
    return num * 3
print(triple(4))

def do_something(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result
print(do_something([2, 2, 2, 2]))

# происходит вызов функции get_highest, в теле которой вычисляется индекс максимального элемента
# списка heights и возврат элемента списка names , индекс которого получен в предыдущем шаге.
# Возвращённое значение функции get_highest выводится на экран с помощью функции print .
# Если совсем по-простому, то в данном случае выводится имя самого высокого человека.
def get_highest(names, heights):
    max_height = max(heights)
    index_max_height = heights.index(max_height)
    return names[index_max_height]
print(
    get_highest(
        ['Андрей', 'Валерия', 'Елена', 'Николай', 'Жанна'],
        [1.75, 1.61, 1.65, 1.83, 1.64],
    )
)

def is_promocode_applicable(order_total, orders_number):
    if order_total > 1000 and orders_number == 0:
        return 'YES'
    else:
        return 'NO'
print(is_promocode_applicable(2499, 1))

# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах
# и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.
def convert_to_miles(km):
    km = num * 0.6214
    return km
num = int(input())
print(convert_to_miles(num))

def convert_to_miles(km):
    ml = km * 0.6214  # km это параметрическая переменная (локальная) и в нее заводится значение
    # num когда мы вызываем функцию.
    return ml
num = int(input())
print(convert_to_miles(num))

# Напишите функцию code_format(text), которая принимает строку текста text, оборачивает её в теги
# <code></code> и возвращает результат.
def code_format(text):
    string = '<code>{}</code>'.format(text)
    return string
text = input()
print(code_format(text))

def code_format(text):
    return f'<code>{text}</code>'
text = input()
print(code_format(text))

# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает
# количество дней в данном месяце.
def get_days(month):
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    else:
        return 30
num = int(input())
print(get_days(num))

def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1]
num = int(input())
print(get_days(num))

def get_days(month):
    return (28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31)
num = int(input()) # считываем данные
print(get_days(num))  # вызываем функцию

def get_days(month):
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
num = int(input())
print(get_days(num))

# Напишите функцию math_round_to_int(num), которая принимает положительное число с плавающей точкой num,
# округляет его до целого по математическим правилам, и возвращает результат.
# Математические правила округления: если дробная часть числа меньше 0.5, то округляем его в
# меньшую сторону. В противном случае округляем число в большую сторону.
def math_round_to_int(num):
    digit = int(num + 0.5)
    return digit
num = float(input())
print(math_round_to_int(num))

from math import ceil, floor
def math_round_to_int(num):
    if int(num * 10) % 10 >= 5:
        return ceil(num)
    else:
        return floor(num)
num = float(input())
print(math_round_to_int(num))

def math_round_to_int(num):
    return int(num+0.5)
num = float(input())
print(math_round_to_int(num))

# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и
# возвращающую список всех делителей данного числа.
def get_factors(num):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l
n = int(input())
print(get_factors(n))

def get_factors(num):
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)

    divisors.append(num)
    return divisors
n = int(input())
print(get_factors(n))

def get_factors(num):
    return [i for i in range(1, num // 2 + 1) if num % i == 0] + [num]
n = int(input())
print(get_factors(n))

def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]
n = int(input())
print(get_factors(n))

# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую
# количество делителей данного числа.
def number_of_factors(num):
    l = []
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
            cnt = len(l)
    return cnt
n = int(input())
print(number_of_factors(n))

def get_factors(num):
    dividers = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            dividers.append(i)
    dividers.append(num)
    return dividers
def number_of_factors(num):
    return len(get_factors(num))
n = int(input())
print(number_of_factors(n))

def number_of_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])
n = int(input())
print(number_of_factors(n))

def number_of_factors(num):
    return sum(1 for i in range(1, num + 1) if num % i == 0)
print(number_of_factors(int(input())))

# Напишите функцию get_unique(numbers), которая принимает список целых чисел numbers и возвращает
# новый список без повторяющихся значений, при этом сохраняя порядок появления чисел в исходном списке.
def get_unique(numbers):
    unique_digit = []
    for i in numbers:
        if i not in unique_digit:
            unique_digit.append(i)
    return unique_digit
numbers = eval(input())
print(get_unique(numbers))

def get_unique(numbers):
    return [numbers[i] for i in range(len(numbers)) if numbers[i] not in numbers[:i]]
print(get_unique(eval(input())))

# Напишите функцию get_last_index(data, value), которая принимает на вход список data и некоторое
# значение value и возвращает индекс последнего вхождения данного значения в список или текст «ERROR!»
# (без кавычек), если искомое значение отсутствует в списке.
# объявление функции
def get_last_index(data, value):
    try:
        # Поиск последнего вхождения значения с конца списка
        return len(data) - 1 - data[::-1].index(value)  # Вычисляет индекс последнего вхождения в исходном списке.
    except ValueError:
        # Возвращает "ERROR!", если значение не найдено
        return "ERROR!"
# считываем данные
data = eval(input())
value = eval(input())
# вызываем функцию
print(get_last_index(data, value))


def get_last_index(data, value):
    res = 'ERROR!'
    for i in range(len(data)):
        if data[i] == value:
            res = i
    return res
data = eval(input())
value = eval(input())
print(get_last_index(data, value))
# Находятся все вхождения, потому что циклом проходят по всему списку от начала до конца.
# Каждый раз, когда обнаруживается соответствие индекс перезаписывается в переменную res.
# Последнее найденное вхождение и будет последним индексом.

# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target
# и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
def find_all(target, symbol):
    all_index = []
    for i in range(len(target)):
        if target[i] == symbol:
            all_index.append(i)
    return all_index
s = input()
char = input()
print(find_all(s, char))

def find_all(target, symbol):
    return [x for x in range(len(target)) if target[x] == symbol]
s = input()
char = input()
print(find_all(s, char))

def find_all(target, symbol):     # объявление функции
    l = []                        # создали пустой список
    for i in range(len(target)):  # цикл на всю длину строки
        if target[i] == symbol:   # если индекс i из строки target является искомой буквой symbol:
            l.append(i)           # добавляем в список индекс
    return l                      # возвращаем список
s = input()                       # считываем строку s / target
char = input()                    # считываем искомый символ char / symbol
print(find_all(s, char))          # вызываем функцию

# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных
# по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
def merge(list1, list2):
    numbers1.extend(numbers2)
    numbers1.sort()
    return numbers1
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))


def merge(list1, list2):
    res_list = list1 + list2
    res_list.sort()
    return res_list
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))


def merge(list1, list2):
    first, second = list1[:], list2[:]
    result = []
    while first and second:
        if first[0] <= second[0]:
            item = first.pop(0)
        else:
            item = second.pop(0)
        result.append(item)
    result.extend(first if first else second)
    return result
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))

def merge(list1, list2):
    numbers = numbers1 + numbers2
    for i in range(len(numbers)):
        for j in range(i ,len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))


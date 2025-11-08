def is_sorted(names):
    new_names = names.copy()
    new_names.sort()
    if names == new_names:
        return True
    else:
        return False
print(is_sorted(['Александра', 'Владимир', 'Борис', 'Илья', 'Мария']))

def is_educational_domain(url):
    return url.endswith('.edu')
urls = [
    'https://www.coursera.org',
    'https://mipt.ru',
    'https://www.edu.ru',
    'https://stepik.org',
    'https://openedu.ru',
    'https://www.mit.edu',
    'https://www.ecu.edu',
    'https://pygen.ru'
]
cnt = 0
for url in urls:
    if is_educational_domain(url):
        cnt += 1
print(cnt)


import timeit
import random
# merge sort using default library
def merge(list1, list2):
    return sorted(list1 + list2)
# from stepic
def quick_merge(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    return result
numbers1 = sorted([random.randint(1, 2000000) for _ in range(1000000)])
numbers2 = sorted([random.randint(1, 2000000) for _ in range(2000000)])
start = timeit.default_timer()
merge(numbers1, numbers2)
print("Processing time merge: %s" % (timeit.default_timer() - start))
start = timeit.default_timer()
quick_merge(numbers1, numbers2)
print("Processing time quick_merge: %s" % (timeit.default_timer() - start))

# На вход программе подаются число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один
# отсортированный список с помощью функции quick_merge(), а затем выводит его. На вход программе подаются
# натуральное число n, а затем n строк, содержащих целые числа в порядке возрастания, разделённые символом
# пробела. Программа должна вывести элементы окончательного отсортированного списка каждое через пробел.
def quick_merge(n):  # объявляем функцию quick_merge, которая принимает один аргумент - n - количество
    # строк(списков), которые нужно прочитать и объединить
    total_list = []  # общий список для всех чисел, в него будем добавлять числа из каждой прочитанной строки
    for _ in range(n):  # цикл повторяется n - раз, по числу строк
        num = [int(c) for c in input().split()]  # читаем строку и превращаем в список целых чисел:
        # input().split() - читает одну строку и разбивает по пробелам в список строк,
        # int(c) for c in - каждую строку с превращаем в целое int(c) и получаем список целых.
        total_list += num  # добавляем прочитанные числа к общему списку
    total_list.sort()  # сортируем все вместе
    return total_list
n = int(input())
print(*quick_merge(n))


# берём из теории уже реализованную функцию быстрой сортировки
def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    while p1 < len(list1) and p2 < len(list2):  # пока ни один из списков не закончился
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    else:  # иначе прицепляем остаток другого списка
        result += list2[p2:]
    return result
# принимаем кол-во строк
n = int(input())
# формируем из первой строки список чисел и возьмём
# этот первый список за основу для результирующего списка
res = [int(num) for num in input().split()]
# принимаем n - 1 строк (потому что первую строку мы уже приняли)
for _ in range(n - 1):
    # принимаем текущую строку и формируем из неё список чисел
    cur_list = [int(num) for num in input().split()]
    # объединяем результирующий список и текущий список
    # и записываем этот новый отсортированный список в качестве
    # результирующего списка
    res = quick_merge(res, cur_list)
# выводим результирующий список
print(*res)


def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    return result
n = int(input())
list2 = []
for i in range(n):
    list2 += list(map(int, input().split()))
list2.sort()
print(*list2)

# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов
# три натуральных числа, и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
# объявление функции
def is_valid_triangle(side1, side2, side3):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
# считываем данные
a, b, c = int(input()), int(input()), int(input())
# вызываем функцию
print(is_valid_triangle(a, b, c))

# объявление функции
def is_valid_triangle(side1, side2, side3):
    sides = [side1, side2, side3]  # создаем список из сторон
    sides.sort()  # сортируем стороны по возрастанию
    return (
        sides[0] + sides[1] > sides[2]
    )  # проверяем, минимальная и средняя стороны больше максимальной
# считываем данные
a, b, c = int(input()), int(input()), int(input())
# вызываем функцию
print(is_valid_triangle(a, b, c))

def is_valid_triangle(side1, side2, side3):
    return (side1 < side2 + side3) and (side2 < side3 + side1) and (side3 < side1 + side2)
print(is_valid_triangle(int(input()), int(input()), int(input())))

# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text
# и возвращает значение True, если указанный текст является палиндромом, или False в противном случае.
def is_palindrome(text):
    s = ''
    for c in text:
        if c.isalpha():  # берем только буквы
            s += c.lower()  # добавляем только буквы в нижнем регистре
    return s == s[::-1]  # сравниваем строку с её обратной версией, одинаково ли читается справа налево
    # и наоборот
# считываем данные
txt = input()
# вызываем функцию
print(is_palindrome(txt))


def is_palindrome(text):
    s = ''.join(c.lower() for c in text if c.isalpha())  # c.lower() for c in text if c.isalpha() - это
    # 'генератор': он берет по одной букве из text, оставляя только буквы isalpha() и делает их маленькими
    # lower(). ''.join собирает буквы в одну строку без пробелов.
    return s == s[::-1]  # сравниваем строку с её обратной версией, одинаково ли читается справа налево и наоборот
txt = input()
print(is_palindrome(txt))

def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]
txt = input()
print(is_palindrome(txt))

def is_palindrome(text):
    text = [i.lower() for i in text if i not in (',.!?- ')]
    return text == text[::-1]
txt = input()
print(is_palindrome(txt))

# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова
# word1 и word2. Функция должна возвращать значение True, если слова имеют одинаковую длину
# и отличаются одним символом на одной и той же позиции, или False в противном случае.
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        s = 0
        for c in range(0, len(word1)):
            if word1[c] != word2[c]:
                s += 1
        if s == 0 or s >= 2:
            return False
        return True
    else:
        return False
txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))

def is_one_away(word1, word2):
    return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)
txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))

def is_one_away(word1, word2):
    a = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            a += 1
    return len(word1) == len(word2) and a == 1
txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))




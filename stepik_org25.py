# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку
# в «верблюжьем регистре» и преобразует его в «змеиный регистр».
def convert_to_python_case(text):
    res = ''
    for i in range(len(text)):
        if i != 0 and text[i] == text[i].upper() and text[i].isdigit() == False:
            res += '_'
        res += text[i].lower()
    return res
txt = input()
print(convert_to_python_case(txt))

def convert_to_python_case(text):
    new_text = ""
    for el in text:
        if not el == el.lower():  # проверяем, что элемент в верхнем регистре (пропускаем цифры)
            new_text += "_" + el.lower()
        else:
            new_text += el
    return new_text[1:]
txt = input()
print(convert_to_python_case(txt))

def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]
print(convert_to_python_case(input()))

def convert_to_python_case(text):
    return ''.join(['_' + i if i.isupper() else i for i in text]).lstrip('_').lower()
txt = input()
print(convert_to_python_case(txt))

def convert_to_python_case(text):
    for i in text:
        if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            text = text.replace(i, '_' + i.lower())
    return text[1:]
txt = input()
print(convert_to_python_case(txt))

def convert_to_python_case(text):  # Функция
    array = []  # Пустой список
    for i in text:  # Цикл
        if i.isupper():  # Условие для вставки нижнего пробела
            array.append('_')  # Нижний пробел
            array.append(i.lower())  # Букву в нижнем регистре с добавлением нижнего пробела
        else:
            array.append(i.lower())  # Добавляем остальное
    return ''.join(array[1:])    # Возврат из списка в строку и убираем первый пробел 1:
txt = input()
print(convert_to_python_case(txt))

# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и
# возвращает значение True, если число является простым, или False в противном случае.
# Простое число – это натуральное число, единственными делителями которого являются только оно само и 1
# Число 1 простым не является
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):  # так как 1 не входит в условие, цикл мы начинаем с 2
        if num % i == 0 or n == 1:  # если исходное число делится на какое-либо отличное от 1 и самого себя
            return False
    return True
n = int(input())
print(is_prime(n))

def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2
n = int(input())
print(is_prime(n))

def is_prime(num):
    counter = 0
    for i in range(num):
        if num % (i + 1) == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False
n = int(input())
print(is_prime(n))

def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False
n = int(input())
print(is_prime(n))

# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное
# число num и возвращает первое простое число, большее числа num.
def get_next_prime(num):
    num += 1  # начинаем проверку со следующего числа, так как ищем первое простое после заданного
    while True:  # бесконечный цикл, пока не найдем простое число
        is_prime = True  # предполагаем, что число простое, пока не найдем делитель
        for i in range(2, num):  # проверяем делители от 2 до num
            if num % i == 0:  # нашли делитель, отличный от num и 1 - значит, число не простое
                is_prime = False  # устанавливаем флаг False для непростого числа
                break  # прерываем цикл по делителям
        if is_prime:  # если делителей не нашли - значит число простое
            return num  # возвращаем его
        num += 1  # иначе увеличиваем на 1 и пробуем следующее число
# считываем данные
n = int(input())
# вызываем функцию
print(get_next_prime(n))

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):  # так как 1 не входит в условие, цикл мы начинаем с 2
        if num % i == 0 or n == 1:  # если исходное число делится на какое-либо отличное от 1 и самого себя
            return False
    return True
def get_next_prime(num):
    num += 1  # начинаем со следующего числа
    while not is_prime(num):  # пока число не простое - проверяем дальше
        num += 1
    return num  # нашли простое число - возвращаем
n = int(input())
print(get_next_prime(n))

# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение
# пароля password и возвращает значение True, если пароль является надёжным, или False в противном случае.
# Пароль является надёжным, если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
def is_password_good(password):  # функция принимает один аргумент - строку password
    if len(password) < 8:  # Проверяем длину
        return False
    has_upper = False  # проверяем наличие заглавных букв
    has_lower = False  # проверяем наличие строчных букв
    has_digit = False  # проверяем наличие цифр
    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit  # если все три условия True, то ответ будет True,
    # если хотя бы одно False, то ответ будет False
# считываем данные
txt = input()
# вызываем функцию
print(is_password_good(txt))

def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])
txt = input()
print(is_password_good(txt))

def is_password_good(password):
    result = True
    if len(password) < 8:
        result = False
    if password.lower() == password:
        result = False
    if password.upper() == password:
        result = False
    if password.isalpha():
        result = False
    return result
# считываем данные
txt = input()
# вызываем функцию
print(is_password_good(txt))

def is_password_good(password):
    countup = 0
    countlower = 0
    countdig = 0
    if len(password) >= 8:
        for i in password:
            if i.isupper():
                countup += 1
            if i.islower():
                countlower += 1
            if i.isdigit():
                countdig += 1
        if countup > 0 and countlower > 0 and countdig > 0:
            return True
        else:
            return False
    else:
        return False
# считываем данные
txt = input()
# вызываем функцию
print(is_password_good(txt))

# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и ) и возвращает значение True, если поступившая на вход строка является
# правильной скобочной последовательностью, или False в противном случае.
# Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ),
# где каждой открывающей скобке найдётся парная закрывающая скобка (при этом каждая открывающая скобка
# должна быть левее соответствующей ей закрывающей скобки).
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text
txt = input()
print(is_correct_bracket(txt))

def is_correct_bracket(text):
    cnt = 0
    for el in text:
        if el == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            break
    return cnt == 0
txt = input()
print(is_correct_bracket(txt))

def is_correct_bracket(text):
    i = 0
    for c in text:
        if (i < 0):
            return False
        if (c == '('):
            i += 1
        elif (c == ')'):
            i -= 1
    return (i == 0)
txt = input()
print(is_correct_bracket(txt))

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть чётным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое
# значение пароля password и возвращает значение True, если пароль является действительным паролем
# BEEGEEK банка, или False в противном случае.
def is_valid_password(password):
    parts = password.split(':')  # разбиваем строку и проверяем, что ровно три части
    if len(parts) != 3:  # если длина списка не равна 3 - значит формат неправильный
        return False
    a = parts[0]  # переменная для палиндрома
    b = parts[1]  # переменная для простого числа
    c = parts[2]  # переменная для четного числа
    if a != a[::-1]:  # проверка на палиндром
        return False  # значит а не палиндром
    if not b.isdigit():  # убеждаемся, что b состоит целиком из чисел
        return False  # значит b не простое число
    b = int(b)  # делаем из строки число
    if b < 2:  # убеждаемся, что b не 0 и не 1
        return False  # значит b не простое число
    for i in range(2, b):  # проходим циклом по b
        if b % i == 0:  # если у b есть делитель, отличный от него и от 1
            return False  # значит b не простое число
    if not c.isdigit():  # убеждаемся, что c состоит целиком из чисел
        return False  # значит с нечетное число
    c = int(c)  # делаем из строки число
    if c % 2 != 0:  # если число не делится на 2 без остатка
        return False  # значит с нечетное число
    return True
psw = input()
print(is_valid_password(psw))


def is_palindrome(num):
    return str(num) == str(num)[::-1]
def is_prim(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_even(num):
    return num % 2 == 0
# объявление функции
def is_valid_password(password):
    seq = password.split(":")
    if len(seq) == 3:
        seq = [int(el) for el in seq]
        a, b, c = seq[0], seq[1], seq[2]
        return is_palindrome(a) and is_prim(b) and is_even(c)
    return False
# считываем данные
psw = input()
# вызываем функцию
print(is_valid_password(psw))


def is_valid_password(password):
    p = password.split(':')
    a = p[0]  # число должно быть палиндром
    b = int(p[1])  # число должно быть простым
    c = int(p[2])  # число должно быть четным
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    if len(p) == 3:
        flag1 = True
    if a == a[::-1]:
        flag2 = True
    for i in range(2, b):
        if b % i == 0:
            break
        else:
            flag3 = True
    if c % 2 == 0:
        flag4 = True
    return flag1 and flag2 and flag3 and flag4
psw = input()
print(is_valid_password(psw))


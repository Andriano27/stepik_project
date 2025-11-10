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
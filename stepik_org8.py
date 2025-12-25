num = 813
while num > 0:
    last_digit = num % 10
    num //= 10
    print(last_digit, sep='=', end='')

num = 725
while num != 0:
    last_digit = num % 10
    num //= 10
    print(last_digit, sep='', end='$')

num = 586
while num > 0:
    last_digit = num % 10
    print(last_digit, sep='*', end='#')
    num //= 10
    print()

# 7 - ка считывается, поскольку условие if i > 6: break находится после  print(i, end='*').
# Т.е., сначала считывается семерка, а потом уже сравнивается с 6 - кой и
# после этого прерывается выполнение условия
for i in range(10):
    print(i, end='*')
    if i > 6:
        break

# 6 - ка считывается и *, а после цикл прерывается
for i in range(10):
    if i > 6:
        break
    print(i, end='*')

i = 100
while i > 0:
    if i == 40:
        break
    print(i, end='*')
    i -= 20

n = 10
while n > 0:
    n -= 1  # при каждой итерации вычитаем из n единицу
    if n == 2:
        continue  # когда цикл дойдет до 2, он пропустит ее не печатая, сразу вернется к условию
    print(n, end='*')

result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i  # при каждой итерации суммируем число с номером нечетной итерации

print(result)

mult = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i % 9 == 0:
        break
    mult *= i  # при каждой итерации умножаем число на номер следующей нечетной итерации

print(mult)

# На вход программе подаётся число n(n>1). Напишите программу, которая выводит его наименьший отличный
# от 1 делитель.
n = int(input())
for i in range(2, n + 1):  # на 0 делить нельзя, а 1 делитель не может равняться, потому начинаем с 2
    if n % i == 0:         # n + 1 так как иначе цикл будет на одно число меньше
        break
print(i)

n, i = int(input()), 2
while True:
    if n % i == 0:
        print(i)
        break
    i += 1

n, a = int(input()), 2
while n % a != 0:
    a += 1
print(a)

n = int(input())
d = 1
while d <= n:
    d += 1
    if n % d == 0:
        break
print(d)

num = int(input())
for i in range(2, num+1):
    if num % i == 0:        # если исходное число делится на какое-либо отличное от 1 и самого себя
        break               # останавливаем цикл если встретили делитель числа
print(i)

# На вход программе подаётся натуральное число n. Напишите программу, которая выводит числа
# от 1 до n включительно за исключением: от 5 до 9 включительно, от 17 до 37 включительно,
# от 78 до 87 включительно
n = int(input())
for i in range(1, n + 1):
    if 4 < i < 10 or 16 < i < 38 or 77 < i < 88:
        continue
    print(i)

n = int(input())
i = 0
while i < n:
    if i == 4:
        i = 9
        continue
    elif i == 16:
        i = 37
        continue
    elif i == 77:
        i = 87
        continue
    i += 1
    print(i)

# На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности
# и их произведение.
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')


# На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Известно, что вводимые числа по абсолютной величине не превышают 10 ** 6. Нужно написать программу,
# которая выводит на экран сумму всех отрицательных чисел последовательности
# и максимальное отрицательное число в последовательности.
# Если отрицательных чисел нет, требуется вывести на экран «NO» (без кавычек).
largest = None   # пока нет отрицательных чисел
digit_sum = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        digit_sum += x
        if largest is None or x > largest:  # ищем максимум среди отрицательных
            largest = x                     # смещен блок кода, чтобы условие работало только для x < 0
if largest is None:
    print("NO")
else:
    print(digit_sum)
    print(largest)

nums = [int(input()) for _ in range(10)]  # собираем все числа в список nums
negatives = [x for x in nums if x < 0]  # отфильтровываем отрицательные в negatives
if negatives:
    print(sum(negatives))
    print(max(negatives))
else:
    print("NO")  # если список пуст → выводим "NO"

#  На обработку поступает последовательность из 7 целых чисел (каждое на отдельной строке).
#  Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности.
#  Если таких чисел нет, программа должна вывести 0.
digit_summa = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        digit_summa += n
if digit_summa == 0:
    print(0)
else:
    print(digit_summa)

sm = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 0:
        sm += n
print(sm)

# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран
# максимальную цифру числа, кратную 3. Если в числе нет цифр, кратных 3, требуется на экран вывести «NO».
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)

n = int(input())
max_digit = -1  # берем максимальное число '-1', чтоб пройти проверку если среди вводимых цифр будет '0'
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:  # проверка или цифра числа максимальная
            max_digit = digit
    n = n // 10  # уменьшаем число на один знак
if max_digit < 0:  # если условие не истина, значит чисел кратных "3" не было
    print('NO')
else:
    print(max_digit)

n = int(input())
max_digit = -1
count = False
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        count = True
        if max_digit < digit:
            max_digit = digit
    n = n // 10
if count:
    print(max_digit)
else:
    print('NO')

n = int(input())
max_digit = -1  # Максимальную цифру числа приравниваем к -1, т. к. к 0 мы не можем потому что 0
# является кратным числу 3
while n > 0:
    digit = n % 10  # находим последнюю цифру в числе
    if digit % 3 == 0:  # проверяем делится ли число на 3
        if digit > max_digit:  # если число делится, и получившееся число больше переменной
            max_digit = digit  # присваиваем нашей переменной эту цифру
    n = n // 10  # отбрасываем последнюю цифру
if max_digit < 0:  # если так и не нашли числа кратного 3 печатаем нет
    print('NO')
else:
    print(max_digit)

# На обработку поступает натуральное число. Нужно написать программу,
# которая выводит на экран его первую (старшую) цифру.
n = int(input())
g = None
while n > 0:
    g = n % 10
    n = n // 10
print(g)

n = int(input())
while n > 9:
    n //= 10
print(n)

# На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран
# произведение цифр введённого числа.
n = int(input())
product = 1
while n != 0:  # необходимо перебрать все цифры числа
    digit = n % 10
    product = product * digit
    n //= 10
print(product)

for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')

# Во внешнем цикле итерации производятся с 99 до 101, переменной temp присвоен номер итерации.
# Пока переменная temp > 0, счетчик считает во вложенном цикле, затем убирается последняя цифра числа.
# Итерации во вложенном цикле продолжаются, пока в числе есть цифры больше 0.
# Затем переход к следующей итерации во внешнем цикле, с 99 к 100 и затем к 101.
counter = 0
for i in range(99, 102):
    temp = i            # сначала temp = 99, число > 0 (условие выполняется и счетчик counter = 1)
    while temp > 0:   # после удаления 1 разряда от числа 99, остается 9, которое также > 0 (counter = 2)
        counter += 1  # При удалении еще одного разряда число 0, условие не выполняется.
        temp //= 10  # Цикл while с числом 99
print(counter)  # Затем temp = 100. Далее снова работает цикл while и уже будет выполнено 3 условия
# (100>0, 10 >0, 1 >0). После работы цикла while с числом 100 счетчик counter = 5
# Дальше temp = 101. Все происходит точно как, как с предыдущим числом.
# Будет тоже выполнено 3 условия (101 >0, 10>0, 1>0)
# По итогу работы вложенного цикла while с числами 99, 100, 101 счетчик counter = 8 (2 + 3 + 3)

# У Тимура есть список никнеймов соцсети FriendsGram. Напишите программу, которая выводит первый никнейм,
# не содержащий символ нижнего подчёркивания _. Программа должна вывести первый никнейм,
# не содержащий символ нижнего подчёркивания _.
flag = False
while not flag:
    text = input()
    if '_' not in text:
        print(text)
        flag = True

name = input()
while '_' in name:
    name = input()
print(name)

print(next(name for name in iter(input, '') if '_' not in name))

while True:
    nickname = input()
    if "_" not in nickname:
        print(nickname)
        break

# Напишите программу, которая выводит, сколько людей стоят в очереди между Александрой и Левоном.
name_alex = 0
name_levon = 0
counter = 0
while True:
    name = input()
    counter += 1
    if name == "Александра":
        name_alex = counter
    if name == "Левон":
        name_levon = counter
        break
print(name_levon - name_alex - 1)

name = input()
while name != 'Александра':
    name = input()
name = input()
cnt = 0
while name != 'Левон':
    cnt += 1
    name = input()
print(cnt)

NAMES = []
while "Левон" not in NAMES:
    NAMES.append(input())
print(NAMES.index("Левон") - NAMES.index("Александра") - 1)

# На вход программе подаются четыре целых числа h1, h2, m1, m2, которые задают временной промежуток
# от h₁:m₁ до h₂:m₂. Напишите программу, которая выводит все моменты времени между этими промежутками
# (включая границы) в формате hh:mm с интервалом в 1 минуту, каждый на отдельной строке.
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
start = h1 * 60 + m1
end = h2 * 60 + m2
while start <= end:
    h = start // 60
    m = start % 60
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    print(h, m, sep=':')
    start += 1

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
start = h1 * 60 + m1
end = h2 * 60 + m2
while start <= end:
    h = start // 60
    m = start % 60
    print(f"{h:02d}:{m:02d}")  # d - число, 2 - минимум 2 символа, 0 - если не хватает, добавить 0 слева
    start += 1

h1, m1, h2, m2 = map(int, open(0))
for x in range(h1 * 60 + m1, h2 * 60 + m2 + 1):
    print(f'{x // 60:02}:{x % 60:02}')


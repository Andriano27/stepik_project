for i in range(5):
    print(str(i) * 2)
    if i >= 2:
        break

num = 7
while num < 12:
    num += 2
    if num == 11:
        break
    print(num)
else:
    print('Цикл завершен.')

num = 4
while num < 10:
    num += 2
    print(num)
else:
    print('Цикл завершен.')

num = 3
total = 0
for i in range(num):
    if i % 2 == i:
        total += 1
else:
    print(total)
print(total + 1)

num = 3
while num < 8:
    num += 1
else:
    print('Цикл завершен.')
print(num)

num = 3281
while num != 0:
    print(num % 10, end='')
    num //= 100
    if num != 0:
        continue

n = int(input())
s = 0
while n > 0:
    l = n % 10
    if l % 2 == 0:
        s = s + l
    n //= 10
print(s)

n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s = s + n % 10
    n //= 10
print(s)

n = 8
count = 0
maximum = -10 ** 12  # числа не превышают 10^12 степени
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

count = 0
maximum = -1
for i in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# На вход программе подаётся натуральное число n(3≤n≤19). Напишите программу, которая печатает
# звёздную рамку размерами n×19.
n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*' * 19)
    else:
        print('*' + ' ' * 17 + '*')

n = int(input())
for i in range(1, n + 1):
    if i == 1:  # по условию первый ряд весь заполнен звездочка
        print('*' * 19)
    elif i == n:  # по условию весь последний ряд заполнен звездочками
        print('*' * 19)
    else:  # середина имеет звездочку в начале и в конце, середина заполнена пробелами, 19 - 2 = 17 пробелов.
        print('*', ' ' * 17, '*', sep='')

n = int(input())
print("*"*19)
for i in range(n-2):
    print("*                 *")
print("*"*19)

# Дано натуральное число n(n>99). Напишите программу, которая определяет его третью (с начала) цифру.
three_digit = None
n = int(input())
while n > 99:
    three_digit = n % 10
    n = n // 10
print(three_digit)

n = int(input())
counter = 0
number = n
while n > 0:
    n //= 10
    counter += 1
print(((number // (10 ** (counter - 3))) % 10))

n = input()
print(n[2])

n = int(input()[::-1])  # Зеркалим число, чтобы сделать только три итерации
for _ in range(2):
    n //= 10
print(n % 10)

# Дано натуральное число. Напишите программу, которая вычисляет: количество цифр 3 в нём; сколько раз в нём
# встречается последняя цифра;количество чётных цифр;сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна,
# то вывести её);сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).
n = int(input())
count_more_five = 0
count_three = 0
count_last = n % 10
count_last_digit = 0
count_more_seven = 1
count_zero_and_five = 0
count_honest = 0
while n > 0:
    last_digit = n % 10
    if last_digit > 5:
        count_more_five = count_more_five + last_digit
    if last_digit == 3:
        count_three += 1
    if last_digit == count_last:
        count_last_digit += 1
    if last_digit % 2 == 0:
        count_honest += 1
    if last_digit > 7:
        count_more_seven *= last_digit
    if last_digit == 0 or last_digit == 5:
        count_zero_and_five += 1
    n = n // 10
print(count_three)
print(count_last_digit)
print(count_honest)
print(count_more_five)
print(count_more_seven)
print(count_zero_and_five)

# На вход программе подаётся натуральное число n. Напишите программу, которая выводит для каждой
# четной цифры данного числа текст в следующем формате: <i>-я четная цифра равна <digit>, где
# <i> – номер четной цифры (начиная с 1), <digit> – значение четной цифры. При этом если в числе нет
# четных цифр, необходимо вывести следующий текст: 'Четных цифр в числе нет'.
n = int(input())
count = 0
num = len(str(n))
for i in range(1, num + 1):
    digit = n // 10 ** (num - i) % 10
    if digit % 2 == 0:
        count += 1
        print(count, '-я ', 'четная цифра равна ', digit, sep='')
if count == 0:
    print('Четных цифр в числе нет')

n = int(input())
even = [digit for digit in str(n) if not int(digit) & 1]
if not even:
    print('Четных цифр в числе нет')
else:
    for i, digit in enumerate(even, start=1):
        print(f'{i}-я четная цифра равна {digit}')

num = [x for x in input() if not int(x)%2]
if not num:
    print('Четных цифр в числе нет')
else:
    for i, digit in enumerate(num, 1 ):
        print(f'{i}-я четная цифра равна {digit}')

#####
num = 952
while num > 0:
    print(num % 10, end='')
    if num % 10 == 5:
        break
    num //= 10
print()
print('Программа завершена.')

# В свободное от модерации курсов время Сэм пишет спам-ботов на заказ. Для каждого бота он формирует
# никнейм по простому (но странному) алгоритму. Сначала Сэм вводит стартовую строку – произвольное имя.
# Дальше, пока длина строки меньше 10 символов, он повторяет правило: если текущая длина строки кратна 4,
# прибавляет справа символ x, иначе, если текущая длина строки кратна 5, прибавляет справа символ y, в
# противном случае прибавляет слева символ z. В конце Сэм добавляет слева символ @ и завершает
# формирование никнейма.
s = input()
while len(s) < 10:
    if len(s) % 4 == 0:
        s = s + 'x'
    elif len(s) % 5 == 0:
        s = s + 'y'
    else:
        s = 'z' + s
s = '@' + s
print(s)

# Майк и Дастин обмениваются цифровыми сообщениями через приёмник. Каждое сообщение представляет собой
# целое число. Майк и Дастин договорились, что последнее сообщение будет оканчиваться на 11, после него
# переписка прекращается. Лукас перехватывает сообщения Майка и Дастина и хочет посчитать, у скольких из
# них длина более 7 символов. Для этого Лукас написал программу, однако допустил в ней несколько ошибок
# из-за того, что прогуливал уроки информатики в школе. Исправьте программу Лукаса так, чтобы она
# корректно находила количество сообщений длиной более 7 символов и выводила текст в следующем виде:
# n/m, где n – количество сообщений длиннее 7 символов, m – общее количество сообщений.
# Последнее сообщение также нужно учитывать при подсчёте сообщений длиной более 7 символов
# и общего количества сообщений.
cnt = 0
total = 0
while True:
    num = int(input())
    total += 1
    if len(str(num)) > 7:
        cnt += 1
    if num % 100 == 11:
        break
print(cnt, total, sep='/')

num = int(input())
cnt = 0
total = 1
while num % 100 != 11:
    if len(str(num)) > 7:
        cnt += 1
    total += 1
    num = int(input())
if len(str(num)) > 7:
    cnt += 1
print(cnt, '/', total, sep='')


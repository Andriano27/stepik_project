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


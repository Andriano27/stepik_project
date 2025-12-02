for i in range(10):
    print(i, '*', ' ', end='')
# Программа должна случайным образом генерировать два числа в диапазоне от 1 до 6 и показывать их.
import random
print('Бросаем кубики... ')
print('Значения граней:')
print(random.randint(1, 6))
print(random.randint(1, 6))

# Будем использовать цикл while, который имитирует один бросок кубиков и затем спрашивает пользователя,
# следует ли сделать еще один бросок. Цикл будет повторяться до тех пор, пока пользователь отвечает "да",
# набирая букву "д":
import random
again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# Мы можем сымитировать бросание монеты путем генерации случайного числа в диапазоне от 0 до 1.
# Для генерации целых чисел мы будем использовать функцию randint():
import random
for _ in range(10):
    num = random.randint(0, 1)
    if num == 0:
        print('Орел')
    else:
        print('Решка')

# /////
import random
count1 = 0
count2 = 0
for _ in range(10000000):
    num = random.randint(0, 1)
    if num == 0:
        # print('Орел')
        count1 += 1
    else:
        # print('Решка')
        count2 += 1
print(f'Орлов выпало: {count1}')
print(f'Решек выпало: {count2}')
print(count1 * 100 / (count2 + count1))

# Программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много,
# попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение
# 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить
# его и вывести сообщение 'Вы угадали, поздравляем!'. Составляющие проекта:
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл while;
# Бесконечный цикл;
# Операторы break, continue;
# Работа с модулем random для генерации случайных чисел.
from random import randint
print("Игра - 'Угадай-ка число!'")
name = input('Пожалуйста введите ваше имя: ')
num = randint(1, 100)
while True:
    user_num = int(input(f'{name} введите число от 1 до 100: '))
    if user_num > num:
        print('Слишком много, попробуйте еще раз')
    elif user_num < num:
        print('Слишком мало, попробуйте еще раз')
    else:
        print('Вы угадали, поздравляем!')
        break
# Чтобы гарантированно угадать задуманное число от 1 до 100 (включительно) потребуется не более 7 попыток.
# Положим left = 1 и right = 100. Называем число, равное middle = (left + right) // 2;
# Если число middle равно задуманному числу, то мы угадали!;
# Если число middle меньше задуманного числа, то положим left = middle + 1 и продолжим алгоритм;
# Если число middle больше задуманного числа, то положим right = middle - 1 и продолжим алгоритм.
import math
n = int(input())
print(math.ceil(math.log2(n)))

n = int(input())
counter = 0  # количество попыток
p = 1  # количество чисел, которые можно гарантированно покрыть за количество попыток
while p < n + 1:
    p *= 2
    counter += 1
print(counter)

n = int(input())
attempts = 0
while 2 ** attempts <= n:
    attempts += 1
print(attempts)


# Тимуру предоставляется возможность загадать число от 1 до n (включительно)
n = int(input())
# Пусть Тимур загадал число n, которое занимает максимальное количество попыток для отгадывания
wished_number = n
# Руслан начинает отгадывать от числа 1
start = 1
# Руслан заканчивает отгадывать числом n (включительно)
end = n
attempts = 0
while True:
    # Руслан называет число middle
    middle = (start + end) // 2
    # Руслан тратит одну попытку
    attempts += 1
    # если Тимур говорит, что загаданное число БОЛЬШЕ
    if wished_number > middle:
        start = middle + 1
    # если Тимур говорит, что загаданное число МЕНЬШЕ
    elif wished_number < middle:
        end = middle - 1
    # если Руслан отгадал число Тимура
    else:
        break
print(attempts)

n = int(input())
for i in range(n):
    if 2**i >= n:
        print(i)
        break


def ugad(n):
    total = 0
    while n // 2 > 0:
        n -= n // 2
        total += 1
    return total
n = int(input())
print(ugad(n))

left = 1
right = int(input())
count = 0
while right > left :
 middle = (right + left) // 2
 count += 1
 right = middle
print(count)


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



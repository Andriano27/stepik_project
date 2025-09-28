
t = list(range(4, 4))  # создаёт пустой список на основе пустой последовательности чисел
print(t)

# На вход программе подаётся одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].
n = int(input())
mylist = list(range(1, n + 1))
print(mylist)

# На вход программе подаётся натуральное число n. Напишите программу, которая выводит список,
# состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
n = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
print(list(s[:n]))  # печатаем строку от начала до указанного количества букв

n = int(input())
s = ""  # переменная s представляет пустую строку
for i in range(n):  # создаем цикл длинной n
    s += chr(ord("a") + i)  # перебираем цикл и добавляем в пустую строку i начиная от численного символа
    # Unicode, соответствующего строчной латинской букве 'a' до указанного количества символов,
    # преобразуем строку из чисел в буквенные символы
print(list(s))

n = int(input())
s = ''
for i in range(n):
    s += chr(97 + i)
print(list(s))

n = int(input())  # получаем целое число на входе
alphabet = list()  # создаем пустой список для символов алфавита

for i in range(n):  # индекс буквы в будущем списке от 0 до n
    alphabet += chr(97 + i)  # прибавляем к списку букву с соответствующим номером в таблице ASCII
print(alphabet)  # выводим получившийся список

# На вход программе подаётся число n(n≥1). Напишите программу, которая создаёт список из нечётных чисел
# от 1 до n (включительно) и выводит его.
n = int(input())
num = list(range(1, n + 1, 2))
print(num)

# Гвидо собрал чемодан в командировку, но совсем забыл, что у авиакомпании есть ограничение на вес багажа.
# Чемодан Гвидо превысил лимит в два раза, поэтому из него придётся выложить каждую вторую вещь.
# На вход программе подаётся строка из эмодзи-символов. Создайте список, содержащий все символы данной
# строки, не включая каждый второй, и выведите этот список.
s = input()
print(list(s[::2]))

print(list(input())[::2])

numbers = [2, 0, 2, 5]
letters = ['a', 'b']
print(len(numbers) + len(letters))

numbers = [2, 0, 2, 5]
print(5 in numbers)
print(20 not in numbers)

browsers = ['Firefox', 'Chrome', 'Safari', 'Yandex']
print(browsers[3] + ' + ' + browsers[1])

friends = ['Chandler', 'Ross', 'Phoebe', 'Rachel']
friends[4] = 'Emily'
print(friends)

browsers = ['Firefox', 'Chrome', 'Safari', 'Yandex']
browsers[1:3] = ['Opera', 'Edge']
print(browsers)

numbers = [3, 1, 4, 1, 5]
numbers[0] = 10
numbers[4] = 3
numbers[-1] = 9
print(numbers)

# Используя индексатор, дополните приведённый ниже код так, чтобы он вывел 17-ый (по порядку) элемент
# списка primes.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])

# Используя срезы, дополните приведённый ниже код так, чтобы он вывел первые 6 элементов списка primes.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])

# Дополните приведённый ниже код так, чтобы он вывел сумму минимального и максимального элементов
# списка numbers.
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
mn = min(numbers)
mx = max(numbers)
summ = [mn, mx]
print(sum(summ))

numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
res = min(numbers) + max(numbers)
print(res)

# Дополните приведённый ниже код так, чтобы он вывел среднее арифметическое элементов списка evens.
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)

# Дополните приведённый ниже код так, чтобы элемент списка имеющий значение Green заменился
# на значение Зеленый, а элемент Violet – на Фиолетовый. Далее необходимо вывести полученный список.
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'
print(rainbow)

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[rainbow.index('Green')] = 'Зеленый'
rainbow[rainbow.index('Violet')] = 'Фиолетовый'
print(rainbow)

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
for x in range(len(rainbow)):
    if rainbow[x] == "Green":
        rainbow[x] = "Зеленый"
    if rainbow[x] == "Violet":
        rainbow[x] = "Фиолетовый"
print(rainbow)

# Дополните приведённый ниже код так, чтобы он вывел "перевёрнутый" список languages
# (то есть элементы будут идти в обратном порядке).
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
languages = languages[::-1]
print(languages)

languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
languages.reverse()
print(languages)

languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda'][::-1]
print(languages)

# Используя операторы конкатенации (+) и умножения списка на число (*), дополните приведённый ниже код
# так, чтобы он вывел следующий список:
# [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
print(numbers1 * 2 + numbers2 * 9 + numbers3)


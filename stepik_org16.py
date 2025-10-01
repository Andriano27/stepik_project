

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

# Дополните приведённый ниже код, чтобы он:
# Вывел длину списка;
# Вывел последний элемент списка;
# Вывел список в обратном порядке (вспоминаем срезы);
# Вывел «YES» (без кавычек), если список содержит числа 5 и 17, или «NO» (без кавычек) в противном случае;
# Вывел список с удалёнными первым и последним элементами.
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers), numbers[-1], numbers[::-1], 'YES' if [5, 17] in numbers else 'NO', numbers[1:-1], sep='\n')

# На вход программе подаются натуральное число n, а затем n строк. Напишите программу,
# которая создаёт из указанных строк список, а затем выводит его.
n = int(input())
languages = []
for s in range(n):
    string = input()
    languages.append(string)
print(languages)

l = list()
for _ in range(int(input())):
    l.append(input())
print(l)

n, lang = int(input()), []
for i in range(n):
    lang.append(input())
print(l)

# Напишите программу, выводящую следующий список: ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
l = []  # вводим пустой список
for i in range(26):  # цикл повторяется 26 раз, от i = 0 до i = 25,
    # что соответствует 26 буквам английского алфавита
    l.append(chr(ord("a") + i)*(i + 1))  # ord("a") возвращает код буквы 'a', то есть 97,
    # ord("a") + i прибавляем i, чтобы получить код следующей буквы
    # (при i = 0: 97 + 0 = 97, 'a', при i = 1: 97 + 1 = 98, 'b'),
    # chr(ord("a") преобразует полученный код обратно в символ,
    # *(i + 1) повторяет этот символ (i + 1) раз( при i = 0 'a' * 1 = 'a', при i = 1 'b' * 2 = 'bb')
    # l.append добавляем эту строку в список
print(l)

res = []
for i in range(26):
    cur = ""
    for j in range(i + 1):
        cur += chr(ord("a") + i)
    res.append(cur)
print(res)

n = []
x = 96
for i in range(1, 27):
    n.append(chr(x+i)*i)
print(n)

abc = 'abcdefghijklmnopqrstuvwxyz'
l = []
for i in range(0, len(abc)):
    l.append(abc[i] * (i+1))
print(l)

# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу,
# которая создаёт из указанных чисел список их кубов, а затем выводит его.
n = int(input())
cube = []
for i in range(n):
    num = int(input())
    cube.append(num ** 3)
print(cube)

print([int(input()) ** 3 for i in range(int(input()))])

# На вход программе подаётся натуральное число n. Напишите программу, которая создаёт список,
# состоящий из делителей введённого числа в порядке возрастания, а затем выводит этот список.
n = int(input())
l = []
for i in range(1, n + 1):  # делители числа n лежат в диапазоне от 1 до самого n включительно
    if n % i == 0:
        l.append(i)
print(l)

n = int(input())
print([i for i in range(1, n + 1) if n % i == 0])

# На вход программе подаётся натуральное число n(n≥2). Затем поступают n целых чисел. Напишите программу,
# которая создаёт из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и так
# далее).
n = int(input())    # читаем натуральное число n — сколько далее чисел будет введено
count = 0           # вспомогательная переменная: здесь будем временно хранить "предыдущее" значение/сумму
l = []              # список, в который будем добавлять промежуточные результаты
for i in range(n):          # цикл повторяется n раз — для каждого введённого числа
    num = int(input())      # читаем очередное число
    count += num            # прибавляем его к count; на первой итерации count был 0 -> получаем a0,
                            # на второй итерации count = a0 -> count = a0 + a1 (это нужная сумма)
    l.append(count)         # добавляем текущее значение count в список
    count = num             # делаем count равным текущему числу — оно станет "предыдущим" для
    # следующей итерации
print(l[1:])    # печатаем список, начиная со второго элемента.

seq = []
for _ in range(int(input())):
    seq.append(int(input()))
res = []
for i in range(len(seq) - 1):
    res.append(seq[i] + seq[i + 1])
print(res)

n = int(input())
list_tmp = [int(input())]
list_1 = []
for i in range(n - 1):
    list_tmp.append(int(input()))
    list_1.append(list_tmp[i] + list_tmp[i + 1])
print(list_1)

# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу,
# которая создаёт из указанных чисел список, затем удаляет все элементы, стоящие по нечётным индексам,
# а затем выводит полученный список.
n = int(input())
l = []
for i in range(n):
    num = int(input())
    l.append(num)
print(l[::2])

l = []
for _ in range(int(input())):
    l.append(int(input()))
del l[1::2]
print(l)

list = []
for i in range(int(input())):
    num = int(input())
    if i % 2 == 0:
        list.append(num)
print(list)

# На вход программе подаются натуральное число n и n строк, а затем число k. Напишите программу,
# которая выводит k-ую букву из введённых строк на одной строке без пробелов.
# На вход программе подаются натуральное число n, далее n строк, каждая на отдельной строке.
# В конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).
# Если некоторые строки слишком короткие и в них нет символа с заданным номером,
# то такие строки при выводе нужно игнорировать.
n = int(input())
l = []
ind = ''
for c in range(n):
    s = input()
    l.append(s)
k = int(input())
for i in range(len(l)):
    m = l[i]  # достаем элемент(строку) из списка
    if k <= len(m):   # сравниваем (к) и длину строки
        x = m[k - 1]   # позволяет извлечь элемент строки по индексу
        ind += x  # добавляем полученную переменную в строку
print(ind)

n = int(input())
li = []
for _ in range(n):
    li.append(input())
index = int(input())
res = ''
for s in li:
    if len(s) >= index:
        res += s[index - 1]  # потому что индекс с 0, а символ - с 1
print(res)

n = int(input())
seq = []
for _ in range(n):
    seq.append(input())
k = int(input())
res = ""
for i in range(n):
    if len(seq[i]) < k:
        continue
    res += seq[i][k - 1]
print(res)

num = int(input())
arr = []              # создаём список для последующего наполнения
for i in range(num):
    str1 = input()
    arr.append(str1)  # наполняем список arr
num2 = int(input())   # вводим номер буквы под индексом
for j in arr[:]:      # обрабатываем список arr
    if len(j) >= num2:   # по условию отбираем значения не меньше num2
        print(j[num2 - 1], end='')  # печатаем букву под индексом num2 -1

# На вход программе подаются натуральное число n, а затем n строк. Напишите программу,
# которая создает список из символов всех строк, а затем выводит его.
n = int(input())
l = []
for _ in range(n):
    s = input()
    l.extend(s)
print(l)

n = int(input())
y = []
for i in range(n):
    x = input()
    for k in range(len(x)):
        z = x[k]
        y.append(z)
print(y)


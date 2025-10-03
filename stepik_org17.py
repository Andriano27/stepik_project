numbers = [3, 1, 4, 1, 5]
for i in range(len(numbers)):
    print(i, end=' ')

numbers = [3, 1, 4, 1, 5]
for i in range(len(numbers)):
    print(numbers[i], end=' ')

numbers = [3, 1, 4, 1, 5]
for i in numbers:
    print(i, end=' ')

numbers = [1, 3, 0, 2, 4]
for i in numbers:
    print(numbers[i], end=' ')

name = 'pygen'
print(*name)

numbers = [2, 10, 1, 3, 4]
total = 1
for i in range(len(numbers)):
    total = total * i
print(total)

numbers = [2, 10, 1, 3, 4]
total = 1
for i in numbers:
    total = total * i
print(total)

numbers = [2, 1, 1, 3, 4]
total = 0
for num in numbers:
    if num % 2 == 1:
        total = total + num
print(total)

# Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers.
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
square = 0
for num in numbers:
    square = square + num ** 2
print(square)

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
a = []
for i in numbers:
    a.append(i**2)
print(sum(a))

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
print(sum(i ** 2 for i in numbers))

# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу,
# которая для каждого введённого числа x выводит значение функции f(x)=x**2 + 2*x + 1,
# каждое на отдельной строке.
n = int(input())
l = []
x = 0
for i in range(n):
    num = int(input())
    x = num ** 2 + 2 * num + 1
    l.append(x)
    print(num)
print('')
print(*l, sep='\n')

n=int(input())
xs=[]
qs=[]
for i in range(1,n+1):
    x=int(input())
    xs.append(x)
    q=x*x+2*x+1
    qs.append(q)
print(*xs, sep='\n')
print()
print(*qs, sep='\n')

n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
    print(a)
print()
for j in l:
    b = j**2+2*j+1
    print(b)

n = int(input())  # ввод натурального числа n
sp = []  # создаём пустой список
for i in range(n):  # цикл в рамках натурального числа n (количество циклов равно числу n)
    x = int(input())  # ввод целого числа, данного по условию
    sp.append(x)  # добавление в список введённого ранее целого числа, данного по условию
    print(x)  # вывод на печать целого числа взятого по условию
print()  # печать пустой строки для создания пробела
for i in sp:  # цикл в рамках созданного списка
    x = i ** 2 + 2 * i + 1  # создаём переменную Х для вычисления по формуле
    print(x)  # вывод на печать найденного значения переменной Х

# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое
# и самое маленькое значение. На вход программе подаются натуральное число n, а затем
# n различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение
# из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
n = int(input())
l = []
for i in range(n):
    num = int(input())
    l.append(num)
s = min(l)
m = max(l)
for j in l:
    if j != s and j != m:
        print(j)

n = int(input())
mx_ind = 0
mn_ind = 0
seq = []
for _ in range(n):
    seq.append(int(input()))
for i in range(n):
    if seq[i] > seq[mx_ind]:
        mx_ind = i
    if seq[i] < seq[mn_ind]:
        mn_ind = i
del seq[max(mx_ind, mn_ind)]
del seq[min(mx_ind, mn_ind)]
print(*seq, sep="\n")

a = [int(input()) for i in range(int(input()))]
for i in a:
    if min(a) < i < max(a):
        print(i)

# На вход программе подаются натуральное число n, а затем n строк. Напишите программу,
# выводящую только уникальные строки, в том же порядке, в котором они были введены.
n = int(input())
l = []
for _ in range(n):
    string = input()
    if string not in l:
        l.append(string)
print(*l, sep='\n')

n = int(input())
numbers_in = list()
numbers_out = list()
for _ in range(n):
    numbers_in.append(input())
for i in range(n):
    if numbers_in[i] not in numbers_out:
        numbers_out.append(numbers_in[i])
print(*numbers_out, sep='\n')

# На вход программе подаются натуральное число n, затем n строк, затем ещё одна строка –
# поисковый запрос. Напишите программу, выводит все введённые строки,
# в которых встречается поисковый запрос.
n = int(input())  # вводим число
l = []  # создаем список
for _ in range(n):  # создаем цикл
    string = input()  # вводим строки
    l.append(string)  # добавляем строки в список
quest = input()  # Делаем запрос
for s in l:  # создаем цикл по длине списка
    if quest.lower() in s.lower():  # Чтобы привести к одному регистру
        print(s, sep='\n')

# put your python code here
n = int(input())                            # ввод к-ва элементов
words = [(input()) for _ in range(n)]     # ввод элементов в виде цикла
search = input()                            # поисковый запрос
for word in words:                          # перебираем слова word в списке Words
    if search.lower() in word.lower():      # если поисковый запрос совпадает с word, то
        print(word)

# На вход программе подаются натуральное число n, затем n строк, затем число k – количество поисковых
# запросов, затем k строк – поисковые запросы. Напишите программу, она выводит все введённые строки,
# в которых встречаются одновременно все поисковые запросы.
n = int(input())
l = []
q = []
s_q = []
for _ in range(n):
    string = input()
    l.append(string)
k = int(input())
for _ in range(k):
    quest = input()
    q.append(quest)
for s in range(len(l)):
    count = 0
    for c in range(len(q)):
        if q[c].lower() in l[s].lower():
            count += 1
        if count == len(q):
            s_q.append(l[s])
print(*s_q, sep='\n')

n = int(input())
# принимаем все строки
strings = []
for _ in range(n):
    s = input()
    strings.append(s)
k = int(input())
# принимаем все поисковые запросы
search_queries = []
for _ in range(k):
    search_query = input()
    search_queries.append(search_query)
# идём по каждой строке
for s in strings:
    # идём по каждому запросу
    for search_query in search_queries:
        # если хотя бы какого-то поискового запроса не оказывается в строке,
        # то выходим из этого цикла
        if search_query.lower() not in s.lower():
            break
    else:
        # если мы не вышли из цикла через break,
        # значит, все поисковые запросы были найдены в строке
        print(s)

n = int(input())
# принимаем все строки
strings = []
for _ in range(n):
    s = input()
    strings.append(s)
k = int(input())
# принимаем все поисковые запросы
search_queries = []
for _ in range(k):
    search_query = input()
    search_queries.append(search_query)
# идём по каждой строке
for s in strings:
    # создаём счётчик для подсчёта кол-ва запросов,
    # которые найдены в текущей строке
    cnt = 0
    # идём по каждому запросу
    for search_query in search_queries:
        # если запрос найден в строке, то увеличиваем счётчик
        if search_query.lower() in s.lower():
            cnt += 1
    # если счётчик равен кол-ву запросов,
    # значит, в текущей строке
    # были найдены все запросы
    if cnt == k:
        print(s)

s = []  # объявляем основной список
p = []  # объявляем поисковый список
for _ in range(int(input())):  # количество элементов основного списка
    s.append(input())  # добавляем элементы
for _ in range(int(input())):  # количество элементов поискового списка
    p.append(input())  # добавляем элементы
for i in s:  # Ищем для каждого элемента основного списка
    n = 0  # счётчик совпадений
    for k in p:  # сравниваем наличие элемента из списка поиска с основным
        if k.lower() in i.lower():  # если совпадение найдено:
            n += 1  # счётчик прибавляет значение
    if n >= len(
            p):  # если счётчик совпадений равен или больше количеству элементов поискового списка,
        # печатаем элемент из основного списка.
        print(i)

# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу,
# которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа,
# каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
n = int(input())
l = []
o = []
p = []
for _ in range(n):
    num = int(input())
    if num < 0:
        l.append(num)
    elif num == 0:
        o.append(num)
    elif num > 0:
        p.append(num)
print(*l, sep='\n')
print(*o, sep='\n')
print(*p, sep='\n')

negatives, zeros, positives = [], [], []
n = int(input())
for _ in range(n):
    cur = int(input())
    if cur < 0:
        negatives.append(cur)
    elif cur > 0:
        positives.append(cur)
    else:
        zeros.append(cur)
res = negatives + zeros + positives
print(*res, sep="\n")


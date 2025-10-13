numbers = [2, 2, 3, 6, 0]
print(numbers.sort())
print(numbers)

numbers = ['10', '5', '9', '1', '11']
numbers.sort()
print(numbers)

words = ['aunt', 'Anton', 'Anna', 'a', 'an']
words.sort()
print(words)

numbers = [8, 9, 10, 11]
numbers.remove(9)
numbers.insert(1, 17)
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.pop(0)
numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)

colors = list('Red Orange red Purple Red Red')  # ['R', 'e', 'd', ' ', 'O', 'r', 'a', 'n', 'g', 'e', ' ', 'R', 'e', 'd']
print(colors.count('Red'))  # После оборачивания в список строка разбивается посимвольно

colors = ['Grey', 'White', 'Black', 'Red']
print(colors.reverse())  # reverse() - не возвращает значение!
print(colors)

numbers = [8, 9, 10, 11]
numbers[1] = 17  # заменяем элемент списка
numbers.extend([4, 5, 6])  # добавляем элементы в конец списка
del numbers[0]  # удаляем элемент списка по индексу
numbers *= 2  # удваиваем список
numbers.insert(3, 25)  # вставляем элемент в список
print(numbers)

# На вход программе подаётся строка, содержащая английский текст. Напишите программу, которая подсчитывает
# общее количество артиклей: a, an, the. На вход программе подаётся строка, содержащая английский текст.
# Слова текста разделены символом пробела. Артикли могут начинаться с заглавной буквы A, An, The.
string = input()
count = 0
st = string.upper()
street = st.split()
cnt1 = street.count('A')
count += cnt1
cnt2 = street.count('AN')
count += cnt2
cnt3 = street.count('THE')
count += cnt3
print('Общее количество артиклей:', count)

seq = input().lower().split()
res = seq.count("a") + seq.count("an") + seq.count("the")
print(f"Общее количество артиклей: {res}")
# lower() должен быть указан перед split(), т.к. lower() можно применить только к строке,
# а если мы сначала применим split(), то это будет уже список, а у списка нет метода lower()

text = input().lower().split()
articles = ['a', 'the', 'an']
total = 0
for i in text:
    if i in articles:
        total += 1
print(f"Общее количество артиклей: {total}")

# На вход программе подаётся строка текста, содержащая различные натуральные числа.
# Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку.
string = input()
st = string.split()
int_st = [int(x) for x in st]
st1 = min(int_st)
st2 = max(int_st)
pos1 = int_st.index(st1)
pos2 = int_st.index(st2)
delete1 = int_st.pop(pos1)
int_st.insert(pos1, st2)
delete2 = int_st.pop(pos2)
int_st.insert(pos2, st1)
print(*int_st)

seq = []
for el in input().split():
    seq.append(int(el))
mx_ind = seq.index(max(seq))
mn_ind = seq.index(min(seq))
seq[mx_ind], seq[mn_ind] = seq[mn_ind], seq[mx_ind]

l = [int(i) for i in input().split()]
x = l.index(min(l))
y = l.index(max(l))
l[x], l[y] = max(l), min(l)
print(*l)

s = input().split()
s_min = min(s, key=int)
s_max = max(s, key=int)
i_min = s.index(s_min)
i_max = s.index(s_max)
s[i_max] = s_min
s[i_min] = s_max
print(*s, sep=' ')

# 1. получаем строку и разделяем ее в список
numbers = input().split()
# 2. в цикле значения строки списка numbers преобразуем в целое число
for i in range(len(numbers)):
    numbers = int(numbers[i])
# 3. находим минимальный и максимальный индексы
index_max = numbers.index(max(numbers))
index_min = numbers.index(min(numbers))
# 4. переписываем значения
numbers[index_min], numbers[index_max] = numbers[index_max], numbers[index_min]
# 5. Выведем список, с помощью функции print()
print(*numbers)

# На первой строке подаётся символ решётки и сразу же натуральное число n – количество строк в программе,
# не считая первой. Далее следуют n строк кода. Нужно вывести те же строки, но удалить комментарии и
# символы пустого пространства в конце строк. Пустую строку вместо первой строки ввода выводить не надо.
st = input()  # считываем строку вида #12
n = int(st[1:])  # отбрасываем '#' и превращаем в число
for _ in range(n):  # создаем цикл
    s = input()  # в цикле читаем каждую строку
    if '#' in s:  # если символ '#' есть в строке
        s = s.split('#')[0]  # оставляем все до символа '#'
    print(s.rstrip())  # убираем пробелы и табуляцию в конце строки

n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

# считаем кол-во строк в программе
n = int(input()[1:])
for _ in range(n):
    # принимаем текущую строку
    s = input()
    # ищем символ # в строке
    hash_index = s.find("#")
    # если нашли символ # в строке
    if hash_index != -1:
        # присваиваем для s новую строку,
        # где убираем # и всё, что после #
        s = s[:hash_index]
    # убираем пробелы справа
    s = s.rstrip()
    print(s)

n = input()    # Ввод первой строки
n = n.replace('#', '')    # Удаляем "#" из первой строки
n = int(n)    # Заменяем строку на число
for i in range(n):
    s = input()
    if '#' in s:    # Проверка каждой введенной строки на наличие "#"
        a = s.find('#')    # Индекс первого вхождения "#"
        b = s.replace(s[a::], '')    # Удаляем все символы после "#"
        s = b.rstrip()    # Удаляем пробелы ДО "#"
        print(s)
    else:    # Если в строке изначально нет комментария
        print(s)

# На вход программе подаётся строка текста, содержащая целые числа. Из данной строки формируется
# список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию,
# а затем по убыванию.
n = input().split()  # считываем строку и разбиваем на элементы
num = []  # создаем пустой список
for i in n:
    num.append(int(i))  # преобразуем каждый элемент строки в целое число и добавляем в новый список
num.sort()  # сортируем список по возрастанию и выводим
for j in num:
    print(j, end=' ')
print()
num.sort(reverse=True)  # сортируем список по убыванию и выводим
for j in num:
    print(j, end=' ')
print()

seq = []
for el in input().split():
    seq.append(int(el))
seq.sort()
print(*seq)
seq.reverse()
print(*seq)

n = input().split()   # считываем данные
for i in range(len(n)):     # запускаем цикл
    n = int(n[i])        # преобразуем строковые данные в цифровые
n.sort()              # сортируем список
print(*n)             # выводим на печать 1-ую строку
n.sort(reverse=True)  # переворачиваем отсортированный список
print(*n)             # выводим на печать 2-ую строку

# На вход программе подаются число n, а затем – n песен из плейлиста Сэма, каждая на отдельной строке.
# Напишите программу, которая сортирует эти песни в алфавитном порядке и выводит каждую из них
# на отдельной строке.
n = int(input())  # вводим число
playlist = []  # создаем список
for _ in range(n):  # создаем цикл по длине введенного числа
    song = input()  # вводим песни в цикле
    playlist.append(song)  # добавляем введенные песни в список
playlist.sort()  # сортируем список по алфавиту
for song in playlist:  # создаем цикл для списка песен
    print(song)  # печатаем песни из списка на каждой строке

n = int(input())
songs = []
for _ in range(n):
    song = input()
    songs.append(song)
songs.sort()
print(*songs, sep='\n')



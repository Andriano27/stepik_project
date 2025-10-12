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


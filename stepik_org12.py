s = input()
c = s[::-1]
print(s + c)

s = input()
print(s[::2])

s = "hello world python"
s = s[:5] + '_' + s[6:11] + '_' + s[12:]
print(s)

s1 = 'a'
s2 = s1.upper()
print(s1, s2)

# На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
s = input()
c = s.title()
if s == c:
    print('YES')
else:
    print('NO')

s = input()
name = s[0:s.find(' ')]      # Находим имя (оно до пробела)
surname = s[s.find(' ')+1:]  # Находим фамилию (после пробела)
s2 = surname.capitalize()    # Создаем строку, в которой фамилия начинается с заглавной буквы
s3 = name.capitalize()       # Создаем строку, в которой имя начинается с заглавной буквы
if s3 == name and s2 == surname:  # Сравниваем, одинаковы ли строки
    print('YES')
else:
    print('NO')

# На вход программе подаётся строка текста. Напишите программу, которая определяет,
# является ли оттенок текста хорошим или нет. Текст имеет хороший оттенок,
# если содержит подстроку «хорош» (без кавычек) во всевозможных регистрах.
s = input()
c = s.lower()
if 'хорош' in c:
    print('YES')
else:
    print('NO')

# На вход программе подаётся строка. Напишите программу, которая подсчитывает количество буквенных
# символов в нижнем регистре.
s = input()
count = 0
for i in range(len(s)):
    if s[i] in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
print(count)

s, counter = input(), 0
for i in s:
    if i != i.upper():  # условие выполняется только для букв в нижнем регистре
        counter += 1
print(counter)

x = input()
y = x.lower()
total = 0
for i in x:
    if i in y and i not in '0123456789':
        total += 1
print(total)


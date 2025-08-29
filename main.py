# Начало курса
def get_sum(a, b) -> int:
    return a + b

print(get_sum(5, 7))

print('мы изучаем язык Python')
print()
print('Я','учусь','программировать','на ','Python')
print('В данном тексте используются "двойные" кавычки.')
print('4', '8', '15', '16', '23', '42')

print('Как тебя зовут?')
print('Привет,', input())  # в терминале написать свое имя и нажать Enter

variable_name = input()
print('Вы ввели текст:', variable_name)  # дать имя переменной variable_name

city = 'Тула'
print(city, '- мой город!')

name = 'Алеша'
city = 'Тула'
print('Меня зовут', name, '.', city, '- мой город!')

name1 = 'Тимур'
name2 = name1
name1 = 'Гвидо'
print(name1)
print(name2)

first = input()
second = input()
print('I am', first, 'and', second)  # вводим данные переменной first и переменной second

print('aa', 'bb', 'cc', sep='*')

minus = '-'
print('aa', 'bb', 'cc', sep=minus)

minus = '-'
print('a', 'b', 'c', end=minus)
print('second line')

print('a', '\n', 'b', '\n', 'c', sep='*', end='#')

print('a', 'b', 'c', sep='*', end='finish')

arg1 = 'Hello'
sep1 = '_-_'
end2 = '+++'

print(arg1, 'everyone', sep=sep1, end='! ')
print('How', 'are', 'you', 'in', '2024?', sep=' ', end=end2)

print('a', 'b', 'c', sep='', end='')
print('d', 'e', 'f', sep='', end='')

print('YES', sep='!', end='#')
print('NO', sep='#', end='!')

name = input()
print('Привет,', name, end='')
print('!')

name = input()
print('Привет,', name, end='!')

str0 = input()
str1 = input()
str2 = input()
str3 = input()
print(str1, str2, str3, sep=str0)

name = 'Timur'
surname = 'Guev'
print('Имя:', name, 'Фамилия:', surname)

num1 = input()
num2 = input()

print(num1 + num2)

num1 = int(input())
num2 = int(input())

print(num1 + num2)

num1 = int(input())
num2 = 1
num3 = num1 + num2
num4 = num3 + num2
print(num1)
print(num3)
print(num4)

n = int(input())                  # Вводим число, добавляем к нему последовательно единицу и еще раз
print(n, n + 1, n + 2, sep='\n')  # единицу, после чего делаем разделение с новой строки,
                                  # чтобы каждое шло на отдельной строчке.

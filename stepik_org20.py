team = ['Arthur', 'Timur', 'Anton', 'Valera', 'Arthur', 'Sveta']
lengths = [len(name) for name in team]
print(*lengths)

expression = '5 + 5 * 2 = 15'
digits = [int(c) for c in expression if c.isdigit()]
print(digits)

binary = [str(i) + str(j) for i in range(2) for j in range(2)]
print(binary)

result = [i for i in [1, 2, 3, 5, 7] if i != 2]
print(result)

result = [i for i in range(1, 8, 2)]
print(result)

result = [i + 1 for i in range(0, 7, 2)]
print(result)

result = [int(i) for i in '1357']
print(result)

result = [i for i in range(8) if i % 2 == 0]
print(result)

result = [i // 2 for i in range(0, 13, 4)]
print(result)

result = [int(i) + len(i) for i in '0135']
print(result)

food = ['pizza', 'burger', 'sushi', 'salad']
dish = [dish for dish in food if dish[0] == 's']
print(dish)

food = ['pizza', 'burger', 'sushi', 'salad']
dish = [dish.count('a') for dish in food]
print(dish)

food = ['pizza', 'burger', 'sushi', 'salad']
dish = [dish.count(dish[-1]) for dish in food]
print(dish)

food = ['pizza', 'burger', 'sushi', 'salad']
dish = [dish for dish in food[::2] if len(dish) == 5]
print(dish)

food = ['pizza', 'burger', 'sushi', 'salad']
dish = [dish for dish in food[-1:-3:-1]]
print(dish)

food = ['pizza', 'burger', 'sushi', 'salad']
[dish.find('s') for dish in food]
print(dish)

# Используя списочное выражение, дополните приведённый ниже код так, чтобы получить новый список,
# содержащий строки исходного списка, где у каждой строки удалён первый символ.
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [s[1:] for s in keywords]
print(new_keywords)

# Используя списочное выражение, дополните приведённый ниже код так, чтобы получить новый список,
# содержащий длины строк исходного списка.
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(word) for word in keywords]
print(lengths)

# Используя списочное выражение, дополните приведённый ниже код так, чтобы получить новый список,
# содержащий только слова длиной не менее пяти символов (включительно).
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [word for word in keywords if len(word) > 4]
print(new_keywords)

a = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
b = []
for i in range(len(a)):
    if len(a[i]) >= 5:
        b.append(a[i])
print(b)

# Используя списочное выражение, дополните приведённый ниже код так, чтобы получить список всех целых
# чисел-палиндромов от 100 до 1000 (включительно) в порядке возрастания.
palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
print(palindromes)

palindromes = [i for i in range(100, 1001) if i // 100 == i % 10]
print(palindromes)

# На вход программе подаётся натуральное число n. Напишите программу, использующую списочное выражение,
# которая создаёт список, содержащий квадраты чисел от 1 до n (включительно),
# а затем выводит его элементы построчно, то есть каждый на отдельной строке.
n = int(input())
square = [n ** 2 for n in range(1, n + 1)]
print(*square, sep='\n')

n = int(input())
squares = [el ** 2 for el in range(1, n + 1)]
for el in squares:
    print(el)

print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')

# На вход программе подаётся строка текста, содержащая целые числа. Напишите программу,
# использующую списочное выражение, которая выведет кубы указанных чисел на одной строке.
s = input()
digits = s.split()
cubes = [int(i)**3 for i in digits]
print(*cubes)

cubes = [int(el)**3 for el in input().split()]
print(*cubes)

# На вход программе подаётся строка текста, содержащая слова. Напишите программу, которая выводит
# слова введённой строки в столбик.
s = input()
words = s.split()
new_words = [word for word in words]
print(*new_words, sep='\n')

words = [word for word in input().split()]
print(*words, sep='\n')

print(*input().split(), sep='\n')

# На вход программе подаётся строка текста. Напишите программу, использующую списочное выражение,
# которая выводит все цифровые символы данной строки.
s = input()
digit = [i for i in s if i.isdigit()]
print(*digit, sep='')

digits = [el for el in input() if el.isdigit()]
print(*digits, sep="")

# На вход программе подаётся строка текста, содержащая целые числа.
# Напишите программу, использующую списочное выражение, выводящее квадраты чётных чисел,
# кроме квадратов, которые оканчиваются на цифру 4.
s = input()
digits = s.split()
square = [int(i)**2 for i in digits if int(i) % 2 == 0 and (int(i)**2) % 10 != 4]
print(*square)

print(*[int(el) ** 2 for el in input().split() if int(el) % 2 == 0 and int(el) ** 2 % 10 != 4])



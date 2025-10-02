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


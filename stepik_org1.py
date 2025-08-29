n = int(input())        # на вход дается одно число, если оно нечетное, при делении
people = (n + 1) // 2   # пополам должно получаться число на единицу больше половины.

print(people)

print(-123//10)
print((-10)**3)


n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print((n1+n2+n3+n4)*3)

a = int(input())
b = int(input())

function = 3*((a+b)*(a+b)*(a+b))+275*(b*b)-127*a-41

print(function)

num = int(input())

print('Следующее за числом', num, 'число:', (num+1))
print('Для числа', num, 'предыдущее число:', (num - 1))

n = int(input())
print('Следующее за числом ', n, ' число: ', n + 1, '\n', 'Для числа ', n, ' предыдущее число: ', n - 1, sep='')

l = int(input())
v = l*l*l
s = 6*(l*l)
print('Объем =', v,'\n''Площадь полной поверхности =', s)

a = int(input())
b = int(input())

print(str(a), '+', str(b), '=', a + b)
print(str(a), '-', str(b), '=', a - b)
print(str(a), '*', str(b), '=', a * b)

x = int(input())

print(x, 2*x, 3*x, 4*x, 5*x, sep='---')

scool = int(input())
citrus = int(input())
point = citrus // scool
remainder = citrus % scool

print(point, remainder, sep='\n')

n = int(input())
a = n // 10000
b = n % 10000 // 1000
c = n % 1000 // 100
d = n % 100 // 10
e = n % 10
print(a, b, c, d, e)




num = int(input())
c = num % 10
b = (num // 10) % 10
a = num // 100
number1 = str(a) + str(b) + str(c)
number2 = str(a) + str(c) + str(b)
number3 = str(b) + str(a) + str(c)
number4 = str(b) + str(c) + str(a)
number5 = str(c) + str(a) + str(b)
number6 = str(c) + str(b) + str(a)
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)
print(number6)

number = int(input())

d1 = (number // 10 ** 2) % 10
d2 = (number // 10 ** 1) % 10
d3 = (number // 10 ** 0) % 10

print(d1, d2, d3, sep="")
print(d1, d3, d2, sep="")
print(d2, d1, d3, sep="")
print(d2, d3, d1, sep="")
print(d3, d1, d2, sep="")
print(d3, d2, d1, sep="")

a,b,c = input()
print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')

num = int(input())
d = num % 10
c = num // 10 % 10
b = num // 100 % 10
a = num // 1000

print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)
print("Сумма цифр = ", digit1 + digit2 + digit3, "\nПроизведение цифр = ", digit1 * digit2 * digit3, sep="")

a = str(input())
print('Сумма цифр =', int(a[0]) + int(a[1]) + int(a[2]))
print('Произведение цифр =', int(a[0]) * int(a[1]) * int(a[2]))


n = 123456789  // 1 % 10
print(n)


# на вход в программе подается целое число - место в купе в вагоне.
# в вагоне всего 9 купе в каждом по 4 места, с 1-4, 5-8, 9-12 и т.д.
# нужно по заданному номеру места узнать номер купе.
plats = int(input())    # место в вагоне
coupe = (plats - 1) // 4 + 1  # номер места делим без остатка на количество мест в купе, и прибавляем 1
print(coupe)

a = int(input())
print((a + 3) // 4)

n=int(input())
k=(36-n)//4
k=9-k
print(k)

a = int(input())
m = "минут"
ms = "минуты"
ma = "минута"
b = a // 60
c = (a % 60)
def minut():
    if a%10 in [0,5,6,7,8,9,]:
        return m
    elif a%10 in [2, 3, 4]:
        return ms
    elif a%100 in [11,12,13,14]:
        return m
    elif a%10 == 1:
        return ma
n = minut()
h = "часов"
hs = "часа"
ha = "час"
def hour():
    if b in [0, 5, 6, 7, 8, 9]:
        return h
    elif b in [2, 3, 4, 22, 23, 24]:
        return hs
    elif b in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        return h
    elif b in [1, 21]:
        return ha
s = hour()
print(a, n, "- это", b, s, c, n)

num = 17
a = num % 10             # вычисляем последнюю цифру числа
b = num // 10            # вычисляем первую цифру числа

print(a)
print(b)

num = 754
a = num % 10             # вычисляем последнюю цифру числа
b = (num % 100) // 10    # вычисляем среднюю цифру числа
c = num // 100           # вычисляем первую цифру числа

print(a)
print(b)
print(c)


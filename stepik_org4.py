# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч.
# Определите, через какое время (в часах) старушки встретятся, если расстояние между ними равно S км.
s = float(input())
v1 = float(input())
v2 = float(input())

v = v1 + v2  # скорость сближения
time = s / v
print(time)

num = float(input())
if num == 0:
    print('Обратного числа не существует')
else:
    num1 = num ** -1
    print(num1)

# Для получения градусов по Цельсию из градусов по Фаренгейту:
tf = float(input())

tc = (5 / 9) * (tf - 32)
print(tc)

# На вход программе подаётся число n – количество собачьих лет. Вычислите возраст собаки в человеческих годах
# по следующему алгоритму: в течение первых двух лет собачий год равен 10.5 человеческим годам,
# после этого каждый год собаки равен 4 человеческим годам.
n = int(input())

if 0 < n < 3:
    print(n * 10.5)
else:
    print(21 + (n - 2) * 4)

# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
n = float(input())
a = int(n * 10)  # отбрасываем дробную часть, переводя при этом нужное число перед запятой в целую часть.
b = a % 10  # находим последнюю цифру числа
print(b)

# Дано положительное действительное число. Выведите его дробную часть.
n = float(input())
a = n - int(n)
print(a)


a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))


name = input()
surname = input()
print('Hello' + ' ' + name + " " + surname + "!" + ' ' + 'You have just delved into Python')

club = input()
print('Футбольная команда' + ' ' + club + ' ' + 'имеет длину' + ' ' + str(len(club)) + ' ' + 'символов')

team_name = input()
team_len = len(team_name)
print('Футбольная команда', team_name, 'имеет длину', team_len, 'символов')

# Даны названия трёх городов. Определите самое короткое и самое длинное название города.
city1 = input()
city2 = input()
city3 = input()

len_city1 = len(city1)
len_city2 = len(city2)
len_city3 = len(city3)

min_city = min(len_city1, len_city2, len_city3)
max_city = max(len_city1, len_city2, len_city3)

if len_city1 == min_city:
    print(city1)
elif len_city2 == min_city:
    print(city2)
else:
    print(city3)
if len_city1 == max_city:
    print(city1)
elif len_city2 == max_city:
    print(city2)
else:
    print(city3)

# Вводятся 3 строки в случайном порядке. Выяснить, можно ли из длин этих строк построить
# арифметическую прогрессию.
str1 = input()
str2 = input()
str3 = input()

len_str1 = len(str1)
len_str2 = len(str2)
len_str3 = len(str3)

min_len = min(len_str1, len_str2, len_str3)
max_len = max(len_str1, len_str2, len_str3)
midl_len = (len_str1 + len_str2 + len_str3) - (min_len + max_len)
if max_len - midl_len == midl_len - min_len:
    print('YES')
else:
    print('NO')

len_1 = len(input())
len_2 = len(input())
len_3 = len(input())

if (2 * len_1 - len_2 - len_3) * (2 * len_2 - len_1 - len_3) * (2 * len_3 - len_1 - len_2) == 0:
    print('YES')
else:
    print('NO')

# Программа, которая считывает одну строку, после чего выводит «YES» (без кавычек),
# если во введённой строке есть подстрока «синий», или «NO» (без кавычек) в противном случае.
text = input()
s = 'синий'
if s in text:
    print('YES')
else:
    print('NO')

# Программа считывает одну строку, после чего выводит «YES» (без кавычек),
# если во введённой строке есть подстрока «суббота» или «воскресенье», или «NO» (без кавычек) в противном случае.
ctr = input()
a = 'суббота'
b = 'воскресенье'
if a in ctr or b in ctr:
    print('YES')
else:
    print('NO')

# Будем считать email адрес корректным, если в нём есть символы собачки (@) и точки (.).
# Проверим корректность email адреса.
email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')

# Определить евклидово расстояние между двумя точками, координаты которых заданы.
import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(p)

from math import pow, sqrt

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

print(distance)

# вывести два числа (каждое на отдельной строке) – площадь круга и длину окружности радиуса R.
r = float(input())
import math
s = math.pi * (r ** 2)
c = 2 * math.pi * r
print(s)
print(c)

from math import pi
R = float(input())
circle_area = pi * R ** 2
circle_lenght = 2 * pi * R
print(circle_area, circle_lenght, sep="\n")

# Вычислить среднее арифметическое, геометрическое, гармоническое и квадратичное.
a = float(input())
b = float(input())
import math
arith_mean = (a + b) / 2
geom_mean = math.sqrt(a * b)
harm_mean = 2 * a * b / (a + b)
mean_square = math.sqrt((math.pow(a, 2) + math.pow(b, 2)) / 2)
print(arith_mean)
print(geom_mean)
print(harm_mean)
print(mean_square)

# Вычисляем значение тригонометрического выражения по заданному числу градусов x.
x = float(input())
import math
r = math.pi * x / 180
meaning = math.sin(r) + math.cos(r) + math.pow(math.tan(r), 2)
print(meaning)

from math import sin, cos, tan, radians
angle = radians(float(input()))
res = sin(angle) + cos(angle) + tan(angle) ** 2
print(res)

# Найти действительные корни квадратного уравнения: Если уравнение имеет один корень, то нужно вывести его,
# а если уравнение имеет два корня, то следует вывести их в порядке возрастания, каждый на отдельной строке.
# При этом если уравнение не имеет действительных корней, то программа должна вывести текст
# «Нет корней» (без кавычек).
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
x = -(b / (2 * a))
x1 = (-b - d ** 0.5) / (2 * a)
x2 = (-b + d ** 0.5) / (2 * a)

if d > 0:
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    print(x)
else:
    print('Нет корней')

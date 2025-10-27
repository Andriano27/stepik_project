def draw_box():
    for _ in range(5):
        print('*' * 7)
draw_box()
print()
draw_box()
print()
draw_box()

# объявление функции
def print_message():
    print('Я - Артур,')
    print('король британцев. ')
# вызов функции
print_message()

def welcome():
    print('Добро пожаловать!')
print('Начинаем изучать функции')
welcome()

# Напишите функцию draw_box(), которая выводит звёздный прямоугольник с размерами 14×10
def draw_box():
    for i in range(1, 15):
        if i == 1 or i == 14:
            print('*' * 10)
        else:
            print('*' + ' ' * 8 + '*')
draw_box()

def draw_box():
    print("*" * 10)
    for i in range(12):
        print("*", "*", sep=" " * 8)
    print("*" * 10)
draw_box()

def draw_box():
    print('*'*10 + '\n' + ('*' + ' '*8 + '*\n')*12 + '*'*10)
draw_box()

# Напишите функцию draw_triangle(), которая выводит звёздный прямоугольный треугольник с катетами, равными 10
def draw_triangle():
    for i in range(10):
        print((1 + i) * '*')
draw_triangle()

def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')
draw_triangle()

def draw_triangle():
    for i in range(1, 11):
        print('*' * i)
draw_triangle()


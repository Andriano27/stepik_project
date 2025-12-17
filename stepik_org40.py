def from_decimal_system():
    while True:
        num = input('Введите число: \n')
        if num.isdigit():
            num = int(num)
            break
        else:
            print('Некорректный ответ, попробуйте заново.')
            continue

    while True:
        print('Введите цифру или число для выбора системы счисления, в которую нужно перевести ваше число:')
        print('2 - двоичная | 4 - четверичная | 8 - восьмеричная | 16 - шестнадцатиричная и т.д.')
        system = input()

        if system == '10':
            print('В этом нет смысла! Зачем переводить число в его же систему счисления?')
            continue
        elif system.isdigit() and int(system) >= 2:
            system = int(system)
            break
        else:
            print('Некорректный ответ, попробуйте заново.')
            continue

    num_list = []

    while num:
        if system >= 10 and num % system >= 10:
            num_list.append(chr(num % system + 55))
        else:
            num_list.append(num % system)
        num //= system

    print('Число в выбранной системе счисления:')
    print(*num_list[::-1], sep ='')

def to_decimal_system():
    while True:
        num = input('Введите число: \n')
        if num.isdigit():
            break
        else:
            print('Некорректный ответ, попробуйте заново.')
            continue

    num_list = []

    for c in num:
        if c.isalpha():
            num_list.append(ord(c) - 55)
        else:
            num_list.append(int(c))

    while True:
        print('Введите цифру или число системы счисления, в которой находится ваше число:')
        print('2 - двоичная | 4 - четверичная | 8 - восьмеричная | 16 - шестнадцатиричная и т.д.')
        system = input()

        if system == '10':
            print('В этом нет смысла! Зачем переводить число в его же систему счисления?')
            continue
        elif system.isdigit() and int(system) >= 2:
            system = int(system)
            break
        else:
            print('Некорректный ответ, попробуйте заново.')
            continue

    total = 0
    num_list = num_list[::-1]

    for i in range(len(num_list)):
        total += num_list[i] * system ** i

    print('Число в десятичной системе счисления:')
    print(total)

print('Добро пожаловать в программу для перевода чисел из одной системы счисления в другую!')

while True:
    print('Введите цифру для выбора действия:')
    print('1 - перевод из десятичной системы в любую другую | 2 - перевод из любой другой системы в десятичную')
    choice_action = input()
    if choice_action == '1':
        from_decimal_system()
        break
    elif choice_action == '2':
        to_decimal_system()
        break
    else:
        print('Некорректный ответ, попробуйте заново.')
        continue
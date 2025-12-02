import random

cnt = 0  # счётчик попыток
entr = 1  # задание диапазона
ext = 100  # задание диапазона
rnd = random.randint(entr, ext)  # загадка


# -----------ФУНКЦИЯ ПРОВЕРКИ ВВОДА ЧИСЛА----------

def is_vld_inpt_nmbr(inpt_nmbr):
    vld = True
    while vld:
        if inpt_nmbr.isdigit() and entr <= int(inpt_nmbr) <= ext:
            vld = False
        else:
            print()
            print(f'Может быть, постараетесь ввести именно число, от {entr} до {ext}?..')
            inpt_nmbr = input(f'Попробуйте ещё раз, ведите число от {entr} до {ext}... ')
    return inpt_nmbr


# -----------ФУНКЦИЯ ПРОВЕРКИ ВВОДА ДИАПАЗОНА----------
def is_vld_rng_nmbr(rng_nmbr):
    vld = True
    while vld:
        if rng_nmbr.isdigit():
            vld = False
        else:
            print()
            print('Может быть, постараетесь ввести именно целое число?..')
            rng_nmbr = input('Попробуйте ещё раз, ведите целое число... ')
    return rng_nmbr


# ------ФУНКЦИЯ ПРОВЕРКИ БОЛЬШЕ ИЛИ МЕНЬШЕ----

def mr_lss(srch_nmbr):
    if srch_nmbr < rnd:
        print()
        print(srch_nmbr, 'слишком мало.')
        return is_vld_inpt_nmbr(input(f'Попробуйте ещё раз, ведите число от {entr} до {ext}... '))
    elif srch_nmbr > rnd:
        print()
        print(srch_nmbr, 'слишком много.')
        return is_vld_inpt_nmbr(input(f'Попробуйте ещё раз, ведите число от {entr} до {ext}... '))
    else:
        return str(rnd)


# --------------ФУНКЦИЯ ИГРЫ------------------

def gm(x):
    x = is_vld_inpt_nmbr(x)
    global cnt
    cnt = 1
    while int(x) != rnd:
        x = int(x)
        x = mr_lss(x)
        cnt += 1


# ----------------ИГРА-----------------

y = 'y'  # первая игра
if cnt == 0:
    print('Привет, я загадываю числа, а Вы их угадываете.')
    x = input(f'Угадайте число от {entr} до {ext}...   ')
    gm(x)
    print()
    print(f'Та-та-м!!! Вы угадали c {cnt} раз, поздравляем!!!', sep='\n')
    print('Было загадано число -', rnd)
    print()
    while y == 'y':  # вторая и последующие игры
        print('Хотите сыграть ещё раз? Может быть, другие числа?..', end='  ')
        y = input('y/n?')
        if y == 'n':
            print()
            print('Ну, ты заходи, если что...')
        elif y == 'y':
            print()
            entr = int(is_vld_rng_nmbr(input('Задайте нижнюю границу диапазона...   ')))
            ext = int(is_vld_rng_nmbr(input('Задайте верхнюю границу диапазона...   ')))
            if entr > ext:
                ext, entr = entr, ext
            rnd = random.randint(entr, ext)
            print()
            x = input(f'Угадайте число от {entr} до {ext}...   ')
            gm(x)
            print()
            print(f'Та-та-м!!! Вы угадали c {cnt} раз, поздравляем!!!', sep='\n')
            print('Было загадано число -', rnd)

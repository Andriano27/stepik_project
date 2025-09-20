print('Cyberpunk 2077'.isalnum())

n = int(input())

# Написать программу, которая поможет Сэму проверять комментарии. Программа должна принимать на вход
# натуральное число n, а затем n строк, представляющих тексты комментариев. Для каждого комментария
# ваша программа должна выводить номер этого комментария (начиная с 1), затем двоеточие (:),
# затем через пробел его текст или сообщение «COMMENT SHOULD BE DELETED» (без кавычек),
# если комментарий должен быть удалён Сэмом.
num = int(input())
for i in range(num):
    s = input()
    if s.isspace() == True or s == '':
        print(i + 1, ':', ' COMMENT SHOULD BE DELETED', sep='')
    else:
        print(i + 1, ':', ' ', s, sep='')

n = int(input())
for i in range(1, n + 1):
    comment_text = input()
    if comment_text == '' or comment_text.isspace():
        comment_text = 'COMMENT SHOULD BE DELETED'
    print(i, ': ', comment_text, sep='')

# Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным
# автомобильным номером. Программа должна вывести «YES» (без кавычек), если искусственный интеллект
# справился со своей задачей, или «NO» (без кавычек) в противном случае. В нашей задаче корректным
# автомобильным номером будем считать следующие форматы:
#  <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
# <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>
# где <ЦИФРА> – это любая цифра, а <БУКВА> – это одна из букв кириллицы АВЕКМНОРСТУХ.
s = input().strip()
letters = "АВЕКМНОРСТУХ"
if (len(s) in (9, 10) and
    s[0] in letters and
    s[1].isdigit() and s[2].isdigit() and s[3].isdigit() and
    s[4] in letters and s[5] in letters and
    s[6] == "_" and
    s[7:].isdigit() and (len(s[7:]) in (2, 3))):
    print("YES")
else:
    print("NO")

s = input()
flag = 'NO'
correct_letters = 'АВЕКМНОРСТУХ'
if 9 <= len(s) <= 10:
    letters = s[0] + s[4:6]
    digits = s[1:4] + s[7:]
    underscore = s[6]
    if digits.isdigit() and underscore == '_':
        flag = 'YES'
    for c in letters:
        if c not in correct_letters:
            flag = 'NO'
            break
print(flag)

number = input()
template = ''
reg_1 = '<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>'
reg_2 = '<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>'
for i in number:
    if i in 'АВЕКМНОРСТУХ':
        template += '<БУКВА>'
    elif i.isdigit():
        template += '<ЦИФРА>'
    elif i == '_':
        template += '_'
    else:
        template = ' '
if template == reg_1 or template == reg_2:
    print('YES')
else:
    print('NO')

s = input()
total = 0
if len(s) >= 9:
    total += 1
    if s[0].isalpha() and s[4].isalpha() and s[5].isalpha():
        total += 1
        if s[1].isdigit() and s[2].isdigit() and s[3].isdigit():
            total += 1
            if s[7:].isdigit():
                total += 1
                if len(s[7:]) >= 2:
                    total += 1
                    if s[6] == '_':
                        total += 1
                        if s[0].isupper() and s[4:7].isupper():
                            total += 1
                            for i in range(len(s)):
                                if s[i] in 	'АВЕКМНОРСТУХ':
                                    total += 1
if total == 10:
    print('YES')
else:
    print('NO')

# Во время собеседования вам предложили решить задачу на валидацию имени пользователя.
# Пользователь пытается создать никнейм для своего аккаунта в соцсети Y. Правила для корректного
# никнейма в соцсети Y следующие: никнейм должен начинаться с символа @; никнейм должен содержать от 5 до
# 15 (включительно) символов (включая первый символ @); никнейм должен содержать только строчные буквы
# и (или) цифры (помимо первого символа @).
# Напишите программу, которая выводит «Correct» (без кавычек), если никнейм соответствует всем
# вышеприведенным правилам, или «Incorrect» (без кавычек) в противном случае.
s = input()
p = '@'
t = s[1:].isalnum()
if 4 < len(s) < 16 and s[0] == p and t and (s[1:].islower() or s[1:].isdigit()):
    print('Correct')
else:
    print('Incorrect')

s = input()
if (
    s.startswith('@')
    and 5 <= len(s) <= 15
    and s[1:].isalnum()
    and s == s.lower()
):
    print('Correct')
else:
    print('Incorrect')

s = input()
spl = s + 'a'  # добавили букву 'а', чтобы работал islower()
if s[:1] == '@' and 5 <= len(s) <= 15 and s[1:].isalnum() and spl.islower():
    print('Correct')
else:
    print('Incorrect')

n = input()
if 5 <= len(n) <= 15 and n[0] == '@':  # если строка от 5 до 15 и начинается с @
    n1 = n[1:]   # для удобства проверки отцепляем от строки первый символ срезом
    if n1.isalnum() and n1.islower() or n1.isdigit():  # если новая строка состоит только из букв
        # и цифр и они строчные ИЛИ новая строка состоит только из цифр
        print('Correct')  # выводим Correct
    else:
        print('Incorrect')  # иначе Incorrect
else:
    print('Incorrect')  # если первое условие (строка 2 программы) не выполняется,
                        # то сразу выводим Incorrect



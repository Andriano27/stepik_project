# программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
cntPw = int(input('Укажите количество паролей для генерации:'))
lenPw = int(input('Укажите длину одного пароля:'))
dig = input('Включать ли цифры 0123456789? (y/n)')
ABC = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
ch = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
exc = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
if dig == 'y':
    chars += digits
if ABC == 'y':
    chars += lowercase_letters
if abc == 'y':
    chars += uppercase_letters
if ch == 'y':
    chars += punctuation
if exc == 'y':
    for c in 'il1Lo0O':
        chars.replace(c, '')
def generate_password(len, chars):
    password = ''  # собираем пароль, для этого переходим к вложенному циклу:
    for _ in range(cntPw):  # в цикле for перебираем количество паролей для генерации, введенное пользователем
        for _ in range(lenPw):  # в цикле for перебираем количество символов для каждого пароля
            password += random.choice(chars)  # с помощью генератора добавляем символы в каждый пароль
        password += ' '  # между паролями вводим символ пробел
    return password  # возвращаем пароль
print(generate_password(len, chars))

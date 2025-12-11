alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
direction = input('Выбери направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ')
lang = int(input('Выбери язык алфавита: \n0 - Русский \n1 - Английский: \n'))
text = input('Введите текст для обработки:\n')
if direction == '-':
    print('\n=== Перебор всех сдвигов (0 - 25) ===')
    for step in range(26):
        print(f'\nСдвиг {step}: ', end="")
        for i in text:
            if i.isalpha():
                char = alph[lang][(alph[lang].index(i.upper()) - step) % len(alph[lang])]
                print(char if i.isupper() else char.lower(), end='')
            else:
                print(i, end='')
        print()
else:
    step = int(input('Веди число, шаг сдвига (0 - 25): '))
    print('\nРезультат: ', end="")
    for i in text:
        if i.isalpha():
            char = alph[lang][(alph[lang].index(i.upper()) + step) % len(alph[lang])]
            print(char if i.isupper() else char.lower(), end='')
        else:
            print(i, end='')
# На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными
# словами присутствует один пробел. Символы, не являющиеся английскими буквами, не изменяются.

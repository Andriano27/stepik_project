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
    print('\n=== Шифрование каждого слова сдвигом по длине ===')
    result = []
    word = ""

    for ch in text + " ":  # Добавляем пробел, чтобы обработать последнее слово
        if ch.isalpha():
            word += ch
        else:
            if word:
                step = len(word)  # сдвиг = длина слова
                encrypted = ""

                for i in word:
                    if i.isalpha():
                        char = alph[1][(alph[1].index(i.upper()) + step) % 26]
                        encrypted += char if i.isupper() else char.lower()
                    else:
                        encrypted += i

                result.append(encrypted)
                word = ""

            result.append(ch)

    print("\nРезультат:")
    print("".join(result))

def caesar_shift_char(ch, step):
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        return chr((
                               ord(ch) - base + step) % 26 + base)  # ord(ch) превращаем букву в число,
        # вычитаем base - это начало алфавита для строчных либо для заглавных, получаем номер буквы
        # в алфавите, прибавляем step - это шаг сдвига, % 26 - это циклический переход(после z снова идет a),
        # остаток от деления на 26 означает: пройди полный круг и начни сначала, + base - возвращаемся
        # от номера обратно к кодам символов, chr - превращаем число обратно в букву.
    return ch


text = input()

words = text.split()
result_words = []

for word in words:
    shift = sum(1 for ch in word if
                ch.isalpha())  # считаем только буквы, для каждой буквы взять число 1, получается список
    # по единицы за каждую букву, sum складывает эти единицы, это и будет количество букв в слове.
    new_word = ""

    for ch in word:
        new_word += caesar_shift_char(ch, shift)

    result_words.append(new_word)

print(" ".join(result_words))

##################################
eng_lower_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # Генерируем два английских алфавита
# upper and
eng_upper_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # lower

text = input()  # Запрашиваем строку для шифрования
text_1 = ''  # Создаем новую переменную в которую с помощью цикла добавляем слова
for i in range(len(text)):  # из запрошенного предложения без знаков препинания '.' ',' '!' ':' '"'
    if text[i] not in '.,!:"':
        text_1 += text[i]

text_list = text_1.split()  # Из полученной строки формируем список

result = []  # Создаем новый список в который будем добавлять зашифрованные символы
for c in text_list:  # С помощью вложенного цикла обрабатываем каждый символ каждого слова в списке
    for i in c:  # с шагом сдвига равным его длине (len(c))
        if i in eng_upper_alphabet:
            result += chr(((ord(i) - ord("A") + len(c)) % 26) + ord("A"))
        elif i in eng_lower_alphabet:
            result += chr(((ord(i) - ord("a") + len(c)) % 26) + ord("a"))

for i in range(len(text)):  # Сравниваем первоначально введенное предложение, расставляем знаки препинания
    if text[i] in '.,!:" ':  # на те индексы на которых они стояли изначально
        result.insert(i, text[i])

print(''.join(result))  # Используя метод join() выводим список


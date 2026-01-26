import random
word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово']
# функция выбора слова
def get_word():
    return random.choice(word_list)  # выбирает одно случайное слово, return возвращает его туда, где функция
    # вызвана
# функция печати слова с угаданными буквами
def print_word(word_, list_):  # word_ - загаданное слово, list_ - список угаданных букв
    for c in word_:  # проходим по каждой букве слова
        if c in list_:  # если буква уже угадана:
            print(c, end=' ')  # печатаем ее
        else:  # если не угадана:
            print('_', end=' ')  # - печатаем '_'
    print()  # перевод строки после вывода слова
# главная функция игры
def play(word):  # word -загаданное слово
    # тело функции
    word_completion = '_ ' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка(угадано ли слово целиком)
    guessed_letters = []  # угаданные буквы
    guessed_words = []  # слова, которые игрок уже пробовал
    tries = 6  # количество попыток
# старт игры
    print('Давайте играть в угадайку слов!')  # печатаем приветствие
    print(display_hangman(tries))  # рисуем виселицу
    print(word_completion)  # показываем слово из _ _ _
# основной игровой цикл
    while True:  # игра продолжается, пока не будет break
        word_input = input('Введите букву или слово: ').upper()  # ввод, перевод в верхний регистр
        if not word_input.isalpha():  # если введены не буквы - будет ошибка
            print('Вы ошиблись, попробуйте ещё')
            continue
        if word_input in guessed_words or word_input in guessed_letters:  # если уже вводили - предупреждение
            print('Уже было')
            continue
# если ввели слово целиком:
        if len(word_input) > 1:
            if word_input == word:  # угадал слово
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
            else:
                guessed_words.append(word_input)  # добавляем слово в список названных
                tries -= 1  # уменьшаем попытки
                print(f'Не верно, осталось попыток {tries}')
                print(display_hangman(tries))  # показываем виселицу
                print_word(word, guessed_letters)  # показываем текущее состояние слова
                if tries == 0:  # если попытки закончились
                    print(f'Вы не смогли угадать слово: {word}')
                    break
                continue
# если ввели одну букву:
        if word_input in word:
            guessed_letters.append(word_input)  # буква есть в слове
            for c in word:  # проверяем, все ли буквы уже угаданы:
                if c not in guessed_letters:  # если хоть одна не угадана - игра продолжается
                    print('Угадали букву')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True  # все буквы угаданы - победа
            if guessed:
                print_word(word, guessed_letters)
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
# если буквы нет:
        else:
            guessed_letters.append(word_input)  # ошибка
            tries -= 1  # минус попытка
            print(f'Не верно, осталось попыток {tries}')
            print(display_hangman(tries))  # показываем виселицу
            print_word(word, guessed_letters)  # показываем текущее состояние слова
        if tries == 0:  # если попытки закончились
            print(f'Вы не смогли угадать слово: {word}')
            break
# функция виселицы
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]  # индекс = количество попыток
play(get_word().upper())  # запуск игры(случайное слово, в верхнем регистре)
# print(get_word().upper())
# print(display_hangman(5))
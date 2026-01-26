
import random

# рисунки виселицы по количеству ошибок
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===
    ''',
    '''
     +---+
     O   |
         |
         |
        ===
    ''',
    '''
     +---+
     O   |
     |   |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|   |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
    /    |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    '''
]

words = ['кот', 'дом', 'мяч', 'лес', 'нос']

while True:
    word = random.choice(words).upper()
    guessed_letters = []
    tries = 6

    print('\n🎯 Игра: Виселица!')
    print('Попыток:', tries)

    while tries > 0:
        # показываем виселицу
        print(HANGMAN_PICS[6 - tries])

        # показываем слово
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

        guess = input('Введите букву: ').upper()

        if len(guess) != 1 or not guess.isalpha():
            print('Введите ОДНУ букву!')
            continue

        if guess in guessed_letters:
            print('Эта буква уже была!')
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print('Неверно! Осталось попыток:', tries)
        else:
            print('Верно!')

        # проверка победы
        win = True
        for letter in word:
            if letter not in guessed_letters:
                win = False

        if win:
            print('\n🎉 Поздравляем! Вы угадали слово:', word)
            break

    if tries == 0:
        print(HANGMAN_PICS[-1])
        print('😢 Вы проиграли!')
        print('Загаданное слово было:', word)

    # повтор игры
    again = input('\nСыграть ещё раз? (д/н): ').lower()
    if again != 'д':
        print('Спасибо за игру! 👋')
        break
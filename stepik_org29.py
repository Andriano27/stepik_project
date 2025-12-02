
_welcome_message = 'Добро пожаловать в числовую угадайку'
_bye_message = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
_play_again_message = 'Would you like to play again?'  # воспроизвести еще раз сообщение
_pay_message = 'Very good! Pay 1 USD :D'  # платное сообщение
_wrong_input_message = 'Wrong input'  # неправильное входное сообщение

_MIN = 1
_MAX = 100

def is_valid(st, min_val, max_val):
    if st.isnumeric():
        val = int(st)
        if min_val <= val <= max_val:
            return val
    return False

def get_guess():
    while True:
        val = is_valid(input('Type in your guess here:\n'), _MIN, _MAX)
        if val != False:
            return val
        print(f'А может быть все-таки введем целое число от {_MIN} до {_MAX}?')

def welcome():
    print(_welcome_message)  # 'Добро пожаловать в числовую угадайку'

def bye():
    print(_bye_message)  # 'Спасибо, что играли в числовую угадайку. Еще увидимся...'

def play_again():
    print(_play_again_message)  # 'Would you like to play again?'
    if input('Press "Y" to play again!\n').lower() == 'y':
        print(_pay_message)  # Very good! Pay 1 USD :D'
        s = input('Type your payment amount\n')  # Введите сумму платежа
        try:
            if s.isnumeric() and int(s) > 1:
                print('here is your change', int(s) - 1)  # вот твоя сдача
            return True
        except Exception as error:
            print(_wrong_input_message)  # 'Wrong input'
    else:
        return False

def game(num_to_guess):
    while True:
        guess = get_guess()  # предположение == догадался
        if num_to_guess == guess:  # число, чтобы угадать == предположение
            print('Holly shoot, man! You did it! :)))')  # Господи, чувак! Ты это сделал!
            break

        elif guess < num_to_guess:  # число, чтобы угадать > предположение
            print('Too low..')  # Слишком низко
        else:  # число, чтобы угадать < предположение
            print("You're thinking too BIG, dude!")  # Ты слишком масштабно мыслишь, чувак!



def start():
    from random import randint
    welcome()  # 'Добро пожаловать в числовую угадайку'
    while True:
        game(randint(_MIN, _MAX))
        if not play_again():
            break
    bye()  # 'Спасибо, что играли в числовую угадайку. Еще увидимся...'

start()
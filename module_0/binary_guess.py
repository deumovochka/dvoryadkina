import numpy as np
import math

def game_core_v3(number):
    '''Устанавливаем любое random число, потом уменьшаем или увеличиваем его в зависимости от того,
       больше оно или меньше нужного по методу двоичного/бинарного поиска.
       Функция принимает загаданное число и возвращает число попыток.'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count += 1
        if number > predict:
            predict = predict + math.ceil((number - predict)/2)
        elif number < predict:
            predict = predict - math.ceil((predict - number)/2)
    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число.'''
    count_ls = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)
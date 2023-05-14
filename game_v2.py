"""Угадай число.
Компьютер сам загадывает и угадывает число."""

import numpy as np

def random_predict(number: int=1) -> int:
    """ Угадываем случайное число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break # Выход из цикла, если угадали число
    return (count)
    
def score_game(random_predict) -> int:
    """ За какое количество попыток из 1000 подходов угадывает наш алгоритм в среднем

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: количество попыток в среднем
    """
    
    count_lst = [] # Список для хранения количества попыток угадывания
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_arrey = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    
    for number in random_arrey:
        count_lst.append(random_predict(number))
        
    score = int(np.mean(count_lst)) # Находим среднее количество попыток
    
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток.')
    return (score)

if __name__ == "__main__":
# RUN
    score_game(random_predict)
    
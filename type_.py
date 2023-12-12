from math import sqrt
from typing import Optional


# def <имя функции>(<аргумент>: <тип>) -> <возвращаемый тип>:
def add_numbers(int_x: int, int_y: int) -> int:
    return int_x + int_y


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number > 0:
        root = calculate_square_root(your_number)
        stroka = 'Мы вычислили '  # Слишком большая строка.
        stroka2 = 'квадратный корень из введённого'  # Слишком большая строка.
        stroka3 = ' вами числа. Это будет: '  # Слишком большая строка
        return stroka + stroka2 + stroka3 + str(root)


int_x = 10
int_y = 5

print('Сумма чисел: ', add_numbers(int_x, int_y))

print(calc(25.5))

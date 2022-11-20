from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Доументируем строку."""
    if your_number <= 0:
        sroot = calculate_square_root(your_number)
        return (f'Мы вычислили квадратный корень из введённого вами числа. '
                f'Это будет: {sroot}')


calc(25.5)

import numpy as np
from scipy.optimize import linprog

# Розв'язок максимуму
def search_max() -> None:
    # Коефіцієнти цільової функції
    c = [-3, -4]

    # Коефіцієнти обмежень
    A = [[-8, 5], [2, -5], [-6, 5], [2, 1]]
    b = [-40, 10, 60, 14]

    # Діапазон для x1 та x2
    x_bounds = [(0, None), (0, None)]

    result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

    if result.success:
        print("Максимальне значення функції:", -result.fun)
        print("Значення x1:", result.x[0])
        print("Значення x2:", result.x[1])
    else:
        print("Задача не має розв'язку.")

# Розв'язок мінімуму
def search_min() -> None:
    # Коефіцієнти цільової функції
    c = [3, 4]

    # Коефіцієнти обмежень
    A = [[8, -5], [-2, -5], [-6, 5], [2, 1]]
    b = [40, -10, 60, 14]

    result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    if result.success:
        print("Мінімальне значення функції:", result.fun)
        print("Значення x1:", result.x[0])
        print("Значення x2:", result.x[1])
    else:
        print("Задача не має розв'язку.")

if __name__ == '__main__':
    count_symbol_in_line = 50
    print("Програму розробив для ЛР № 2 з ДО Вальчевський П., група ОІ-11сп")
    print("=" * count_symbol_in_line)
    search_min()
    print("=" * count_symbol_in_line)
    search_max()
    print("=" * count_symbol_in_line)
    print("Програма завершила роботу")
from uniform_search import uniform_search_method


def target_function(self, x_):
    """целевая функция"""
    return 10 * (((x_ - 1) ** 2) ** (1 / 3)) / (x_ ** 2 + 9)


def fun(self, x_):
    return x_ + 2


class One_D_Problem:
    def __init__(self):
        self.left_border = 0.1  # интервал
        self.right_border = 1.5
        self.target_function = lambda a: target_function(self, a)

    uniform_search_method = uniform_search_method
    # target_function = target_function


    """
    Здесь добавляем методы решения данной задачи
    Методы возвращают два числа: 1) ответ 2) количество обращений к вычислению функции
    Метод равномерного поиска: (точность accuracy, число разбиений n) -> (ответ, то есть любая точка последнего интервала)
    Метод золотого сечения: (точность accuracy) -> (ответ, то есть любая точка последнего интервала)
    Метод пробных точек: (точность accuracy, ...) -> (ответ, то есть любая точка последнего интервала)
    """
    """
    Для каждого метода надо написать метод красивой печати
    """
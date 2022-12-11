import doctest
from typing import Union


class Pen:
    def __init__(self, colour: str, line_width: Union[int, float], percent_of_ink_left: float):
        """
        Инициализация и подготовка к работе объекта "Ручка"
        :param colour: цвет чернил
        :param line_width: толщина линии
        :param percent_of_ink_left: процент оставшихся чернил
        Пример:
        >>> pen = Pen("blue", 0.9, 99)
        """
        if not isinstance(colour, str):
            raise TypeError("Цвет ручки должен иметь тип строковой переменной")
        self.colour = colour

        if not isinstance(line_width, (int, float)):
            raise TypeError("Толщина линии должна иметь тип int или float")
        if line_width < 0:
            raise ValueError("Толщина линии не может быть отрицательным числом")
        self.line_width = line_width

        if not isinstance(percent_of_ink_left, (int, float)):
            raise TypeError("Процент оставшихся чернил выражается int или float")
        if percent_of_ink_left < 0:
            raise ValueError("Процент оставшихся чернил не может быть отрицательным числом")
        if percent_of_ink_left > 100:
            raise ValueError("Процент оставшихся чернил не может быть больше 100")
        self.percent_of_ink_left = percent_of_ink_left

    def is_empty_pen(self) -> bool:
        """
        Функция, которая проверяет, может ли ручка еще писать.

        :return: Значение типа Правда или Ложь, Правда соответствует закончившейся ручке, Ложь - ещё пишущей.

        Пример:
         >>> pen = Pen("blue", 0.9, 99)
         >>> pen.is_empty_pen()
         False
        """
        if self.percent_of_ink_left > 0:
            return False
        else:
            return True

    def write(self, expression: str) -> None:
        """
        Написание(выведение на печать) выражения ручкой с затратой чернил (1% на 100 знаков).

        :param expression: Выражение, которое будет написано ручкой.
        :raise: TypeError: Если выражение представлено не строковой переменной, возвращается ошибка.
        :raise: ValueError: Если выражение слишком длинное, чтобы написать его полностью,возвращается ошибка.

        Примеры:

        >>> pen = Pen("blue", 0.9, 99)
        >>> pen.write("This task is a serious challenge for my creative abilities")
        This task is a serious challenge for my creative abilities
        """
        if not isinstance(expression, str):
            raise TypeError("Выражение должно быть строковой переменной")
        if len(expression)*0.01 > self.percent_of_ink_left:
            raise ValueError("Выражение слишком длинное, вам не хватит чернил написать его полностью")
        self.percent_of_ink_left -= len(expression)*0.01
        print(expression)


class Tooth:
    def __init__(self, colour: int, number_in_the_row: int, is_healthy: bool):
        """
        Инициализация и подготовка к работе объекта "Зуб"

        :param colour: Цвет зуба по шкале Вита, от 1 до 16.
        :param number_in_the_row: Номер зуба в ряду, отсчитывая от центра.
        :param is_healthy: Аргумент, указывающий, является ли зуб здоровым.
        Пример:
        >>> tooth = Tooth(7, 3, True)
        """
        if not isinstance(colour, int):
            raise TypeError("Цвет зуба должен иметь тип int")
        if colour < 1:
            raise ValueError("Цвет зуба не может быть меньше 1")
        if colour > 16:
            raise ValueError("Цвет зуба не может быть больше 16")
        if not isinstance(number_in_the_row, int):
            raise TypeError("Номер зуба должен иметь тип int")
        if number_in_the_row < 1:
            raise ValueError("Номер зуба не может быть меньше 1")
        if number_in_the_row > 8:
            raise ValueError("Номер зуба не может быть больше 8")
        if not isinstance(is_healthy, bool):
            raise TypeError("Аргумент здоровья должен иметь тип bool")

        self.colour = colour
        self.number_in_the_row = number_in_the_row
        self.is_healthy = is_healthy

    def get_whitened(self, number_of_shades: int) -> None:
        """
        Метод, описывающий отбеливание зуба
        :param number_of_shades: число тонов, на которое зуб отбеливается
        >>> tooth = Tooth(7, 3, True)
        >>> tooth.get_whitened(4)
        """
        if not isinstance(number_of_shades, int):
            raise TypeError("Число оттенков должно иметь тип int")
        if number_of_shades > self.colour-1:
            raise ValueError("Число оттенков должно быть меньше номера цвета")
        ...

    def get_caries(self) -> None:
        """
        Метод, описывающий появление кариеса.
        Пример использования:
        >>> tooth = Tooth(7, 3, False)
        >>> tooth.get_caries()
        На этом зубе уже есть кариес.
        """
        if self.is_healthy:
            self.is_healthy = False
        else:
            print("На этом зубе уже есть кариес.")


class VideoGameCharacter:
    def __init__(self, name: str, health_points: int, strength: Union[int, float]):
        """
        Инициация и подготовка к работе объекта класса "Персонаж видеоигры"
        :param name: имя персонажа
        :param health_points: число очков здоровья
        :param strength: число очков силы
        Пример:
        >>> character = VideoGameCharacter("Josh", 10, 5)
        """
        if not isinstance(name, str):
            raise TypeError("Имя персонажа должно иметь тип str")
        if not isinstance(health_points, int):
            raise TypeError("Число единиц здоровья должно иметь тип int")
        if health_points < 0:
            raise ValueError("Число единиц здоровья должно быть положитеьным числом")
        if not isinstance(strength, (int, float)):
            raise TypeError("Число единиц cилы должно иметь или тип int, или тип float")
        if strength < 0:
            raise ValueError("Число единиц cилы должно быть положитеьным числом")

        self.name = name
        self.health_points = health_points
        self.strength = strength

    def levelup(self) -> None:
        """
        Метод, повышающий силу и здоровье персонажа

        Пример:
        >>> character = VideoGameCharacter("Josh", 10, 5)
        >>> character.levelup()
        """
        self.strength += 1
        self.health_points += 1

    def take_damage(self, points: Union[int, float]) -> None:
        """
        Метод, описывающий получение урона в определенное количество очков персонажем
        :param points:число очков урона
        Пример использования:

        >>> character = VideoGameCharacter("Josh", 10, 5)
        >>> character.take_damage(10)
        """
        if not isinstance(points, (int, float)):
            raise TypeError("Число единиц урона должно иметь или тип int, или тип float")
        ...


if __name__ == "__main__":
    doctest.testmod()



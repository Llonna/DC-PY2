class Book:
    def __init__(self, pages_count: int, cover_height: float):
        """
        Создание и подготовка к работе объекта "Книга"
        :param pages_count: Количество страниц
        :param cover_height: Высота обложки
        Примеры:
        >>> book = Book(365, 14)  # инициализация экземпляра класса
        """
        if not isinstance(pages_count, int):
            raise TypeError("Страницы считаются как int")
        if pages_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages_count = pages_count

        if not isinstance(cover_height, float):
            raise TypeError("Высота обложки должна быть float")
        if cover_height <= 0:
            raise ValueError("Высота книги не может быть отрицательным числом")
        self.cover_height = cover_height
        ...

    def is_big_book(self) -> bool:
        """
        Функция, которая проверяет, является ли книга фолиантом
        :return: Является ли книга фолиантом
        Примеры:
         >>> book = Book(365, 14)
         >>> book.is_big_book()
         """
        ...
class Bottle:
    def __init__(self, material: str, capacity_volume: float):
        """
        Создание и подготовка к работе объекта "Бутылка"
        :param material: Материал бутылки
        :param capacity_volume: Объём бутылки
        Примеры:
        >>> bottle = Bottle("glass", 0)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал задаётся как string")
        self.material = material

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume
        ...

    def is_reusable_bottle(self) -> bool:
        """
        Функция, которая проверяет, является ли бутылка такого материала многоразовой
        :return: Является ли бутылка многоразовой
        Примеры:
        >>> bottle = Book("glass", 0)
        >>> bottle.is_reusable_bottle()
        """
        ...
class Plant:
    def __init__(self, name: str, leaf_color: str, food_preferences: str):
        """
        Создание и подготовка к работе объекта "Растение"
        :param name: Наименование растения
        :param leaf_color: Цвет листьев
        :param food_preferences: Плотоядные или нет
        Примеры:
        >>> plant = Plant("fern", "burgundy", "meat")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название задаётся как string")
        self.name = name
        if not isinstance(leaf_color, str):
            raise TypeError("Цвет листьев задаётся как string")
        self.leaf_color = leaf_color
        if not isinstance(leaf_color, str):
            raise TypeError("Цвет листьев задаётся как string")
        self.leaf_color = leaf_color
        ...
    def is_carnivorous_plant(self) -> bool:
        """
        Функция, которая проверяет, является ли растение плотоядным
        :return: Является ли растение плотоядным
        Примеры:
        >>> plant = Plant("fern", "burgundy", "meat")
        >>> plant.is_carnivorous_plant()
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()

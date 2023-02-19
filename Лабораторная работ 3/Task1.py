class Book:
    def __init__(self, name: str, author: str):
        # Атрибуты name и author изменяться не могут
        self.__name = name
        self.__author = author

    def __str__(self):
        return f'Книга называется {self.__name!r}, её автор - {self.__author!r}.'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__name!r}, {self.__author!r})'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц книги должно быть типа int.")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.pages = pages

    def __str__(self):
        str_super = super().__str__()
        return f'{str_super}. Кoл-во страниц {self.pages}.'

    def __repr__(self):
        repr_super = super().__repr__()
        return f'{self.__class__.__name__}({repr_super}, {self.pages})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, int):
            raise TypeError("Длительность книги должна быть типа float.")
        if duration < 0:
            raise ValueError("Длительность книги должна быть положительным числом.")
        self.duration = duration

    def __str__(self):
        super_str = super().__str__()
        return f'{super_str}. Длительность аудио {self.duration}.'

    def __repr__(self):
        repr_super = super().__repr__()
        return f'{self.__class__.__name__}({repr_super}, {self.duration})'


if __name__ == '__main__':
    paper_book = PaperBook("Безуиный корабль", "Робин Хобб", 927)
    print(paper_book)
    audio_book = AudioBook("Безуиный корабль", "Робин Хобб", 40.57)
    print(audio_book)
